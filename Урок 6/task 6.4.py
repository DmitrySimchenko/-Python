"""4.	Реализуйте базовый класс Car.

●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Атомобиль марки {self.name}, {self.color} цвет, поехал со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'Атомобиль марки {self.name}, {self.color} цвет остановился')

    def turn(self, side):
        print(f'Атомобиль марки {self.name}, {self.color} цвет повернул на {side}')

    def show_speed(self):
        print(f'Текущая скорость атомобиля марки {self.name}, {self.color} цвет составляет {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль марки {self.name}, {self.color} цвет превышает скорость на {self.speed - 60} км/ч')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль марки {self.name}, {self.color} цвет превышает скорость на {self.speed - 40} км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


my_town_car = TownCar(70, 'красный', 'reno Logan', False)
my_town_car.go()
my_town_car.stop()
my_town_car.turn("право")
my_town_car.show_speed()

my_work_car = WorkCar(45, 'оранжевый', 'МАЗ', False)
my_work_car.go()
my_work_car.stop()
my_work_car.turn("право")
my_work_car.show_speed()

my_police_car = PoliceCar(90, 'белый', 'ford Mondeo')
my_police_car.go()
my_police_car.stop()
my_police_car.turn("лево")
my_police_car.show_speed()
