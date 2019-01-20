from .relation import Relation
from constants import FEMALE, MALE


class Mother(Relation):
      """Get the mother of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            if family.parent.main_member.gender == FEMALE:
                return family.parent.main_member.name
            else:
                return family.parent.spouse.name