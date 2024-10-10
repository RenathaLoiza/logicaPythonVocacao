#exercicio 1
#crie um programa que exiba se nome completo e idade
print("#############################################################")
print("nome e idade do desenvovedor")
nome= print("Renatha Loiza Monteiro E silva")
idade=print("27 anos")

#desenvolva um progrma que peça ao usuario dois numeros e mostre 2
print("#############################################################")
print("CALCULADORA")
numero1= int( input("Digite o primeiro numero "))
numero2=int(input("Digite o segundo numero "))

soma= numero1 +numero2
subtracao=numero1 - numero2
multiplicacao= numero1 * numero2
divisao= numero1 / numero2
potencia= numero1 ** numero2
modulo= numero1 % numero2

print(f"A soma dos dois numero deu {soma}")
print(f"A subtração dos dois numero deu {subtracao}")
print(f"A multiplicação dos dois numero deu {multiplicacao}")
print(f"A divisão dos dois numero deu {divisao}")
print(f"A potencia dos dois numero deu {potencia}")
print(f"A modulo dos dois numero deu {modulo}")
print("#############################################################")
#par ou impar
print("QUAL IMPAR OU PAR")
num= int(input("digite um numero "))

if num % 2 == 0:
    print("Esse numero é par")
else :
    print("Esse é impar ")

print("##############################################################")
#maior de tres numero
print("QUAL É O MAIOR")
num1 =int(input("Digite o primeiro número "))
num2 =int(input("Digite o segunda número "))
num3 =int(input("Digite o terceiro número "))

if num1 > num2 and num1 > num3:
  print(f"O primeiro numero é o maior {num1}")
elif  num2 > num1 and num2 >num3:
    print(f"O segundo numero é o maior {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O terceiro é o maior numero {num3}")
    
print("##############################################################")
#conversão de temperadora
print("Conversor de temperatura")
valor= int(input("digite 1- fahrenheit para celsius ou 2- celsius para fahrenheit "))

if valor == 1 :
   
   f=float(input("digite quantos graus em fahrenheit "))
   celsius =(f - 32 ) * 5/9
   print(f"graus {celsius}")
elif valor ==2:
   c = float(input("digite quantos graus celsius "))
   #f=float(input("digite quantos graus em fahrenheit "))
   fahrenheit= (c *9/5) + 32
   print(f"graus {fahrenheit}")

print("##############################################################")
#Calculo de media
print("Calculo de media")
nota1=float(input("digite a primeira nota "))
nota2=float(input("digite a segunda nota "))
nota3=float(input("digite a terceira nota "))
media= (nota1 + nota2 + nota3)/3

if media >= 7:
    print("parabens voce foi aprovado")
else:
    print("Voce foi reprovado")

print("##############################################################")
#Contagem de numeros de 1 ate 10
print("Contagem de numeros de 1 ate 10")  

for x in range(11):
  print(x)

print("##############################################################")
#taboada 1 ate 10
print("taboada ")  

