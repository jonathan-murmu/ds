from .relation import Relation
from constants import FEMALE, MALE


class Sisters(Relation):
      """Get the sistes of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
            sibling_families = family.parent.child_family
            sisters = []
            for sibling in sibling_families:
                # skip himself
                if sibling == family:
                    continue
                if sibling.main_member.gender == FEMALE:
                    sisters.append(sibling.main_member.name)
            return sisters
