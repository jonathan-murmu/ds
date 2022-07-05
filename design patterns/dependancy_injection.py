from abc import ABC


# absctra class
class Tyre(ABC):
    def build_wheels(self):  # abstact method
        pass



class MRF(Tyre):
    def build_wheels(self):
        return 'wheels built'


class Apollo(Tyre):
    def build_wheels(self):
        return 'appolo wheels built'

class Micheline(Tyre):
    def build_wheels(self):
        return 'micheline wheels built'

class Hyndai:
    parts = []
    def __init__(self, tyre):
        self.tyre = tyre

    def build_body(self):
        self.parts.append('body')
        print('body built')

    def build_engine(self):
        self.parts.append('engine')
        print('engine built')

    def put_wheels(self):
        # wheels = MRF()  # create object
        # wheels = Apollo()
        # wheels = Micheline()

        wheels = self.tyre
        self.parts.append(wheels.build_wheels())





class CarFactory:

    def start_building_car(self):
        hyd_car = Hyndai(Micheline())
        # hyd_car = Hyndai()
        hyd_car.build_body()

        hyd_car.build_engine()
        hyd_car.put_wheels()
        print(hyd_car.parts)


if __name__ == '__main__':
    obj = CarFactory()
    obj.start_building_car()