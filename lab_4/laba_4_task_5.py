from math import pi

def my_func(f,a=2,b=3,h=4,R=2):
  """
     1 - треугольник (введите a и h)
     2 - круг (введите R)
     3 - прямоугольник (введите a и b)
  """
  if f == 1:
      S = 1/2 * a * h
      print(S)

  elif f == 2:
      S = pi * R ** 2
      print(S)

  elif f == 3:
      S = a * b
      print(S)


my_func(3, a=4, b=5)
