from motor import Motor

class Motobomba(Motor):
    def __init__(self, marca: str,modelo: str, presion: float, caudal: float, voltaje: float, ampere: float): 
        super().__init__(marca, modelo, voltaje, ampere)
        self.presion: float = presion
        self.caudal: float = caudal
    
    def obtener_informacion(self):
        motor_info = super().obtener_informacion() 
        motobomba_info = f"Presión: {self.presion} psi\n" \
                         f"Caudal: {self.caudal} L/s\n"
        return motor_info + motobomba_info
    
    

   

