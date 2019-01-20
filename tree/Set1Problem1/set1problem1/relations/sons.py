from .relation import Relation
from ..constants import FEMALE, MALE


class Sons(Relation):
      """Get the father of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            children = family.child_family
            sons = [child.main_member.name for child in children if child.main_member.gender == MALE]
            return sons