import random
from typing import List

class Detector:
    def __init__(self):
        self.mutaciones_horizontal = False
        self.mutaciones_vertical = False
        self.mutaciones_diagonal = False
    
    def detectar_mutantes(self, matriz: List[str]) -> bool:
        """
        Detecta si en la matriz hay mutantes en direcciones horizontal, vertical o diagonal.
        
        Args:
            matriz (List[str]): Lista de strings representando el ADN.
            
        Returns:
            bool: True si hay mutantes, False si no hay.
        """
        self.mutaciones_horizontal = self._revisar_horizontal(matriz)
        self.mutaciones_vertical = self._revisar_vertical(matriz)
        self.mutaciones_diagonal = self._revisar_diagonal(matriz)
        
        return self.mutaciones_horizontal or self.mutaciones_vertical or self.mutaciones_diagonal
    
    def _revisar_horizontal(self, matriz: List[str]) -> bool:
        for fila in matriz:
            if self._buscar_secuencia(fila):
                return True
        return False

    def _revisar_vertical(self, matriz: List[str]) -> bool:
        for col in range(6):
            columna = ''.join([fila[col] for fila in matriz])
            if self._buscar_secuencia(columna):
                return True
        return False

    def _revisar_diagonal(self, matriz: List[str]) -> bool:
        for i in range(3):
            for j in range(3):
                if self._buscar_secuencia([matriz[i+k][j+k] for k in range(4)]) or \
                   self._buscar_secuencia([matriz[i+3-k][j+k] for k in range(4)]):
                    return True
        return False
    
    def _buscar_secuencia(self, cadena) -> bool:
        for i in range(len(cadena) - 3):
            if cadena[i] == cadena[i+1] == cadena[i+2] == cadena[i+3]:
                return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada: str):
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = (0, 0)
        self.orientacion_de_la_mutacion = ""
    
    def crear_mutante(self):
        pass  


class Radiacion(Mutador):
    def __init__(self, base_nitrogenada: str):
        super().__init__(base_nitrogenada)
        self.tipo = "Radiacion"
    
    def crear_mutante(self, matriz: List[str], posicion_inicial: tuple, orientacion_de_la_mutacion: str) -> List[str]:
        try:
            fila, col = posicion_inicial
            if orientacion_de_la_mutacion == "H":
                matriz[fila] = matriz[fila][:col] + self.base_nitrogenada * 4 + matriz[fila][col + 4:]
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    matriz[fila + i] = matriz[fila + i][:col] + self.base_nitrogenada + matriz[fila + i][col + 1:]
            return matriz
        except (IndexError, ValueError):
            print("Error en la mutación. Verifique las posiciones y orientación.")
            return matriz


class Virus(Mutador):
    def __init__(self, base_nitrogenada: str):
        super().__init__(base_nitrogenada)
        self.tipo = "Virus"
    
    def crear_mutante(self, matriz: List[str], posicion_inicial: tuple) -> List[str]:
        try:
            fila, col = posicion_inicial
            for i in range(4):
                matriz[fila + i] = matriz[fila + i][:col + i] + self.base_nitrogenada + matriz[fila + i][col + i + 1:]
            return matriz
        except (IndexError, ValueError):
            print("Error en la mutación. Verifique las posiciones.")
            return matriz


class Sanador:
    def __init__(self):
        self.adn_curado = []

    def sanar_mutantes(self, matriz: List[str], detector: Detector) -> List[str]:
        if detector.detectar_mutantes(matriz):
            return self._generar_adn_aleatorio()
        return matriz

    def _generar_adn_aleatorio(self) -> List[str]:
        bases = ['A', 'T', 'C', 'G']
        return [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]
