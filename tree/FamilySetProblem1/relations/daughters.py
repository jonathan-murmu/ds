from .relation import Relation
from constants import FEMALE, MALE


class Daughters(Relation):
      """Get the daughters of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return [child.main_member.name for child in family.child_family if child.main_member.gender == FEMALE]
