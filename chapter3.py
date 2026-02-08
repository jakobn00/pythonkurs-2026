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
