import abc

class Relation(metaclass=abc.ABCMeta):
    """Relation Abstract Class"""

    @abc.abstractmethod
    def get_relatives(self, person_name, relation, family):
        pass
    
    def is_main_member(func):
        """Docorator to check if the person is the blood son/daughter i.e. the main member or not."""
        def _is_main_member(self, person_name, relation, family):
            if family.main_member.name != person_name:
                return "{0} does not have own {1}.".format(person_name, relation.lower())
            else:
                # calling the function
                return func(self, person_name, relation, family)
        return _is_main_member