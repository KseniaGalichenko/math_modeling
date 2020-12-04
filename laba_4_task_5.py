from math import pi

print('Введите фигуру')
x = str(input())

if 'треугольник':
  def my_func1(a,h):
    S = 1/2 * a * h
    print(S)
  my_func1(3,4)

elif 'круг':
  def my_func2(R):
    S = pi * R ** 2
    print(S)
  my_func2(4)

elif 'прямоугольник':
  def my_func3(a,b):
    S = a * b
    print(S)
  my_func3(3,6)
