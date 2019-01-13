from constants import PERSON_ADDRESS


class Family(object):
    def __init__(self, parents=None, main_member=None, spouse=None, child_family=None):
        self.parents = parents  # a Family object, 
        self.main_member = main_member  # a Person object
        self.spouse = spouse  # a Person object
        self.child_family = child_family or []  # list of child Family objects
        
        if self.main_member:
            self.update_address(self.main_member.name, self)
        if self.spouse:
            self.update_address(self.spouse.name, self)
    
    def update_address(self, name, address):
        PERSON_ADDRESS.update({name: address})
    
    def marriage(self, new_person):
        """Then main member of the family  is married to the new person."""
        self.spouse = new_person
        self.update_address(self.spouse.name, self) # the new person's family adddress is then updated
    
    def has_no_child_family(self):
        """Has no children or leaf node in a tree."""
        return not self.child_family
        
    
#     def add_child_family(self, child_family):
#         # add the new family to the list of children to the current family
#         self.child_family.append(child_family)
#         # add this family as the parent of the new family.
#         child_family.parents = self
      