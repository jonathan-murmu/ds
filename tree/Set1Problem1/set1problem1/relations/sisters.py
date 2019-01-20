from .relation import Relation
from ..constants import FEMALE
from .sibling import Sibling


class Sisters(Relation, Sibling):
      """Get the sistes of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_sibling(family, FEMALE)
