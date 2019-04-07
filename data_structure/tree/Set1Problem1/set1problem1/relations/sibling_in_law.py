class SiblingInLaw(object):
    """Get the siblings in law."""
    def get_sibling_in_law(self, person_name, relation, family, gender):
        # if he/she is not the main member, only then he/she has "in-laws".
        if family.main_member.name != person_name:
            sibling_families = family.parent.child_family
            sibling_in_law = []
            for sibling in sibling_families:
                # skip himself
                if sibling == family:
                    continue
                if sibling.main_member.gender == gender:
                    sibling_in_law.append(sibling.main_member.name)
        else:
            return "{0} does not have own {1}.".format(person_name, relation.lower())
            
        return sibling_in_law
