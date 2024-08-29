"""
Dada uma lista de números inteiros, crie uma nova lista que contenha a string
 "Par" para os números pares e "Ímpar" para os números ímpares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Requisito: Utilize list comprehension para gerar a nova lista.

Dica: Você pode usar uma expressão condicional dentro da list comprehension.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares_impares = ['Par' if num % 2 == 0 else 'Impar' for num in numeros]

print(pares_impares)