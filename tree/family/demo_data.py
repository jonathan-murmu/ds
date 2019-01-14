from constants import FEMALE, MALE
from family import Family
from generation import Generation
from person import Person

class DemoData(object):
  def __init__(self):
    self.shan = Person(name='Shan', gender=MALE)
    self.anga = Person(name='Anga', gender=FEMALE)

    self.ish = Person(name='Ish', gender=MALE)
    self.chit = Person(name='Chit', gender=MALE)
    self.ambi = Person(name='Ambi', gender=FEMALE)
    self.vich = Person(name='Vich', gender=MALE)
    self.lika = Person(name='Lika', gender=FEMALE)
    self.satya = Person(name='Satya', gender=FEMALE)
    self.vyan = Person(name='Vyan', gender=MALE)

    self.drita = Person(name='Drita', gender=MALE)
    self.jaya = Person(name='Jaya', gender=FEMALE)
    self.vrita = Person(name='Vrita', gender=MALE)

    self.vila = Person(name='Vila', gender=MALE)
    self.jnki = Person(name='Jnki', gender=FEMALE)
    self.chika = Person(name='Chika', gender=FEMALE)
    self.kpila = Person(name='Kpila', gender=MALE)

    self.satvy = Person(name='Satvy', gender=FEMALE)
    self.aswa = Person(name='Aswa', gender=MALE)
    self.savya = Person(name='Savya', gender=MALE)
    self.kripi = Person(name='Kripi', gender=FEMALE)
    self.saayan = Person(name='Saayan', gender=MALE)
    self.mina = Person(name='Mina', gender=FEMALE)

    self.jta = Person(name='jta', gender=MALE)
    self.driya = Person(name='Driya', gender=FEMALE)
    self.mnu = Person(name='Mnu', gender=MALE)

    self.lavnya = Person(name='Lavnya', gender=FEMALE)
    self.gru = Person(name='Gru', gender=MALE)

    self.kriya = Person(name='Kriya', gender=MALE)

    self.misa = Person(name='Misa', gender=MALE)
    
    self.shan_family = Family(main_member=self.shan, spouse=self.anga)

    self.ish_family = Family(main_member=self.ish)
    self.chit_family = Family(main_member=self.chit, spouse=self.ambi)
    self.vich_family = Family(main_member=self.vich, spouse=self.lika)
    self.satya_family = Family(main_member=self.satya, spouse=self.vyan)

    self.drita_family = Family(main_member=self.drita, spouse=self.jaya)
    self.vrita_family =Family(main_member=self.vrita)

    self.vila_family = Family(main_member=self.vila, spouse=self.jnki)
    self.chika_family = Family(main_member=self.chika, spouse=self.kpila)

    self.satvy_family = Family(main_member=self.satvy, spouse=self.aswa)
    self.savya_family = Family(main_member=self.savya, spouse=self.kripi)
    self.saayan_family = Family(main_member=self.saayan, spouse=self.mina)

    self.jta_family = Family(main_member=self.jta)
    self.driya_family = Family(main_member=self.driya, spouse=self.mnu)

    self.lavnya_family = Family(main_member=self.lavnya, spouse=self.gru)

    self.kriya_family = Family(main_member=self.kriya)

    self.misa_family = Family(main_member=self.misa)

    self.g = Generation()
    self.g.add_child_family(child_family=self.shan_family)
    self.g.add_child_family(parent_name='Shan', child_family=self.ish_family)
    self.g.add_child_family(parent_name='Shan', child_family=self.chit_family)
    self.g.add_child_family(parent_name='Shan', child_family=self.vich_family)
    self.g.add_child_family(parent_name='Shan', child_family=self.satya_family)

    self.g.add_child_family(parent_name='Chit', child_family=self.drita_family)
    self.g.add_child_family(parent_name='Chit', child_family=self.vrita_family)

    self.g.add_child_family(parent_name='Vich', child_family=self.vila_family)
    self.g.add_child_family(parent_name='Vich', child_family=self.chika_family)

    self.g.add_child_family(parent_name='Satya', child_family=self.satvy_family)
    self.g.add_child_family(parent_name='Satya', child_family=self.savya_family)
    self.g.add_child_family(parent_name='Satya', child_family=self.saayan_family)

    self.g.add_child_family(parent_name='Drita', child_family=self.jta_family)
    self.g.add_child_family(parent_name='Drita', child_family=self.driya_family)

    self.g.add_child_family(parent_name='Vila', child_family=self.lavnya_family)

    self.g.add_child_family(parent_name='Savya', child_family=self.kriya_family)

    self.g.add_child_family(parent_name='Saayan', child_family=self.misa_family)
  
  def relationship(self, person_name=None, relation=None):
    return self.g.relationship(person_name=person_name, relation=relation)
