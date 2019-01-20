import collections

from .constants import FEMALE, MALE


def is_main_member(func):
    """Docorator to check if the person is the blood son/daughter i.e. the main member or not."""
    def _is_main_member(person_name, relation, family):
        print(person_name, relation, family)
        if family.main_member.name != person_name:
            return "{0} does not have own {1}.".format(person_name, relation.lower())
        else:
            # calling the function
            return func(person_name, relation, family)
    return _is_main_member

@is_main_member
def get_father(person_name, relation, family):
    if family.parent.main_member.gender == MALE:
        return family.parent.main_member.name
    else:
        return family.parent.spouse.name

@is_main_member
def get_mother(person_name, relation, family):
    if family.parent.main_member.gender == FEMALE:
        return family.parent.main_member.name
    else:
        return family.parent.spouse.name

def get_children(person_name, relation, family):
    children = family.child_family
    children_names = [child.main_member.name for child in children]
    return children_names

def get_sons(person_name, relation, family):
    """Sons in the family"""
    children = family.child_family
    sons = [child.main_member.name for child in children if child.main_member.gender == MALE]
    return sons

def get_daughters(person_name, relation, family):
    """Daughters in the family."""
    return [child.main_member.name for child in family.child_family if child.main_member.gender == FEMALE]

@is_main_member
def get_brothers(person_name, relation, family):
    """Get the brother of the main member in the family."""
    sibling_families = family.parent.child_family
    brothers = []
    for sibling in sibling_families:
        # skip himself
        if sibling == family:
            continue
        if sibling.main_member.gender == MALE:
            brothers.append(sibling.main_member.name)
    return brothers

def get_brother_in_law(person_name, relation, family):
    # if he/she is not the main member, only then he/she has "in-laws".
    if family.main_member.name != person_name:
        sibling_families = family.parent.child_family
        brothers = []
        for sibling in sibling_families:
            # skip himself
            if sibling == family:
                continue
            if sibling.main_member.gender == MALE:
                brothers.append(sibling.main_member.name)
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())
        
    return brothers

@is_main_member
def get_sisters(person_name, relation, family):
    sibling_families = family.parent.child_family
    brothers = []
    for sibling in sibling_families:
        # skip himself
        if sibling == family:
            continue
        if sibling.main_member.gender == FEMALE:
            brothers.append(sibling.main_member.name)
    return brothers

def get_sister_in_law(person_name, relation, family):
    # if he/she is not the main member, only then he/she has "in-laws".
    if family.main_member.name != person_name:
        sibling_families = family.parent.child_family
        sisters = []
        for sibling in sibling_families:
            # skip himself
            if sibling == family:
                continue
            if sibling.main_member.gender == FEMALE:
                sisters.append(sibling.main_member.name)
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())
        
    return sisters

def get_grand_daughter(person_name, relation, family):
    g_children = []
    if not family.child_family:
        return g_children
    for child in family.child_family:
        if not child.child_family:
            continue
        for g_child in child.child_family:
            if g_child.main_member.gender == FEMALE:
                g_children.append(g_child.main_member.name)

    return g_children
@is_main_member
def get_cousins(person_name, relation, family):
    uncle_aunt_families = family.parent.parent.child_family
    cousin_name = []
    for uncle_aunt in uncle_aunt_families:
        for cousins in uncle_aunt.child_family:
            cousin_name.append(cousins.main_member.name)
    return cousin_name

@is_main_member
def get_maternal_aunt(person_name, relation, family):
    # the mother is the main member, only then she has maternal aunt
    if family.parent.main_member.gender == FEMALE:
        uncle_aunt_families = family.parent.parent.child_family
        maternal_aunt = []
        for uncle_aunt in uncle_aunt_families:
            if uncle_aunt == family.parent:
                continue
            if uncle_aunt.main_member.gender == FEMALE:
                maternal_aunt.append(uncle_aunt.main_member.name)
            if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == FEMALE:
                maternal_aunt.append(uncle_aunt.spouse.name)
        return maternal_aunt
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())

@is_main_member
def get_maternal_uncle(person_name, relation, family):
    # the mother is the main member, only then he has maternal uncle
    if family.parent.main_member.gender == FEMALE:
        uncle_aunt_families = family.parent.parent.child_family
        maternal_uncle = []
        for uncle_aunt in uncle_aunt_families:
            if uncle_aunt == family.parent:
                continue
            if uncle_aunt.main_member.gender == MALE:
                maternal_uncle.append(uncle_aunt.main_member.name)
            if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == MALE:
                maternal_uncle.append(uncle_aunt.spouse.name)
        return maternal_uncle
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())

@is_main_member
def get_paternal_aunt(person_name, relation, family):
    # the father is the main member, only then he has paternal aunt
    if family.parent.main_member.gender == MALE:
        uncle_aunt_families = family.parent.parent.child_family
        maternal_aunt = []
        for uncle_aunt in uncle_aunt_families:
            if uncle_aunt == family.parent:
                continue
            if uncle_aunt.main_member.gender == FEMALE:
                maternal_aunt.append(uncle_aunt.main_member.name)
            if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == FEMALE:
                maternal_aunt.append(uncle_aunt.spouse.name)
        return maternal_aunt
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())

@is_main_member
def get_paternal_uncle(person_name, relation, family):
    # the father is the main member, only then he has paternal aunt
    if family.parent.main_member.gender == MALE:
        uncle_aunt_families = family.parent.parent.child_family
        maternal_aunt = []
        for uncle_aunt in uncle_aunt_families:
            if uncle_aunt == family.parent:
                continue
            if uncle_aunt.main_member.gender == MALE:
                maternal_aunt.append(uncle_aunt.main_member.name)
            if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == MALE:
                maternal_aunt.append(uncle_aunt.spouse.name)
        return maternal_aunt
    else:
        return "{0} does not have own {1}.".format(person_name, relation.lower())


def display(tree):
    """Tree level order traversal"""
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        if currentNode.main_member:
            main_member = currentNode.main_member.name
            main_member_gender = currentNode.main_member.gender
        else:
            main_member = main_member_gender = ''

        if currentNode.spouse:
            spouse = currentNode.spouse.name
            spouse_gender = currentNode.spouse.gender
        else:
            spouse = spouse_gender = ''

        print("{0}({1})-{2}({3})".format(main_member, main_member_gender, spouse, spouse_gender), end=', ' )
        nodes = nodes + collections.deque(currentNode.child_family)
        nextCount += len( currentNode.child_family)
        
        if currentCount==0:
            #finished printing current level
            print('\n')
            currentCount, nextCount = nextCount, currentCount