# Calculadora de IMC:

flag = True

while flag:
    massa = float(input("Insira seu peso: ")) # Peso em Kilograma;
    altura = float(input("Insira sua altura: ")) # Altura em Metros;

    imc = (massa / altura ** 2)
    print(imc)
    if imc < 18.5:
        print("Abaixo do peso")
        print()
    elif 18.5 < imc < 25:
        print("Saudável")
        print()
    elif 25 < imc < 30:
        print("Peso em excesso")
        print()
    elif 30 < imc < 35:
        print("Obesidade Grau I")
        print()
    elif 35 < imc < 40:
        print("Obesidade Grau II (Severa)")
        print()
    elif imc >= 40:
        print("Obesidade Gra III (Morbida)")
        print()
