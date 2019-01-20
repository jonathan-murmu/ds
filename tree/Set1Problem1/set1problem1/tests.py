import unittest

from .constants import FEMALE, MALE
from .demo_data import DemoData
from .family import Family
from .generation import Generation
from .person import Person
from .family import PERSON_ADDRESS
from .relationfactory import RelationFactory
from . import relations


class TestGeneration(unittest.TestCase):
    def setUp(self):
      self.demo = DemoData()

    def test_relationship(self):
      self.assertEqual(
        self.demo.relationship(person_name='Ish', relation='Brothers'), ['Chit', 'Vich'],
        'Incorrect Brothers implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Chit', relation='Mother'), 'Anga',
        'Incorrect Mother implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Vich', relation='Father'), 'Shan',
        'Incorrect Father implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Shan', relation='Sons'), ['Ish', 'Chit', 'Vich'],
        'Incorrect Sons implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Ish', relation='Sisters'), ['Satya'],
        'Incorrect Sisters implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Shan', relation='Daughters'), ['Satya'],
        'Incorrect Daughters implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Shan', relation='Children'), ['Ish', 'Chit', 'Vich', 'Satya'],
        'Incorrect Children implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Ambi', relation='Brothers'), 'Ambi does not have own brothers.',
        'Incorrect Brothers implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Ambi', relation='Brother-in law'), ['Ish', 'Vich'],
        'Incorrect Brother-in law implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Jnki', relation='Sister-in law'), ['Chika'],
        'Incorrect Sister-in law implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Satvy', relation='Maternal aunt'), ['Ambi', 'Lika'],
        'Incorrect Maternal aunt implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Drita', relation='Maternal aunt'), 'Drita does not have own maternal aunt.',
        'Incorrect Maternal aunt implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Satvy', relation='Maternal uncle'), ['Ish', 'Chit', 'Vich'],
        'Incorrect Maternal uncle implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Drita', relation='Maternal uncle'), 'Drita does not have own maternal uncle.',
        'Incorrect Maternal uncle implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Satvy', relation='Paternal aunt'), 'Satvy does not have own paternal aunt.',
        'Incorrect Paternal aunt implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Drita', relation='Paternal aunt'), ['Lika', 'Satya'],
        'Incorrect Paternal aunt implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Satvy', relation='Paternal uncle'), 'Satvy does not have own paternal uncle.',
        'Incorrect Paternal uncle implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Drita', relation='Paternal uncle'), ['Ish', 'Vich', 'Vyan'],
        'Incorrect Paternal uncle implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Shan', relation='Grand daughter'), ['Chika', 'Satvy'],
        'Incorrect Paternal uncle implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Satvy', relation='Cousins'), ['Drita', 'Vrita', 'Vila', 'Chika', 'Savya', 'Saayan'],
        'Incorrect Cousin implementation')
      self.assertEqual(
        self.demo.relationship(person_name='Ish', relation='Cousins'), "Ish does not have own cousins.",
        'Incorrect Cousin implementation')


class TestFamily(unittest.TestCase):
    def setUp(self):
        # PERSON_ADDRESS = {}
        self.person_name = 'Test Person 1'
        self.test_person_1 = Person(name=self.person_name, gender=MALE)
        self.test_family = Family(main_member=self.test_person_1)
    
    def test_update_address(self):
        self.assertEqual(
            self.person_name in PERSON_ADDRESS, True,
            'Incorrect Update Address implementation')
        self.assertEqual(
            "Test Person 2" in PERSON_ADDRESS, False,
            'Incorrect Update Address implementation')


class TestPerson(unittest.TestCase):
    def test_person_class(self):
        self.person_name = "Test Person"
        self.gender = MALE
        self.person_obj = Person(name=self.person_name, gender=self.gender)
        self.assertEqual(
            type(self.person_obj), Person,
            'Incorrect Person class  implementation')


class TestRelationFactory(unittest.TestCase):
    def setUp(self):
        self.relation_factory = RelationFactory()
        self.class_instances = {
            'BrotherInLaw': relations.BrotherInLaw,
            'Brothers': relations.Brothers,
            'Children': relations.Children,
            'Cousins': relations.Cousins,
            'Daughters': relations.Daughters,
            'Father': relations.Father,
            'GrandDaughter': relations.GrandDaughter, 
            'MaternalAunt': relations.MaternalAunt,
            'MaternalUncle': relations.MaternalUncle,
            'Mother': relations.Mother,
            'PaternalAunt': relations.PaternalAunt,
            'PaternalUncle': relations.PaternalUncle,
            'SisterInLaw': relations.SisterInLaw,
            'Sisters': relations.Sisters,
            'Sons': relations.Sons,
        }

    def test_load_relations(self):
        for cls_name, cls_type in self.class_instances.items():
            self.assertEqual(
                self.relation_factory.relation[cls_name], cls_type,
                'Incorrect load_relation() {0} implementation'.format(cls_name))


    def test_create_instance(self):

        wrong_class = "WrongClass"
        for cls_name, cls_type in self.class_instances.items():
            self.assertEqual(
                type(self.relation_factory.create_instance(cls_name)) == cls_type, True,
                'Incorrect load_relation() MaternalUncle implementation')
        self.assertEqual(
            type(self.relation_factory.create_instance(wrong_class)) == relations.NullRelation, True,
            'Incorrect load_relation() MaternalUncle implementation')



# # Run Tests
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestGeneration('test_relationship'))

#     return suite


# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
