from .relation import Relation
from ..constants import FEMALE, MALE


class Children(Relation):
      """Get the children of the family."""
      
      def get_relatives(self, person_name, relation, family):
            children = family.child_family
            children_names = [child.main_member.name for child in children]
            return children_names