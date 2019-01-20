from inspect import getmembers,  isclass, isabstract
from . import relations

class RelationFactory(object):
    relation = {}  # Key = relation name, Value = class for the relation

    def __init__(self):
        self.load_relations()

    def load_relations(self):
        classes = getmembers(relations, 
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, relations.Relation):
                self.relation.update([[name, _type]])

    def create_instance(self, relation_name):
        if relation_name in self.relation:
            return self.relation[relation_name]()
        else:
            return relations.NullRelation(relation_name)
    