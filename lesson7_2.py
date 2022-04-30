from abc import ABC, abstractmethod
class Clothes(ABC):
  def __init__(self, name):
    self.name = name
  @abstractmethod
  def material(self):
    print("Мне тут считать нечего...")
    return 0
class Coat(Clothes):
  def __init__(self, v):
    self.__v = v
  @property
  def v(self):
    return self.__v
  @v.setter
  def v(self, new_v):
    if str(new_v).isdigit():
      self.__v = new_v
    else:
      print("Размер должен быть целым цифрой!")
  @property
  def material(self):
    return self.__v / 6.5 + 0.5
class Suit(Clothes):
  def __init__(self, h):
    self.__h = h
  @property
  def h(self):
    return self.__h
  @h.setter
  def h(self, new_h):
    if str(new_h).isdigit():
      self.__h = new_h
    else:
      print("Размер должен быть целым цифрой!")
  @property
  def material(self):
    return self.__h * 2 + 0.3

coat = Coat(52)
suit = Suit(180)
coat_m = [round(coat.material, 2)]
suit_m = [round(suit.material, 2)]
print(f"Для пошива пальто {coat.v} размера понадобится {round(coat.material, 2)} материала.")
while True:
  v_coat = input("Введите размер следующего пальто, или напишите 'n' для перехода к расчету материала на пальто: ")
  if v_coat == "n":
    print(f"На пошив пальто Вам понадобится всего {round(sum(coat_m), 2)} материала")
    break
  else:
    coat.v = v_coat
    coat.v = int(coat.v)
    print(f"Для пошива пальто {coat.v} размера понадобится {round(coat.material, 2)} материала.")
    coat_m.append(round(coat.material,2))
print(f"\nДля пошива костюма {suit.h} размера понадобится {round(suit.material, 2)} материала.")
while True:
  h_suit = input("Введите размер следующего костюма, или напишите 'q' завершения расчета материала: ")
  if h_suit == "q":
    print(f"На пошив костюмов Вам понадобится всего {round(sum(suit_m), 2)} материала")
    break
  else:
    suit.h = h_suit
    suit.h = int(suit.h)
    print(f"Для пошива костюма {suit.h} размера понадобится {round(suit.material, 2)} материала.")
    suit_m.append(round(suit.material,2))

