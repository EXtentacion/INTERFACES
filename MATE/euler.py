def f(x, y):
    return 0.1 * (y ** 0.5) + 4 * x ** 2

def euler_method(x0, y0, h, target_x):
    x = x0
    y = y0

    while x < target_x:
        y += h * f(x, y)
        x += h

    return y

# Valores iniciales
x0 = 2
y0 = 4

# Primer caso con h = 0.1
h1 = 0.1
target_x1 = 2.1
approximation1 = euler_method(x0, y0, h1, target_x1)
print(f"Aproximación con h = 0.1: {approximation1}")




