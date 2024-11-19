print("print something")
a, b = 0, 1
while a < 10:
    print(a, end='x')
    a, b = b, a + b
