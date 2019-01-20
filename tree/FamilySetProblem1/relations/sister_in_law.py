from .relation import Relation
from constants import FEMALE
from .sibling_in_law import SiblingInLaw


class SisterInLaw(Relation, SiblingInLaw):
      """Get the children of the main member in the family."""
      
      def get_relatives(self, person_name, relation, family):
            return self.get_sibling_in_law(person_name, relation, family, FEMALE)