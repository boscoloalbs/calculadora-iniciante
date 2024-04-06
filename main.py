import os

def menu():
    while True:
        os.system("")
        print("########### MENU - CALCULADORA ###########")
        print("1. SOMA")
        print("2. SUBTRAÇÃO")
        print("3. DIVISÃO")
        print("4. MULTIPLICAÇÃO")
        print("5. SAIR")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            opcao = soma()
            return menu()
        elif opcao == "2":
            opcao = subtracao()
            return menu()
        elif opcao == "3":
            opcao = divisao()
            return menu()
        elif opcao == "4":
            opcao = multiplicacao()
            return menu()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")

def soma ():
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    resultado = numero1 + numero2
    return print(f"=====> O resultado da operação é: {resultado} <=====")

def subtracao():
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    resultado = numero1 - numero2
    return print(f"=====> O resultado da operação é: {resultado} <=====")

def multiplicacao():
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    resultado = numero1 * numero2
    return print(f"=====> O resultado da operação é: {resultado} <=====")

def divisao(): 
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    resultado = numero1 / numero2
    return print(f"=====> O resultado da operação é: {resultado} <=====")

opcao = menu()


