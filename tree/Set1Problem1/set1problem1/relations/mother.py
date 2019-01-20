from .relation import Relation
from ..constants import FEMALE, MALE
from .parent import Parent


class Mother(Relation, Parent):
      """Get the mother of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_parent(family, FEMALE)