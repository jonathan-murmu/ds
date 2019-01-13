from constants import FEMALE, MALE


def get_father(family):
    if family.parents.main_member.gender == MALE:
        return family.parents.main_member.name
    else:
        return family.parents.spouse.name

def get_mother(family):
    if family.parents.main_member.gender == FEMALE:
        return family.parents.main_member.name
    else:
        return family.parents.spouse.name

def get_children(family):
    children = family.child_family
    children_names = [child.main_member.name for child in children]
    return children_names

def get_sons(family):
    """Sons in the family."""
    children = family.child_family
    sons = [child.main_member.name for child in children if child.main_member.gender == MALE]
    return sons

def get_daughters(family):
    """Daughters in the family."""
    return [child.main_member.name for child in family.child_family if child.main_member.gender == FEMALE]
     
def get_brothers(family):
    """Get the brother of the main member in the family."""
    sibling_families = family.parents.child_family
    brothers = [sibling.main_member.name for sibling in sibling_families if sibling.main_member.gender == MALE]
    return brothers

def get_sisters(family):
    return [sibling.main_member.name for sibling in family.parents.child_family if sibling.main_member.gender == FEMALE]

def get_grand_daughter(family):
    g_children = []
    if not family.child_family:
        return g_children
    for child in family.child_family:
        if not child.child_family:
            continue
        for g_child in child.child_family:
            g_children.append(g_child.main_member.name)

    return g_children
