from .relation import Relation
from ..constants import MALE
from .uncle import Uncle


class PaternalUncle(Relation, Uncle):
      """Get the paternal uncle of the main member in the family."""
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            return self.get_uncle(person_name, relation, family, MALE)