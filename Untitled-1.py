#!/usr/bin/env python
print("*********Seja Bem vindo ao seu boletim Online**********")

nome_completo = input("Por Favor Digite seu nome completo: ")
print("Que nome Bonito!")
nota1_semestre = int(input("Digite qual foi sua nota no primeiro semestre: "))
nota2_semestre = int(input("Digite qual foi sua nota no segundo semestre: "))
calculo = ((nota1_semestre  + nota2_semestre) / 2)
if (calculo >= 7):
    print("Uau você estudou bastante!")
    print(f"Você passou de ano sua nota foi de {calculo}")
else:
    print("você precisa estudar mais!")
    print(f"Você não passou de ano sua nota foi de {calculo}")
    



