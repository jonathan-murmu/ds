from .relation import Relation
from constants import FEMALE, MALE


class Father(Relation):
      """Get the father of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            if family.parent.main_member.gender == MALE:
                return family.parent.main_member.name
            else:
                return family.parent.spouse.name