def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

#Se definen las funciones lambda para las operaciones de la calculadora
suma = lambda /x, y: x + y
resta = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Error: No se puede dividir por cero."

#funcion que devuelve el resultado de la operacion
def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    try:
        result = callback(num1, num2)
        print("Resultado:", result)
    except Exception as e:
        print("Error:", e)



def main():
    operations = {'+': suma, '-': resta, '*': mult, '/': div} #parametro para saber cual operacion realizar

    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()
