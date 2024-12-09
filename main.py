# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"

class House:
    # Атрибут класса для хранения истории домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Создаем новый объект
        instance = super().__new__(cls)

        # Добавляем название дома в историю
        if args:
            cls.houses_history.append(args[0])  # Добавляем первое аргумент (название дома) в историю

        return instance

    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли указанный этаж
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Вывод этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращает количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращает строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise ValueError("Value must be an integer")

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        # Сообщаем, что объект снесён
        print(f"{self.name} снесён, но он останется в истории")


# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
del h1




