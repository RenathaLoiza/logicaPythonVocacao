import random
#Calculatora
print("Calculadora simples")

opcao=input("voce deseja 1-soma 2-subtração 3-multiplicação 4-divisão ")

if opcao == "1":
   num5=int(input("Digite o primeiro numero "))
   num6=int(input("Digite o segundo numero "))
   som= num5+num6
   print(f"resultado da soma de numero {num5} + {num6} = {som}")

elif opcao== "2":
   num5=int(input("Digite o primeiro numero "))
   num6=int(input("Digite o segundo numero "))
   som= num5-num6
   print(f"resultado da soma de numero {num5} - {num6} = {som}")
elif opcao== "3":
   num5=int(input("Digite o primeiro numero "))
   num6=int(input("Digite o segundo numero "))
   som= num5*num6
   print(f"resultado da soma de numero {num5} * {num6} = {som}")
elif opcao== "4":
   num5=int(input("Digite o primeiro numero "))
   num6=int(input("Digite o segundo numero "))
   som= num5/num6
   print(f"resultado da soma de numero {num5} / {num6} = {som}")

# jogo de adivinha

def jogo_adivinha():
   numero= []
   random.randint()

