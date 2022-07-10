print("=============================")
print("CALCULADORA")
print("=============================")

operacao = input("Selecione a operação desejada (somar, subtrair, multiplicar ou dividir): ")
numero1 = input("Insira o primeiro número da operação: ")
numero2 = input("Insira o segundo número da operação: ")

if operacao == "somar":
    resultado = int(numero1) + int(numero2)
elif operacao == "subtrair":
    resultado = int(numero1) - int(numero2)
elif operacao == "multiplicar":
    resultado = int(numero1) * int(numero2)
elif operacao == "dividir":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "Operação não suportada, utilizar 'somar, subtrair, multiplicar ou dividir'."

print("O resultado da operação é: " + str(resultado))







