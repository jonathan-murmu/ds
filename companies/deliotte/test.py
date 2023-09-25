# int to string


def int_to_string(num):
    result_str = ''

    while num != 0:
        last_digit = num % 10
        num = num // 10  # excluding the last digit

        result_str += str(last_digit)

    result_str = result_str[::-1]

    return result_str

print(int_to_string(123))

