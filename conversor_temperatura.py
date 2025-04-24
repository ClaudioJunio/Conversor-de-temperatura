def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def menu():
    print("Conversor de Temperatura")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("0 - Sair")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            c = float(input("Digite a temperatura em Celsius: "))
            f = celsius_para_fahrenheit(c)
            print(f"{c:.2f}°C = {f:.2f}°F")

        elif opcao == "2":
            f = float(input("Digite a temperatura em Fahrenheit: "))
            c = fahrenheit_para_celsius(f)
            print(f"{f:.2f}°F = {c:.2f}°C")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
