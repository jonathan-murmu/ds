import unittest

from constants import FEMALE, MALE
from demo_data import DemoData
from family import Family
from generation import Generation
from person import Person


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

# Run Tests
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGeneration('test_relationship'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
