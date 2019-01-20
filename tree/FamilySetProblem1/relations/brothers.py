from .relation import Relation
from constants import FEMALE, MALE


class Brothers(Relation):
      """Get the brother of the main member in the family."""
      
      @Relation.is_main_member
      def get_relatives(self, person_name, relation, family):
          sibling_families = family.parent.child_family
          brothers = []
          for sibling in sibling_families:
              # skip himself
              if sibling == family:
                  continue
              if sibling.main_member.gender == MALE:
                  brothers.append(sibling.main_member.name)
          return brothers