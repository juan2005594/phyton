def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    while True:
        # Solicitar datos al usuario
        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        peso = float(input("Introduce tu peso en kg: "))
        altura = float(input("Introduce tu altura en metros: "))

        # Calcular el IMC
        imc = calcular_imc(peso, altura)

        # Mostrar resultados
        nombre_completo = f"{nombre} {apellidos}"
        print(f"\nNombre completo: {nombre_completo}")
        print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

        # Clasificación del IMC
        if imc < 18.5:
            print("Clasificación: Bajo peso (riesgo bajo)")
        elif 18.5 <= imc < 24.9:
            print("Clasificación: Peso adecuado (riesgo bajo)")
        elif 25 <= imc < 29.9:
            print("Clasificación: Sobrepeso (riesgo medio)")
        elif 30 <= imc < 34.9:
            print("Clasificación: Obesidad 1 (riesgo medio)")
        elif 35 <= imc < 39.9:   
            print("Clasificación: Obesidad 2 (riesgo alto)")
        else:
            print("Clasificación: Obesidad 2 (riesgo alto)")

        # Preguntar si quiere calcular el IMC de otra persona
        continuar = input("\n¿Quieres calcular el IMC de otra persona? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()