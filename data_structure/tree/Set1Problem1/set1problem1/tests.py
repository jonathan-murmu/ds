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


class TestRelation(unittest.TestCase):
    """Test all the classes in the relation package."""
    def setUp(self):
        self.demo = DemoData()
    
    def test_aunt(self):
        aunt = relations.aunt.Aunt()
        self.assertEqual(
            aunt.get_aunt('Satvy', "Maternal aunt", self.demo.satvy_family, FEMALE),
            ['Ambi', 'Lika'],
            'Incorrect Aunt implementation')
        self.assertEqual(
            aunt.get_aunt('Drita', "Maternal aunt", self.demo.drita_family, FEMALE),
            "Drita does not have own maternal aunt.",
            'Incorrect Aunt implementation')
    def test_brother_in_law(self):
        brother_in_law = relations.BrotherInLaw()
        self.assertEqual(
            brother_in_law.get_relatives('Ambi', "Brother-in law", self.demo.chit_family),
            ['Ish', 'Vich'],
            'Incorrect Brother in law implementation')
    
    def test_brothers(self):
        brothers = relations.Brothers()
        self.assertEqual(
            brothers.get_relatives('Ambi', "Brothers", self.demo.chit_family),
            'Ambi does not have own brothers.',
            'Incorrect Brothers implementation')
    def test_children(self):
        children = relations.Children()
        self.assertEqual(
            children.get_relatives('Shan', "Children", self.demo.shan_family),
            ['Ish', 'Chit', 'Vich', 'Satya'],
            'Incorrect Children implementation')
    
    def test_cousins(self):
        obj = relations.Cousins()
        self.assertEqual(
            obj.get_relatives('Satvy', "Cousins", self.demo.satvy_family),
            ['Drita', 'Vrita', 'Vila', 'Chika', 'Savya', 'Saayan'],
            'Incorrect Cousin implementation')
    
    def test_daughters(self):
        obj = relations.Daughters()
        self.assertEqual(
            obj.get_relatives('Shan', "Daughters", self.demo.shan_family),
            ['Satya'],
            'Incorrect Daughters implementation')
    
    def test_father(self):
        obj = relations.Father()
        self.assertEqual(
            obj.get_relatives('Vich', "Father", self.demo.vich_family),
            'Shan',
            'Incorrect Father implementation')
        self.assertEqual(
            obj.get_relatives('Shan', "Father", self.demo.shan_family),
            'Shan does not have own father.',
            'Incorrect Father implementation')
    
    def test_grand_daughters(self):
        obj = relations.GrandDaughter()
        self.assertEqual(
            obj.get_relatives('Shan', "Grand daughters", self.demo.shan_family),
            ['Chika', 'Satvy'],
            'Incorrect Grand Daughter implementation')
    
    def test_maternal_aunt(self):
        obj = relations.MaternalAunt()
        self.assertEqual(
            obj.get_relatives('Drita', "Maternal aunt", self.demo.drita_family),
            'Drita does not have own maternal aunt.',
            'Incorrect MaternalAunt implementation')
    
    def test_mother(self):
        obj = relations.Mother()
        self.assertEqual(
            obj.get_relatives('Drita', "Mother", self.demo.drita_family),
            "Ambi",
            'Incorrect Mother implementation')
    
    def test_paternal_aunt(self):
        obj = relations.PaternalAunt()
        self.assertEqual(
            obj.get_relatives('Drita', "Paternal aunt", self.demo.drita_family),
            ['Lika', 'Satya'],
            'Incorrect Paternal aunt implementation')
    
    def test_sisters(self):
        obj = relations.Sisters()
        self.assertEqual(
            obj.get_relatives('Ish', "Sisters", self.demo.ish_family),
            ['Satya'],
            'Incorrect Sisters implementation')
    
    def test_sons(self):
        obj = relations.Sons()
        self.assertEqual(
            obj.get_relatives('Shan', "Sons", self.demo.shan_family),
            ['Ish', 'Chit', 'Vich'],
            'Incorrect Sons implementation')
