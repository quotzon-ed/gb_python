class Cell:
  def __init__(self, value):
    self.value = value
  def __add__(self, other):
    return f"При сложении двух клеток получилась клетка, состоящая из {self.value + other.value} ячеек."
  def __sub__(self, other):
    cell_sub = self.value - other.value
    if cell_sub > 0:
      return f"Разность двух клеток дала клетку, состоящую из {cell_sub} ячеек."
    elif cell_sub == 0:
      return f"Клетки уничтожили друг друга"
    else:
      return f"Данное действие невозможно, так как дает отрицательный результат."
  def __mul__(self, other):
    return f"При произведении двух клеток получилась клетка, состоящая из {self.value * other.value} ячеек."
  def __truediv__(self, other):
    if other.value != 0 and self.value / other.value >= 1:
      return f"При делении двух клеток получилась клетка, состоящая из {int(self.value / other.value)} ячеек."
    elif other.value != 0 and self.value / other.value < 1:
      return f"Количество ячеек в клетке меньше 1, такая операция невозможна"
    else:
      return f"Делить на 0 нельзя!"
  def make_order(self, row):
    for r in range(row - 1):
      for c in range(self.value // row):
        print("💥", end=" ")
      print("")
    if self.value % row != 0:
      for last in range(self.value % row):
        print("💥", end=" ")
      print("")

cell_1 = Cell(20)
cell_2 = Cell(10)
print(f'{cell_1 + cell_2}\n{cell_1 - cell_2}\n{cell_1 * cell_2}\n{cell_1 / cell_2}')
cell_1.make_order(5)