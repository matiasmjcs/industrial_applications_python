import math
class Motor:
    def __init__(self, marca: str, modelo: str, voltaje: float, ampere: float):
        self.marca: str = marca
        self.modelo: str = modelo
        self.voltaje: float = voltaje
        self.ampere: float = ampere
        self.potencia_aparente: float = self.voltaje * self.ampere
        self.potencia_activa: float = 0
        self.potencia_reactiva: float = 0
        self.factor_de_potencia_actual: float = None
        self.angulo_de_fase_actual: float = None
        self.lista_factor_de_potencia = []
        self.lista_angulo_de_fase = []
    
    
    def obtener_informacion(self):
        return f"Motobomba {self.marca} {self.modelo}\n" \
               f"Voltaje: {self.voltaje} V\n" \
               f"Amperaje: {self.ampere} A\n" \
               f"Potencia Aparente: {self.potencia_aparente} VA\n" \
               f"Potencia Activa: {self.potencia_activa} W\n" \
               f"Potencia Reactiva: {self.potencia_reactiva} VAR\n" \
               f"Factor de Potencia Actual: {self.factor_de_potencia_actual}\n" \
               f"Ángulo de Fase Actual: {self.angulo_de_fase_actual}\n" \
               f"Lista de Factores de Potencia: {self.lista_factor_de_potencia}\n" \
               f"Lista de Ángulos de Fase: {self.lista_angulo_de_fase}\n"

        
    def factor_de_potencia(self, potencia_activa: float):
        self.factor_de_potencia_actual = potencia_activa / self.potencia_aparente
        self.lista_factor_de_potencia.append(self.factor_de_potencia_actual)

    def calcular_angulo_de_fase(self, potencia_activa: float, potencia_reactiva: float):
        if potencia_reactiva == 0:
            self.angulo_de_fase_actual = 0
        else:
            self.angulo_de_fase_actual = math.degrees(
                math.atan(potencia_reactiva / potencia_activa))
        self.lista_angulo_de_fase.append(self.angulo_de_fase_actual)
        
motor = Motor('bosh', 'xt662', 220, )
        