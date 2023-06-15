import random
#Inicial do Jogo
print ("Bem vindo ao jogo da velha do grupo JJCGL")
print ("Você vai jogar contra o computador")
print ("Ganha quem conseguir uma linha, coluna ou diagonal do grid com o mesmo símbolo")

print ("Você precisa escolher uma posição no tabuleiro para marcar sua jogada, veja o tabuleiro:")
print ("_ _ _")
print ("_ _ _")
print ("_ _ _")
print ("Escolha um número de 1 a 9 para sua jogada, conforme o tabuleiro a seguir:")
print ("1 2 3")
print ("4 5 6")
print ("7 8 9")
    #funcão para atualizar o tabuleiro a cada rodada
def imprime_tabuleiro(tabuleiro):
	print ("O status do tabuleiro é\n")

	for indice in range(len(tabuleiro)):
		print (tabuleiro[indice], end=" ")
		if indice == 2 or indice == 5 or indice == 8:
			print ("")
    #Verificação do tabuleiro
def verifica_tabuleiro(tabuleiro, jogador):
	
	# testando linhas
	if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	# testando colunas
	if tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	
	#testando diagonais
	if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	return 0

#Definindo um contador de escolhas
quantidade_escolhas = 0	

tabuleiro = ["_"] * 9
#Enquanto o Jogador escolher numeros difentes o jogo continua
while True:

	escolha = int(input("Qual é a sua escolha: "))
    #Caso o jogador digite a mesmo numero
	while tabuleiro[escolha-1] != "_":
		print ("Sua escolha foi inválida! Veja como está o tabuleiro")
		imprime_tabuleiro(tabuleiro)
		escolha = int(input("Qual é a sua escolha "))
    #O numero esolhido pelo jogador sera adicinado no tabuleiro
	tabuleiro[escolha-1] = "X"
	quantidade_escolhas += 1
    #Definindo uma variavel vencedor
	vencedor = verifica_tabuleiro(tabuleiro,"X")

	if vencedor != 0:
		break

	if quantidade_escolhas == 9:
		break

	imprime_tabuleiro(tabuleiro)
    #A escolha do computador sera definida de forma aleatoria com uma radiante de 1 a 9
	escolha_computador = random.randint(1,9)
	while tabuleiro[escolha_computador-1] != "_":
		escolha_computador = random.randint(1,9)

	tabuleiro[escolha_computador-1] = "O"
	quantidade_escolhas += 1

	vencedor = verifica_tabuleiro(tabuleiro,"O")
	if vencedor != 0:
		break
	imprime_tabuleiro(tabuleiro)
#Resultado final do jogo
if vencedor == 1:
	print ("Parabéns, você ganhou")
elif vencedor == 2:
	print ("Você perdeu, o computador ganhou")
else:
	print ("Deu velha, ninguém venceu, foi empate!")

imprime_tabuleiro(tabuleiro)