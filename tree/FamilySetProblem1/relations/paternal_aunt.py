from .relation import Relation
from constants import MALE
from .aunt import Aunt


class PaternalAunt(Relation, Aunt):
      """Get the children of the main member in the family."""
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_aunt(person_name, relation, family, MALE)
