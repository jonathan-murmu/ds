from .relation import Relation
from ..constants import FEMALE, MALE
from .sibling_in_law import SiblingInLaw


class BrotherInLaw(Relation, SiblingInLaw):
      """Get the children of the main member in the family."""
      
      def get_relatives(self, person_name, relation, family):
          return self.get_sibling_in_law(person_name, relation, family, MALE)
