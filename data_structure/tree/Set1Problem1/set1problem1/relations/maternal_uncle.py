from .relation import Relation
from ..constants import FEMALE
from .uncle import Uncle


class MaternalUncle(Relation, Uncle):
      """Get the maternal uncle of the main member in the family."""
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_uncle(person_name, relation, family, FEMALE)
