class Wagon:
    MAX_PASSENGERS = 10

    def __init__(self, passengers=None, is_head_wagon=False):
        if passengers is None:
            passengers = []

        if not isinstance(passengers, list):
            raise TypeError("Passengers must be a list")

        if is_head_wagon and len(passengers) > 0:
            raise ValueError("Локомотив не може перевозити пасажирів")

        if not is_head_wagon and len(passengers) > self.MAX_PASSENGERS:
            raise ValueError("Звичайний вагон може перевозити не більше 10 пасажирів")

        self.passengers = passengers
        self.is_head_wagon = is_head_wagon


class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        if not isinstance(wagon, Wagon):
            raise TypeError("До поїзда можна додати тільки Wagon")

        if wagon.is_head_wagon:
            if len(self.wagons) > 0:
                raise ValueError("Локомотив може бути тільки першим вагоном")

            self.wagons.append(wagon)
            return

        if len(self.wagons) == 0:
            raise ValueError("Перший вагон має бути локомотивом")

        self.wagons.append(wagon)

    def total_passengers(self):
        total = 0

        for wagon in self.wagons:
            total += len(wagon.passengers)

        return total

train = Train()

locomotive = Wagon(is_head_wagon=True)
wagon_1 = Wagon(["Alex", "Ivan"])
wagon_2 = Wagon(["Oleg", "Anna", "Petro"])

train.add_wagon(locomotive)
train.add_wagon(wagon_1)
train.add_wagon(wagon_2)

print(train.total_passengers())


через трай ексепт пороахувати + провалідувати на помилки.

