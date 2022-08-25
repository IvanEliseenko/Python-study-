class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name}, {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


seller = Position("John", "Johnson", "Seller", 1000, 300)
print(seller.get_full_name())
print(seller.get_total_income())