def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = adicionar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")
    elif escolha == '2':
        resultado = subtrair(num1, num2)
        print(f"{num1} - {num2} = {resultado}")
    elif escolha == '3':
        resultado = multiplicar(num1, num2)
        print(f"{num1} * {num2} = {resultado}")
    elif escolha == '4':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Escolha inválida")

    # Código duplicado para demonstrar problemas de duplicação
    if escolha == '1':
        resultado = adicionar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")
    elif escolha == '2':
        resultado = subtrair(num1, num2)
        print(f"{num1} - {num2} = {resultado}")
    elif escolha == '3':
        resultado = multiplicar(num1, num2)
        print(f"{num1} * {num2} = {resultado}")
    elif escolha == '4':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Escolha inválida")

# Executar a calculadora
calculadora()
