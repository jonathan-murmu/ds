from constants import MALE

class Uncle(object):
    """Get uncle."""
    def get_uncle(self, person_name, relation, family, gender):
        # the mother is the main member, only then he has maternal uncle
        if family.parent.main_member.gender == gender:
            uncle_aunt_families = family.parent.parent.child_family
            uncle = []
            for uncle_aunt in uncle_aunt_families:
                if uncle_aunt == family.parent:
                    continue
                if uncle_aunt.main_member.gender == MALE:
                    uncle.append(uncle_aunt.main_member.name)
                if (uncle_aunt.spouse) and uncle_aunt.spouse.gender == MALE:
                    uncle.append(uncle_aunt.spouse.name)
            return uncle
        else:
            return "{0} does not have own {1}.".format(person_name, relation.lower())