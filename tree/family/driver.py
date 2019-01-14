from constants import FEMALE, MALE
from demo_data import DemoData
from person import Person


class Driver(object):
  def __init__(self):
    self.relation = {
      "1": "Paternal uncle",
      "2": "Maternal uncle",
      "3": "Paternal aunt",
      "4": "Maternal aunt",
      "5": "Sister-in law",
      "6": "Brother-in law",
      "7": "Cousins",
      "8": "Father",
      "9": "Mother",
      "10": "Children",
      "11": "Sons",
      "12": "Daughters",
      "13": "Brothers",
      "14": "Sisters",
      "15": "Grand daughter"
    }

  def double_line(self):
    print("="*50)
  def single_line(self):
    print("-"*50)
  def show_main_menu(self):
    print("1. Create King Shan and Queen Anga's Generation.")
    print("2. Find Relation.")
    print("x. Exit")

  def create_generation(self):
    self.demo = DemoData()
    self.single_line()
    print('Shan Family Generation Created!')
  
  def find_relation(self):
    self.double_line()
    print("Enter the person name")
    person_name = input()
    print("Choose the relation:")
    self.single_line()
    for k,v in self.relation.items():
      print("{0}. {1}".format(k,v))
    self.single_line()
    try:
      relation = self.relation[input()]
    except:
      print("Wrong choice of relation!")
      self.double_line()
      return

    self.single_line()
    print(self.demo.relationship(person_name=person_name.title(), relation=relation))
    
  def run(self):
    while True:
      self.double_line()
      print("Enter Your Choice")
      self.double_line()
      self.show_main_menu()
      self.double_line()
      choice = input()
      if choice == 'x':
        break
      elif choice == '1':
        self.create_generation()
      elif choice == '2':
        self.find_relation()
      else:
        print('Wrong choice')
        self.double_line()
  

if __name__ == '__main__':
  driver = Driver()
  driver.run()
