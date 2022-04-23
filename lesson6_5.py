class Stationery:
  def __init__(self, color, thickness):
    self.color = color
    self.thickness = thickness
  def draw(self):
    print(f"Выбранный цвет: {self.color}\nТолщина линии: {self.thickness}\nЗапуск отрисовки...")
class Pen(Stationery):
  # def __init__(self, color, thickness, mech, colour):
  def draw(self, type):
    pen_types = {"gel": "гелевая", "ball": "шариковая", "fountain": "перьевая", "capillary": "капиллярная"}
    self.type = pen_types.get(type)
    print(f"Инструмент: ручка.\nТип ручки: {self.type}\nТолщина стержня: {self.thickness}\nЦвет: {self.color}\nЗапуск написания эссе...")
class Pencil(Stationery):
  def draw(self, mat):
    self.material = mat
    print(f"Инструмент: карандаш.\nМатериал карандаша: {self.material}\nТолщина стержня: {self.thickness}\nЦвет: {self.color}\nЗапуск черчения...")

i_other = Stationery("Зеленый", 2)
i_other.draw()

i_pen = Pen("Синий", 0.5)
i_pen.draw("gel")

i_pencil = Pencil("Черный", 0.2)
i_pencil.draw("Деревянный")