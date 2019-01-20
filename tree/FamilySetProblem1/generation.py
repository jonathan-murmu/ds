import constants
from family import PERSON_ADDRESS
from relationfactory import RelationFactory


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
        # return RELATION[relation](person_name, relation, family)
        RELATION = {
            constants.BROTHERS: constants.BROTHERS_CLASS,
            constants.MOTHER: constants.MOTHER_CLASS,
            constants.FATHER: constants.FATHER_CLASS,
            constants.SONS: constants.SONS_CLASS,
            constants.SISTERS: constants.SISTERS_CLASS,
            constants.DAUGHTERS: constants.DAUGHTERS_CLASS,
            constants.CHILDREN: constants.CHILDREN_CLASS,
            constants.BROTHER_IN_LAW: constants.BROTHER_IN_LAW_CLASS,
            constants.SISTER_IN_LAW: constants.SISTER_IN_LAW_CLASS,
            constants.MATERNAL_AUNT: constants.MATERNAL_AUNT_CLASS,
            constants.MATERNAL_UNCLE: constants.MATERNAL_UNCLE_CLASS,
            constants.PATERNAL_AUNT: constants.PATERNAL_AUNT_CLASS,
            constants.PATERNAL_UNCLE: constants.PATERNAL_UNCLE_CLASS,
            constants.GRAND_DAUGHTER: constants.GRAND_DAUGHTER_CLASS,
            constants.COUSINS: constants.COUSINS_CLASS
        }
        relation_name = relation
        factory = RelationFactory()
        relation = factory.create_instance(RELATION[relation])
        return relation.get_relatives(person_name, relation_name, family)
