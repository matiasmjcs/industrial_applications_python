import math
import numpy as np
import matplotlib.pyplot as plt

class CalculadoraPotencia:
    def __init__(self, potencia_activa, potencia_reactiva):
        if potencia_activa <= 0 or potencia_reactiva <= 0:
            raise ValueError("Las potencias deben ser números positivos.")
        
        self.potencia_activa: float = potencia_activa
        self.potencia_reactiva: float = potencia_reactiva
        self.potencia_aparente: float = math.sqrt(self.potencia_activa**2 + self.potencia_reactiva**2)

    def calcular_factor_potencia(self):
        factor_potencia = self.potencia_activa / self.potencia_aparente
        return factor_potencia

    def calcular_angulo_fase(self):
        angulo_fase_rad = math.atan(self.potencia_reactiva / self.potencia_activa)
        angulo_fase_deg = math.degrees(angulo_fase_rad)
        return angulo_fase_deg

    def calcular_angulo_desfase(self):
        angulo_desfase_rad = math.acos(self.calcular_factor_potencia())
        angulo_desfase_deg = math.degrees(angulo_desfase_rad)
        return angulo_desfase_deg
    
    def graficar_onda_electricidad(self):
        tiempo = np.linspace(0, 0.2, 500)
        frecuencia = 50  # Hz (ajusta la frecuencia según tus necesidades)
        voltaje_efectivo = 220  # V (ajusta el voltaje según tus necesidades)

        # Calcula la onda de potencia reactiva (ejemplo: onda sinusoidal)
        onda_reactiva = voltaje_efectivo * np.sin(2 * np.pi * frecuencia * tiempo)

        # Configuración de la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(tiempo, onda_reactiva, label='Potencia Reactiva')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--', label='Potencia Activa')
        plt.axhline(self.potencia_reactiva, color='green', linewidth=0.8, linestyle='--', label='Potencia Reactiva')
        plt.axhline(self.potencia_aparente, color='blue', linewidth=0.8, linestyle='--', label='Potencia Aparente')

        # Anotaciones en la gráfica con desplazamiento vertical
        offset = 30
        plt.annotate(f'Potencia Activa: {self.potencia_activa} kW', xy=(0.02, self.potencia_activa + offset), color='black')
        plt.annotate(f'Potencia Reactiva: {self.potencia_reactiva} kVAR', xy=(0.08, self.potencia_reactiva + offset), color='green')
        plt.annotate(f'Potencia Aparente: {self.potencia_aparente} kVA', xy=(0.15, self.potencia_aparente + offset), color='blue')

        plt.xlabel('Tiempo (s)')
        plt.ylabel('Potencia (unidad)')
        plt.title('Onda de Potencia en función del Tiempo')
        plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95))
        plt.grid(True)
        plt.tight_layout()  # Añadir para mejorar el espaciado
        plt.show()


# Valores de ejemplo
potencia_activa = 5.2  # kW
potencia_reactiva = 1.1  # kVAR

try:
    calculadora = CalculadoraPotencia(potencia_activa, potencia_reactiva)
    
    factor_potencia = calculadora.calcular_factor_potencia()
    potencia_aparente = calculadora.potencia_aparente
    potencia_activa = calculadora.potencia_activa
    potencia_reactiva = calculadora.potencia_reactiva
    angulo_fase = calculadora.calcular_angulo_fase()
    angulo_desfase = calculadora.calcular_angulo_desfase()

    
    calculadora.graficar_onda_electricidad()

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
