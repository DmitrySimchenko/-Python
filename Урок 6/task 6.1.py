"""1.	Создать класс TrafficLight (светофор).

●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
 третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.

"""

from itertools import cycle
from time import sleep


class TrafficLight:
    colors_queue = ('красный', 'желтый', 'зеленый')
    time = (7, 2, 10)
    message = ("Красный свет - проезда нет!", "Желтый - будь готов к пути", "А зеленый свет - кати!")

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.colors_queue)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.colors_queue.index(self.__color)])
                sleep(self.time[self.colors_queue.index(self.__color)])
                self.__color = next(my_cycle)


my_traffic = TrafficLight("желтый")
my_traffic.running()
