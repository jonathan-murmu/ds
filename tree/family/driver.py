from constants import FEMALE, MALE
from person import Person


class Driver(object):
  def double_line(self):
    print("="*50)

  def create_person(self):
    self.double_line()
    print("Enter Name")
    name = input()
    print("Enter Gender(m/f)")
    gender = MALE if input() == MALE else FEMALE
    person = Person(name=name, gender=gender)
    print("Person - {0} Created!".format(name))
    self.double_line()
    return person
    
  def run(self):
    while True:
      self.double_line()
      print("Enter Your Choice")
      self.double_line()
      print("1. Create Person")
      print("x. Exit")
      self.double_line()
      choice = input()
      if choice == 'x':
        break
      elif choice == '1':
        self.create_person()
      else:
        print('Wrong choice')
        self.double_line()


if __name__ == '__main__':
  driver = Driver()
  driver.run()