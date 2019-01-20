from .relation import Relation
from ..constants import FEMALE, MALE


class Daughters(Relation):
      """Get the daughters of the family."""
      
      def get_relatives(self, person_name, relation, family):
            return [child.main_member.name for child in family.child_family if child.main_member.gender == FEMALE]
