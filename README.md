# Mandelbrot-Menge

Das Skript visualisiert die **Mandelbrot-Menge**, dabei wird eine **Folge von Punkten an der Mauposition** angezeigt. **Konvergiert** die Folge, so liegt der Punkt **innerhalb** der Mandelbrot-Menge; **divergiert** die Folge, so befindet sich der Punkt **außerhalb** der Menge. Während du die Maus bewegst, werden die berechneten Punkte in Echtzeit angepasst, sodass du die Mandelbrot-Menge interaktiv erkunden und verschiedene Bereiche der Menge untersuchen kannst.

# Definition
Für eine komplexe Zahl \( c \) ist der Punkt \( c \) in der Mandelbrot-Menge, wenn die Iteration der Funktion

\[
z_{n+1} = z_n^2 + c
\]

mit \( z_0 = 0 \) **nicht** divergiert, d.h., \( |z_n| \) bleibt für alle \( n \) endlich, wenn \( n \to \infty \). Andernfalls liegt der Punkt außerhalb der Mandelbrot-Menge, wenn die Folge divergiert.

Weitere Informationen auf [Wikipedia zur Mandelbrot-Menge](https://de.wikipedia.org/wiki/Mandelbrot-Menge).

![Beispiel Animation](./example.gif)
