class Parent(object):
    """Mother or Father class."""
    def get_parent(self, family, gender):
        """Given the gender, returns Mother or Father."""
        if family.parent.main_member.gender == gender:
            return family.parent.main_member.name
        else:
            return family.parent.spouse.name
