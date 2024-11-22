import random
from clases import Detector, Radiacion, Virus, Sanador

def generar_adn_aleatorio() -> list:
    """Genera una matriz de ADN aleatoria de 6x6."""
    bases = ['A', 'T', 'C', 'G']
    return [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]

def obtener_adn_usuario() -> list:
    """Pide al usuario ingresar una matriz de ADN de 6x6."""
    print("Ingrese una matriz de ADN de 6x6 (una fila a la vez):")
    adn = []
    for i in range(6):
        fila = input(f"Fila {i + 1}: ").strip().upper()
        # Validación de longitud de la fila
        while len(fila) != 6 or any(base not in "ATCG" for base in fila):
            print("Error: Cada fila debe tener exactamente 6 caracteres (A, T, C o G).")
            fila = input(f"Fila {i + 1}: ").strip().upper()
        adn.append(fila)
    return adn

def seleccionar_matriz_inicial() -> list:
    """Permite al usuario decidir si desea ingresar una matriz de ADN manualmente o generar una aleatoria."""
    print("Seleccione cómo desea obtener la matriz de ADN:")
    print("1. Ingresar manualmente")
    print("2. Generar aleatoriamente")
    opcion = input("Ingrese 1 o 2: ").strip()
    while opcion not in ["1", "2"]:
        print("Opción inválida. Intente de nuevo.")
        opcion = input("Ingrese 1 o 2: ").strip()
    
    if opcion == "1":
        return obtener_adn_usuario()
    elif opcion == "2":
        adn = generar_adn_aleatorio()
        print("\nMatriz de ADN generada aleatoriamente:")
        for fila in adn:
            print(fila)
        return adn

def mostrar_menu():
    """Muestra el menú principal y solicita al usuario una opción válida."""
    print("\nOpciones:")
    print("1. Detectar mutaciones")
    print("2. Aplicar una mutación")
    print("3. Sanar mutaciones")
    print("4. Salir")
    opcion = input("Seleccione una opción (1, 2, 3 o 4): ").strip()
    while opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Intente de nuevo.")
        opcion = input("Seleccione una opción (1, 2, 3 o 4): ").strip()
    return opcion

def imprimir_adn(matriz_adn: list, mensaje: str):
    """Imprime el ADN actual junto con un mensaje."""
    print("\n" + mensaje)
    for fila in matriz_adn:
        print(fila)

def main():
    try:
        # Seleccionamos la matriz inicial
        matriz_adn = seleccionar_matriz_inicial()
        
        while True:
            opcion = mostrar_menu()

            # Creamos las instancias necesarias
            detector = Detector()
            sanador = Sanador()

            if opcion == "1":
                # Detectar mutaciones
                es_mutante = detector.detectar_mutantes(matriz_adn)
                mensaje = "Se ha detectado una mutación en el ADN." if es_mutante else "El ADN no contiene mutaciones."
                imprimir_adn(matriz_adn, mensaje)
            
            elif opcion == "2":
                # Aplicar una mutación
                tipo_mutacion = input("Seleccione tipo de mutación ('H' para horizontal, 'V' para vertical, 'D' para diagonal): ").strip().upper()
                base_nitrogenada = input("Seleccione la base nitrogenada para la mutación (A, T, C o G): ").strip().upper()
                posicion_inicial = input("Ingrese la posición inicial de la mutación (formato fila,columna): ").strip()
                
                try:
                    fila, col = map(int, posicion_inicial.split(","))
                    if tipo_mutacion in ["H", "V"]:
                        # Radiación (horizontal o vertical)
                        radiacion = Radiacion(base_nitrogenada)
                        matriz_adn = radiacion.crear_mutante(matriz_adn, (fila, col), tipo_mutacion)
                    elif tipo_mutacion == "D":
                        # Virus (diagonal)
                        virus = Virus(base_nitrogenada)
                        matriz_adn = virus.crear_mutante(matriz_adn, (fila, col))
                    else:
                        print("Error: Tipo de mutación inválido.")
                        continue

                    imprimir_adn(matriz_adn, "Se ha aplicado la mutación con éxito.")
                except ValueError:
                    print("Posición inicial inválida. Asegúrese de usar el formato fila,columna.")
                except Exception as e:
                    print(f"Error al aplicar la mutación: {e}")
            
            elif opcion == "3":
                # Sanar mutaciones
                matriz_adn = sanador.sanar_mutantes(matriz_adn, detector)
                imprimir_adn(matriz_adn, "El ADN ha sido sanado. No contiene mutaciones.")
            
            elif opcion == "4":
                # Salir del programa
                imprimir_adn(matriz_adn, "Estado final del ADN. Saliendo del programa. ¡Hasta luego!")
                break
            
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

# Punto de entrada principal
if __name__ == "__main__":
    main()
