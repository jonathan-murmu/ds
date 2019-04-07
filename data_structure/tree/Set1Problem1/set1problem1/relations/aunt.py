from ..constants import FEMALE

class Aunt(object):
    """Get Aunt."""
    def get_aunt(self, person_name, relation, family, gender):
        # the mother is the main member, only then she has maternal aunt
        if family.parent.main_member.gender == gender:
            uncle_aunt_families = family.parent.parent.child_family
            aunt = []
            for uncle_aunt in uncle_aunt_families:
                if uncle_aunt == family.parent:
                    continue
                if uncle_aunt.main_member.gender == FEMALE:
                    aunt.append(uncle_aunt.main_member.name)
                if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == FEMALE:
                    aunt.append(uncle_aunt.spouse.name)
            return aunt
        else:
            return "{0} does not have own {1}.".format(person_name, relation.lower())