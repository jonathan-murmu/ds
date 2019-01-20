class Sibling(object):
    """Get the siblings."""
    def get_sibling(self, family, gender):
        sibling_families = family.parent.child_family
        siblings = []
        for sibling in sibling_families:
            # skip himself
            if sibling == family:
                continue
            if sibling.main_member.gender == gender:
                siblings.append(sibling.main_member.name)
        return siblings
