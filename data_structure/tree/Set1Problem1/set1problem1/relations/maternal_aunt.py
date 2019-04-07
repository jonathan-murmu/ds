from .relation import Relation
from ..constants import FEMALE
from .aunt import Aunt


class MaternalAunt(Relation, Aunt):
      """Get the maternal aunt of the main member in the family."""
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_aunt(person_name, relation, family, FEMALE)