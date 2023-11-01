# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input("Digite o primeiro termo da PA: "))
a3 = int(input("Digite a razão da PA: "))

for p in range(10):
    print(p)
    termo = a1 + p * a3
    print(f'Termo {p+1}: {termo}')