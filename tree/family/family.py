# PERSON_ADDRESS has all the names of the person, and to which family he/she belongs
# key- person name
# value- family's address(object/instance)
PERSON_ADDRESS = {}

class Family(object):
    """Family class.

    Family class acts as a node in the generation tree. Having reference to its parent.
    """
    def __init__(self, parent=None, main_member=None, spouse=None, child_family=None):
        self.parent = parent  # a Family object, 
        self.main_member = main_member  # a Person object
        self.spouse = spouse  # a Person object
        self.child_family = child_family or []  # list of child Family objects
        
        if self.main_member:
            self.update_address(self.main_member.name, self)
        if self.spouse:
            self.update_address(self.spouse.name, self)
    
    def update_address(self, name, address):
        PERSON_ADDRESS.update({name: address})

      