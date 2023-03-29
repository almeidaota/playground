#testetestetesteteste


import random 

escolhas = ['pedra', 'papel', 'tesoura']
jogardnv = "0"
empate = 0
maquina = 0
jogador = 0



while jogardnv == "0":

    escolhapc = random.choice(escolhas)
    escolhausuario = str(input('Pedra, papel, ou tesoura? ')).lower()
    
    if escolhausuario == escolhapc:
        print(f'ambos escolheram {escolhausuario}, temos um empate!\n')
        empate = empate + 1

    elif escolhausuario == 'pedra' and escolhapc == 'papel':
        print(f'você escolheu {escolhausuario} e a máquina escolheu {escolhapc}, você perdeu!\n')
        maquina = maquina +1

    elif escolhausuario == 'pedra' and escolhapc == 'tesoura':
        print(f'você escolheu pedra e a máquina escolheu tesoura, você ganhou!\n')
        jogador = jogador + 1

    elif escolhausuario == 'tesoura' and escolhapc == 'pedra':
        print(f'você escolheu tesoura e a máquina pedra, você perdeu!\n')
        maquina = maquina + 1

    elif escolhausuario == 'tesoura' and escolhapc == 'papel':
        print(f'você escolheu tesoura e a máquina papel, você ganhou!\n')
        jogador = jogador + 1

    elif escolhausuario == 'papel' and escolhapc == 'tesoura':
        print(f'você escolheu papel e a máquina tesoura, você perdeu\n')
        maquina = maquina + 1

    elif escolhausuario == 'papel' and escolhapc == 'pedra':
        print(f'você escolheu papel e a máquina pedra, você ganhou!\n') 
        jogador = jogador + 1

    else:
        print("Entrada inválida. Tente novamente.")
    
    print(f'Placar atual:\nMaquina {maquina} pontos\nEmpate {empate}\nJogador: {jogador}\n')
    jogardnv = str(input('Deseja jogar novamente? Se sim, digite 0, senão, aperte qualquer outra tecla '))
    
print('Obrigado por jogar!')