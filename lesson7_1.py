# Небольшое пояснение к решению задачи. К сожалению я не нашел никакой информации по сложению разноразмерных матриц. Поэтому предположил, что, если матрицы разноразмерные, то недостающие столбцы/строки можно заменить нулями, а затем складывать стандартным алгоритмом сложения матриц
from random import randint
class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix

  def __str__(self):
    string_rows = [] # В этот список будем записывать строки, чтобы красиво выводить матрицу в консоли
    for rows in self.matrix:
      for cells in range(len(rows)): # Этот цикл отвечает за расставление отступов между элементами матрицы (чтобы было красиво и элементы в столбцах находились друг под другом)
        if int(rows[cells]) < 10:
          rows[cells] = str(rows[cells]) + "  "
        elif int(rows[cells]) >= 100:
          rows[cells] = str(rows[cells])
        else:
          rows[cells] = str(rows[cells]) + " "
      string_rows.append("   ".join(rows))
    return "\n".join(string_rows) # Выводим полученные строки на экран, закрывая каждую строку переходом на новую

  def __add__(self, other):
    new_row = []
    sum_matrix = []
    if len(self.matrix) < len(other.matrix): # Сверяем количество строк в матрицах. Если в одной из матриц их меньше, заменяем строки нулями
      for cells in range(len(self.matrix)):
        new_row.append(0)
      self.matrix.append(new_row)
    elif len(self.matrix) > len(other.matrix):
      for cells in range(len(other.matrix)):
        new_row.append(0)
      other.matrix.append(new_row)
    new_row.clear()
    for row in range(len(self.matrix)):
      sum_row = []
      while len(self.matrix[row]) != len(other.matrix[row]): # Сравниваем количество столбцов в матрицах. Если в одной из матриц их меньше, заменяем нулями
        if len(self.matrix[row]) < len(other.matrix[row]):
          self.matrix[row].append(0)
        elif len(self.matrix[row]) > len(other.matrix[row]):
          other.matrix[row].append(0)
      for cell in range(len(self.matrix[row])): # Перебираем и складываем попарно элементы матрицы, записываем в итоговую матрицу, возвращаем ее
        sum_row.append(int(self.matrix[row][cell]) + int(other.matrix[row][cell]))
      sum_matrix.append(sum_row)
    return Matrix(sum_matrix)
          
      

def new_mat(cells, rows): # Небольшая функция, которая генерирует матрицу из заданного количества столбцов и строк
  new_mat = []
  for r in range(rows):
    mat_cells = []
    for c in range(cells):
      el = randint(0, 100)
      mat_cells.append(el)
    new_mat.append(mat_cells)
  return new_mat
matrix_1 = Matrix(new_mat(3,4))
matrix_2 = Matrix(new_mat(2,3))
matrix_3 = Matrix(new_mat(4,5))
print(matrix_1, end="\n\n")
print(matrix_2, end="\n\n")
print(matrix_3, end="\n\n")
print("-" * 20 + "\n")
print(matrix_1 + matrix_2 + matrix_3)