import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
factor_potencia: float = 0.9783497031189412
potencia_aparente: float = 5.315072906367325
angulo_fase: float = 11.944177188446332
angulo_desfase: float = 11.944177188446329

# Cálculo de la potencia activa
potencia_activa: float = potencia_aparente * factor_potencia

# Cálculo del tiempo en segundos con más puntos para mayor detalle
tiempo = np.linspace(0, 1, 10000)  # Aumentamos la cantidad de puntos

# Cálculo de la corriente alterna en función del tiempo
corriente = np.sqrt(potencia_activa) * np.cos(2 * np.pi * 60 * tiempo + np.radians(angulo_fase))

# Graficar la corriente alterna en función del tiempo con más detalle
plt.figure(figsize=(10, 6))
plt.plot(tiempo, corriente)
plt.title('Comportamiento de la Corriente Alterna')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Corriente (A)')
plt.grid(True)
plt.show()
