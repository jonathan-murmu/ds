import utils


# Relatioinship Mapper
RELATION = {
    "Paternal uncle": None,
    "Maternal uncle": None,
    "Paternal aunt":None,
    "Maternal aunt": None,
    "Sister-in law": None,
    "Brother-inlaw": None,
    "Cousins": None,
    "Father": utils.get_father,
    "Mother": utils.get_mother,
    "Children": utils.get_children,
    "Sons": utils.get_sons,
    "Daughters": utils.get_daughters,
    "Brothers": utils.get_brothers,
    "Sisters": utils.get_sisters,
    "Grand daughter": utils.get_grand_daughter
}

class Generation(object):
    def __init__(self, family=None):
        self.root_family = family
        # has all the names of the person and to which family he/she belongs
        self.person_dict = {}
        self.size = 0 # no. of families in this generations
    
    def get_family(self, name):
        try:
            return self.person_dict[name]
        except:
            return None # the person does not have a family.
    
    def add_child_family(self, parent_name, child_family):
        """Add a child family in the Generation Tree.
        
        :param: parent_name- main member name of the parent in which to add the child family.
        :param: child_family- the familly object of the child."""
        if not parent_name and not child_family:
            return "Please specify the parent name and the child family"
        
        parent_family = self.get_family(parent_name)
        if not parent_family:
            return "No family found for the name: {0}".format(parent_name)
        
        child_family.parent = parent_family
        parent_family.child_family.append(child_family)


