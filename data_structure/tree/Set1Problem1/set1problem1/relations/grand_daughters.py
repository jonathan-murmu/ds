from .relation import Relation
from ..constants import FEMALE, MALE


class GrandDaughter(Relation):
      """Get the grand daughters of the main member in the family."""

      def get_relatives(self, person_name, relation, family):
            g_children = []
            if not family.child_family:
                return g_children
            for child in family.child_family:
                if not child.child_family:
                    continue
                for g_child in child.child_family:
                    if g_child.main_member.gender == FEMALE:
                        g_children.append(g_child.main_member.name)
            
            return g_children