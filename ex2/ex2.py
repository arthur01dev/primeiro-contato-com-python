# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# numero = int(input("Digite um numero: "))

# if numero % 2 == 0:
#     print(f"O numero {numero} que você escolheu é par.\n")
# else:
#     print(f"O numero {numero} que você escolheu é impar.\n")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# idade_usuario = int(input("Digite aqui sua idade: "))

# if idade_usuario <= 12:
#     print("Usuario é criança.")
# elif idade_usuario > 12 and idade_usuario <= 18:
#     print("Usuario é adolecente.")
# else:
#     print("Usuario é adulto.")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# nome_usuario = 'ozark'
# senha = 'arthurlindao'

# usuario_cliente = input("Digite seu nome de usuario: ")
# senha_cliente = input('Digite sua senha: ')

# if usuario_cliente == nome_usuario and senha_cliente == senha:
#     print("Usuario esta liberado.")
# else:
#     print("Usuario bloqueado.")    

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

cordenada_x = int(input("Digite sua cordenada x: "))
cordenada_y = int(input("Digite sua cordenada y: "))

def plano_cartesiano(cordenada_x, cordenada_y):
    if cordenada_x > 0 and cordenada_y > 0:
        print("Primeiro Quadrante.")
    elif cordenada_x < 0 and cordenada_y > 0:
        print("Segundo Quadrante.")
    elif cordenada_x < 0 and cordenada_y < 0:
        print("Terceiro Quadrante.")    
    elif cordenada_x > 0 and cordenada_y < 0:  
        print("Quarto Quadrante.")  
    else:
        print("Caso Contrário.")    

plano_cartesiano(cordenada_x, cordenada_y)
