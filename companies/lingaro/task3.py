# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def check_available_slots(parcel_size, locker_details):
    """is sloth availabl in current locker."""
    if locker_details["available_slots"][parcel_size] > 0:
        return True
    else:
        return False


def get_one_size_bigger(cur_size):
    next_size_mapper = {
        "S": "M",
        "M": "L"
    }

    return next_size_mapper[cur_size]


def compose_result(is_locker_changed=False, locker_id=None, slot_size=None):
    result = {
        "is_locker_changed": is_locker_changed,
        "locker_id": locker_id,
        "slot_size": slot_size
    }
    return result


def check_current_available(parcel_size, locker_details, is_locker_changed=False):
    locker_id = locker_details["id"]
    # check if size if available.
    is_slot_available = check_available_slots(parcel_size, locker_details)
    if is_slot_available:
        return compose_result(is_locker_changed=is_locker_changed, locker_id=locker_id, slot_size=parcel_size)

    if parcel_size == 'L':
        # do not check for next bigger size.
        return False
    # if size not available look in only one size bigger in same locker.
    new_size = get_one_size_bigger(parcel_size)
    is_slot_available = check_available_slots(new_size, locker_details)

    if is_slot_available:
        return compose_result(is_locker_changed=is_locker_changed, locker_id=locker_id, slot_size=new_size)

    return False  # not found


def distance(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def arrange_lockers(interface: "Interface", cur_locker_details=None, lockers=None):
    cur_locker_id = cur_locker_details["id"]
    cur_locker_location = cur_locker_details["location"]
    cur_x1 = cur_locker_location[0]
    cur_y1 = cur_locker_location[1]

    dist_dict = {}

    for locker in lockers:
        locker_details = interface.get_locker_details(locker)
        next_locker_location = locker_details["location"]
        next_x1 = next_locker_location[0]
        next_y1 = next_locker_location[1]

        dist = distance(x1=cur_x1, y1=cur_y1, x2=next_x1, y2=next_y1)
        dist_dict[locker] = dist

    lockers = sorted(dist_dict.items(), key=lambda x: x[1])
    lockers = [i[0] for i in lockers]
    return lockers


def choose_locker_slot(interface: "Interface", parcel_id: str):
    # implement your solution here

    # get parchel details
    parcel_details = interface.get_parcel_details(parcel_id)
    print(parcel_details)
    parcel_size = parcel_details['size']
    locker_id = parcel_details['locker']

    # now get the locker details
    locker_details = interface.get_locker_details(locker_id)
    post_code = locker_details["postcode"]

    # # check if size if available.
    result = check_current_available(parcel_size, locker_details)
    if result:
        return result

    # if not available look for lockers in the nearby postcode
    nearby_postcodes = interface.get_nearby_postcodes(post_code)

    for next_postcode in nearby_postcodes:
        lockers = interface.get_lockers(next_postcode)

        lockers = arrange_lockers(interface, cur_locker_details=locker_details, lockers=lockers)
        print('new locker', lockers)
        for next_locker in lockers:
            next_locker_details = interface.get_locker_details(next_locker)
            print('next_locker_details', next_locker_details)

            result = check_current_available(parcel_size, next_locker_details, is_locker_changed=True)
            print('result', result)
            if result:
                return result

    return None

    print("this is a debug message")
    result = {
        "is_locker_changed": "",
        "locker_id": "",
        "slot_size": ""
    }
    return result
