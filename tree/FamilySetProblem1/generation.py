from family import PERSON_ADDRESS
from utils import (
    get_brothers, get_brother_in_law,
    get_children, get_cousins,
    get_daughters,
    get_father,
    get_grand_daughter,
    get_maternal_aunt, get_maternal_uncle, get_mother,
    get_paternal_aunt, get_paternal_uncle,
    get_sisters, get_sister_in_law, get_sons
)

# Relatioinship Mapper- Maps particular relation to coresponding helper function.
RELATION = {
    "Paternal uncle": get_paternal_uncle,
    "Maternal uncle": get_maternal_uncle,
    "Paternal aunt":get_paternal_aunt,
    "Maternal aunt": get_maternal_aunt,
    "Sister-in law": get_sister_in_law,
    "Brother-in law": get_brother_in_law,
    "Cousins": get_cousins,
    "Father": get_father,
    "Mother": get_mother,
    "Children": get_children,
    "Sons": get_sons,
    "Daughters": get_daughters,
    "Brothers": get_brothers,
    "Sisters": get_sisters,
    "Grand daughter": get_grand_daughter
}

class Generation(object):
    """Generation Class.

    Tree data structure is used to implemented the generation hierarchy. With root_family holding 
    the reference to family node.
    """
    def __init__(self, family=None):
        self.root_family = family
        self.size = 0 # no. of families in this generations
    
    def get_family(self, name):
        """Use the PERSON_ADDRESS dictionary to efficiently get the family object"""
        try:
            return PERSON_ADDRESS[name]
        except:
            return None # the person does not have a family.
    
    def add_child_family(self, parent_name=None, child_family=None):
        """Add a child family to the Generation Tree.
        
        The family is node is already created. The reference is the family node is added in the tree.
        :param: parent_name- main member name of the parent in which to add the child family.
        :param: child_family- the familly object of the child."""
        # if the generation tree is empty
        if not self.root_family:
            self.root_family=child_family
            self.size += 1
            return
            
        if not parent_name and not child_family:
            return "Please specify the parent name and the child family"
        
        parent_family = self.get_family(parent_name)
        if not parent_family:
            return "No family found for the name: {0}".format(parent_name)
        
        
        child_family.parent = parent_family
        parent_family.child_family.append(child_family)
        self.size += 1

    def relationship(self, person_name=None, relation=None):
        """Given the person name and relation, get his/her relatives."""
        family = self.get_family(person_name)
        if not family:
            return "No family found for the name: {0}".format(person_name)
        
        # dynamically call the corresponding utility function based on relation
        return RELATION[relation](person_name, relation, family)



