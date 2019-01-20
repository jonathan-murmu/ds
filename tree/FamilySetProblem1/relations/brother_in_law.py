from .relation import Relation
from constants import FEMALE, MALE


class BrotherInLaw(Relation):
      """Get the children of the main member in the family."""
      
      def get_relatives(self, person_name, relation, family):
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