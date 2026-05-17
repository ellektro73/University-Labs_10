import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 10, 500)  # починаємо з 0.01, щоб уникнути 0^0 або 0^від'ємне

y = x ** np.cos(x)

plt.plot(x, y, 
         label='y = $x^{\\cos(x)}$', 
         color='red', 
         linewidth=3, 
         linestyle='-')

plt.title('Графік функції $y = x^{\\cos(x)}$', fontsize=14)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.grid(True)

plt.show()