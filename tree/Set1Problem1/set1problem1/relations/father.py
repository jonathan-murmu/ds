from .relation import Relation
from ..constants import FEMALE, MALE
from .parent import Parent


class Father(Relation, Parent):
      """Get the father of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            try:
                return self.get_parent(family, MALE)
            except:
                return "{0} does not have own {1}.".format(person_name, relation.lower())