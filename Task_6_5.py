class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Draw initialization")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title} draw")


class Pencil(Stationary):
    def draw(self):
        print(f"{self.title} draw")


class Handle(Stationary):
    def draw(self):
        print(f"{self.title} draw")


pen = Pen("Pen")
pencil = Pencil("Pencil")
handle = Handle("Handle")

list = [pen, pencil, handle]

for i in list:
    i.draw()
