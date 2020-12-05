def my_func(a):
  s = 1
  for i in range(len(a)):
    b = s * a[i]
    s = b
    print(b)
my_func([2,3,4,5])
