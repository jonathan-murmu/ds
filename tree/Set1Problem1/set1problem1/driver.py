from collections import deque

from .constants import (
    PATERNAL_UNCLE,
    MATERNAL_UNCLE,
    PATERNAL_AUNT,
    MATERNAL_AUNT,
    SISTER_IN_LAW,
    BROTHER_IN_LAW,
    COUSINS,
    FATHER,
    MOTHER,
    CHILDREN,
    SONS,
    DAUGHTERS,
    BROTHERS,
    SISTERS,
    GRAND_DAUGHTER
)
from .demo_data import DemoData
from .person import Person


class Choice(object):
    """Command Invoker"""
    def __init__(self):
        self._history = deque()

    @property
    def history(self):
        return self._history

    def execute(self, command):
        self._history.appendleft(command)
        return command.execute()

class Command(object):
    """The Command interface"""
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError

class CreateGenerationCommand(Command):
    """Command to create King Shan and Queen Anga Generation Tree."""
    def execute(self):
        return self._obj.create_generation()

class FindRelationCommand(Command):
    """Command to find the relative of the give person."""
    def execute(self):
        return self._obj.find_relation()

class ExitCommand(Command):
    """Command to exit the program."""
    def execute(self):
        return self._obj.exit()

class Generation(object):
    """The reciever to execute the commands."""
    def __init__(self):
      self.relation = {
            "1": PATERNAL_UNCLE,
            "2": MATERNAL_UNCLE,
            "3": PATERNAL_AUNT,
            "4": MATERNAL_AUNT,
            "5": SISTER_IN_LAW,
            "6": BROTHER_IN_LAW,
            "7": COUSINS,
            "8": FATHER,
            "9": MOTHER,
            "10": CHILDREN,
            "11": SONS,
            "12": DAUGHTERS,
            "13": BROTHERS,
            "14": SISTERS,
            "15": GRAND_DAUGHTER
          }

    def create_generation(self):
        self.demo = DemoData()
        print("King Shan and Queen Anga's generation created.")
        return True

    def find_relation(self):
        print("Enter the person name")
        person_name = input()
        print("Enter Relation")
        for k,v in self.relation.items():
          print("{0}. {1}".format(k,v))
        try:
          relation = self.relation[input()]
        except:
          print("Wrong choice of relation! Please try again.")
          return True
        print(self.demo.relationship(person_name=person_name.title(), relation=relation))
        print("Relation Found")
        return True
    
    def exit(self):
      print('Thank You!')
      return False

class Driver(object):
    """The Driver client to execute the Program."""
    def __init__(self):
        self._generation = Generation()
        self._choice = Choice()

    @property
    def choice(self):
        return self._choice

    def show_main_menu(self):
      print("="*50)
      print("1. Create King Shan and Queen Anga's Generation.")
      print("2. Find Relation.")
      print("X. Exit")
      print("="*50)
      
    def press(self, cmd):
        cmd = cmd.strip().upper()

        if cmd == "1":
          return self._choice.execute(CreateGenerationCommand(self._generation))
        elif cmd == "2":
          return self._choice.execute(FindRelationCommand(self._generation))
        elif cmd == "X":
          return self._choice.execute(ExitCommand(self._generation))
        else:
            print("Wrong Choice!")
        return True

def main():
    driver = Driver()
    status = True
    while(status):
        driver.show_main_menu()
        cmd = input()
        status = driver.press(cmd)

if __name__ == '__main__':
    main()

