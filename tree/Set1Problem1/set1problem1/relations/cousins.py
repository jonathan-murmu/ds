from .relation import Relation
from ..constants import FEMALE, MALE


class Cousins(Relation):
        """Get the grand daughters of the main member in the family."""

        @Relation.is_main_member
        def get_relatives(self, person_name, relation, family):
                try:
                    uncle_aunt_families = family.parent.parent.child_family
                except:
                    return "{0} does not have own {1}.".format(person_name, relation.lower())
                cousin_name = []
                for uncle_aunt in uncle_aunt_families:
                    for cousins in uncle_aunt.child_family:
                        if cousins == family:
                            continue
                        cousin_name.append(cousins.main_member.name)
                return cousin_name