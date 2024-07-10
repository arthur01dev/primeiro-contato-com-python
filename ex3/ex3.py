# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lista_de_nomes = ['Gabriel', 'Manuela', 'Claudia', 'Getulio']

# lista_de_anos = [2002, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# lista_de_nomes = ['Gabriel', 'Manuela', 'Claudia', 'Getulio']

# for nomes in lista_de_nomes:
#     print(f'.{nomes}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.   

# soma = 0

# for numero in range(1, 11):
#     if numero % 2 != 0:
#         soma += numero

# print(f'A soma dos numeros ímpares de 1 a 10 é: {soma}')        

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for numero in range(10, 0, -1):
#     print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero = int(input('Digite um número para ver a Tabuada: '))

# for i in range(1, 11):
#     resultado = numero * i
#     print(f'{numero} x {i} = {resultado}')    

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# numeros = [34, 56, 2, 6, 'j', 4, 9, 'b', 234, 74]

# soma = 0

# for numero in numeros:
#     try:
#         soma += numero
#     except TypeError:
#         print(f"Erro: {numero} não é um número e foi ignorado.")   

# print(f'A soma de todos os elementos numéricos é: {soma}')        

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

soma = sum(numeros)

try:
    media = soma / len(numeros)
except ZeroDivisionError:
    print("Erro: Não é possível calcular a média de uma lista vazia.")
else:
    print(f"A média dos valores na lista é: {media}")