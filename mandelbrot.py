import matplotlib.pyplot as plt
import numpy as np

# Dimension des Bildes
width, height = 800, 800
re_min, re_max = -2.5, 1.5
im_min, im_max = -2.0, 2.0
max_iter = 50

# Berechnung der Mandelbrot-Menge
def mandelbrot(c, max_iter=100):
    z = 0
    for n in range(max_iter):
        z = z ** 2 + c
        if abs(z) > 2:  # Punkt divergiert
            return n
    return max_iter

# Erstellung des Bildes
def generate_mandelbrot_image(width, height, re_min, re_max, im_min, im_max, max_iter=100):
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(real[j], imag[i])
            image[i, j] = mandelbrot(c, max_iter)

    return image

mandelbrot_image = generate_mandelbrot_image(width, height, re_min, re_max, im_min, im_max, max_iter)

fig, ax = plt.subplots(figsize=(10, 10))
cmap = 'twilight'
# Andere modi: viridis, plasma, inferno, magma (good at weak contrast), twilight (cyclic)

# Plot Mandelbrot-Menge
ax.imshow(mandelbrot_image, cmap=cmap, extent=(re_min, re_max, im_min, im_max))
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title('Mandelbrot-Menge')

# Anzeige der Mausposition (als Punkt)
point, = ax.plot([], [], 'o', markersize=5, color='purple')
# Andere Farben hier setzen


# Punktpositionsberechnung
def mandelbrot_iterations(c, max_iter=8):
    z = 0
    iterations = [z]
    for n in range(max_iter):
        z = z ** 2 + c
        iterations.append(z)
        if abs(z) > 2:  # Punkt divergiert
            break
    return iterations

# Mausbewegung handhaben
def on_move(event):
    if event.inaxes:
        # Mausposition als Komplexe-Zahl
        real = event.xdata
        imag = event.ydata
        cnum_at_mouse = complex(real, imag)

        iterations = mandelbrot_iterations(cnum_at_mouse, max_iter=8)

        points = np.array([(z.real, z.imag) for z in iterations])
        point.set_data(points[1:, 0], points[1:, 1])  # 0ten Eintrag überspringen

        fig.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
