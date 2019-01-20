from .relation import Relation
from ..constants import MALE
from .sibling import Sibling


class Brothers(Relation, Sibling):
      """Get the brother of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_sibling(family, MALE)