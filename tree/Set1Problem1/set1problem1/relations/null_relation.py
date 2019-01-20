from .relation import Relation

class NullRelation(Relation):
    def __init__(self, relation_name):
        self._relation_name = relation_name

    def get_relatives(self):
        print('Unknown relation "%s".' % self._relation_name)
