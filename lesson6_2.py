class Road:

  def __init__(self, l, w, m, h):
    self._length = l
    self._width = w
    self.min_weight = m
    self.height = h

  def weight(self):
    all_weight = self._length * self._width * self.min_weight * self.height
    return all_weight / 1000

a = Road(5000, 20, 25, 5)
print(f"Масса асфальта для покрытия дороги шириной {a._width} м, длинной {a._length} м, толщиной {a.height} см равна {int(a.weight())} т")
