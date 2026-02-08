# %% 3.1.1
import numpy as np

a, b, N = 12, 18, 200
points = np.linspace(a, b, N)

even_idx = np.arange(start=0, stop=N, step=2)
even_sum = np.sum(points[even_idx])
print(f"{even_sum=:.2f}")

odd_idx = np.arange(start=1, stop=N + 1, step=2)
odd_sum = np.sum(points[odd_idx])
print(f"{odd_sum=:.2f}")

div_by_10_idx = np.arange(start=0, stop=N, step=10)
div_by_10_sum = np.sum(points[div_by_10_idx])
print(f"{div_by_10_sum=:.2f}")

special_idx = np.array([2, 5, 19, 92])
special_sum = np.sum(points[special_idx])
print(f"{special_sum=:.2f}")

# %% 3.2.1

size = 4
A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((2 * size, 2 * size))
C[0:size, 0:size] = A
C[size : 2 * size, size : 2 * size] = A
C[size : 2 * size, 0:size] = B
C[0:size, size : 2 * size] = B

print(C)

# %% 3.3.1
import matplotlib.pyplot as plt

radius = 1
x_margin = radius / 3
linewidth = 8

# Upper rings
blue = plt.Circle(
    (-2 * radius - x_margin, 0), radius, color="blue", fill=False, linewidth=linewidth
)
plt.gca().add_patch(blue)
black = plt.Circle((0, 0), radius, color="black", fill=False, linewidth=linewidth)
plt.gca().add_patch(black)
red = plt.Circle(
    (2 * radius + x_margin, 0), radius, color="red", fill=False, linewidth=linewidth
)
plt.gca().add_patch(red)

# Lower rings
yellow = plt.Circle(
    (-radius - x_margin / 2, -radius),
    radius,
    color="#FFCD00",
    fill=False,
    linewidth=linewidth,
)
plt.gca().add_patch(yellow)

green = plt.Circle(
    (+radius + x_margin / 2, -radius),
    radius,
    color="green",
    fill=False,
    linewidth=linewidth,
)
plt.gca().add_patch(green)

plt.xlim(-4 * radius, 4 * radius)
plt.ylim(-4 * radius, 2 * radius)

# %% 3.4.2

def trapezoidal_integrate(f, interval, N):
    a, b = interval
    h = (b - a) / N  # step length
    integral = 0
    for k in range(N):
        integral += 1 / 2 * (f(k * h) + f((k + 1) * h)) * h
    return integral

f = lambda x: x**2
interval = (0, 1)
N = 1000

integral = trapezoidal_integrate(f, interval, N)
print(integral)
