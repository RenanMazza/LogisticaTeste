#lista de valor de rotas

rotas = [
    ["BR", "BR - De Brasília para o Rio de Janeiro", 1.5],
    ["BS", "BS - De Brasília para o São Paulo", 1.2],
    ["RB", "RB - De Rio de Janeiro para Brasília", 1.5],
    ["RS", "RS - De Rio de Janeiro para São Paulo", 1],
    ["SR", "SR - De São Paulo para Rio de Janeiro", 1],
    ["SB", "SB - De São Paulo para Brasília", 1.2],
]

print('Bem vindo a Companhia de Logistica RENAN S.A\n')

#definições de variaveis
solicitarDimensoes = 1
solicitarPeso = 1
solicitarRota = 1
volumeObjeto = 0
valorVolumeObjeto = 0
multiplicadorPeso = 0
rotaSelectionada = ""
multiplicadorRota = 0


while solicitarDimensoes:
    try:
        comprimento = int(input("Digite o comprimento do objeto (em cm):"))
        largura = int(input("Digite o largura do objeto (em cm):"))
        altura = int(input("Digite o altura do objeto (em cm):"))

        # Calculo de Volume
        volumeObjeto = comprimento * largura * altura
        print("O volume do objeto (em cm3) é: {0:.2f}".format(volumeObjeto))

        if volumeObjeto < 1000:
            valorVolumeObjeto = 10
        elif 1000 <= volumeObjeto <= 10000:
            valorVolumeObjeto = 20
        elif 10000 <= volumeObjeto <= 30000:
            valorVolumeObjeto = 30
        elif 30000 <= volumeObjeto <= 100000:
            valorVolumeObjeto = 50

        # Imprime quando as dimensões são diferentes
        if valorVolumeObjeto == 0:
            print("Não aceitamos objetos com dimensões tão grandes")
            solicitarDimensoes = 1
        else:
            solicitarDimensoes = 0
    except:
        print(
            "Você digitou alguma dimensão do objeto com valor não numérico\nPor favor entre com as dimensões desejadas novamente")

while solicitarPeso:
    try:
        peso = float(input("Digite o peso do objeto (em kg):"))

        if peso < 0.1:
            multiplicadorPeso = 1
        elif 0.1 <= peso <= 1:
            multiplicadorPeso = 1.5
        elif 1 <= peso <= 10:
            multiplicadorPeso = 2
        elif 10 <= peso <= 30:
            multiplicadorPeso = 3

        # Imprime quando peso for maior que o permitido
        if multiplicadorPeso == 0:
            print("Não aceitamos objetos tão pesados\nPor favor entre com o peso desejado novamente")
            solicitarPeso = 1
        else:
            solicitarPeso = 0
    except:
        print("Você digitou o peso do objeto com valor não numérico\nPor favor entre com o peso desejado novamente")

while solicitarRota:
    print('Selecione a Rota:')

    for rt in rotas:
        print(rt[1])

    rotaSelectionada = input().upper()

    for rt in rotas:
        if rt[0] == rotaSelectionada:
            multiplicadorRota = rt[2]

    # Tratamento de rota inexistente
    if multiplicadorRota == 0:
        print("Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente")
        solicitarRota = 1
    else:
        solicitarRota = 0

total = valorVolumeObjeto * multiplicadorRota * multiplicadorPeso
print(
    "Total a pagar (R$): {0:.2f} (dimensões: {1:.2f} * peso: {2:.2f} * rota: {3:.2f})".format(total, valorVolumeObjeto,
                                                                                              multiplicadorPeso,
                                                                                              multiplicadorRota))
