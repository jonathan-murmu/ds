from .relation import Relation
from constants import FEMALE, MALE


class PaternalAunt(Relation):
      """Get the children of the main member in the family."""
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
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