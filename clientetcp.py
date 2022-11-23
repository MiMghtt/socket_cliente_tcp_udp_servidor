#relacionamento entre placa de rede e sistema operacional
import socket
#fornece acesso a algumas var e function do interpretador python
import sys

def main():
    #tentar conexão tcp/ip
    try: 
        #s recebe na biblioteca socket, chamar o metodo socket passando como parametro
        #o tipo de conexão a ser feito: FAMILIA DE PROTOCOLO(AF_INET = protocolo ip), O TIPO(SOCK_STREAM = TCP), PROTOCOLO (0 = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e: 
        print('A conexão falhou!')
        print('Erro: {}'.format(e))
        #sair do programa
        sys.exit()
    print("Socket criado com sucesso")

    #Definir host e porta alvo
    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        #conexão do socket, no connect, o segundo parametro de PORTA não é aceito string e porisso
        #precisa converter para inteiro
        s.connect((HostAlvo, int(PortaAlvo)))
        print('CLiente TCP conectado com sucesso no Host: ' + HostAlvo + 'e na porta: ' + PortaAlvo)
        #finalizar a conexão depois 2 segundos
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar no host ' + HostAlvo + 'e na porta: ' +  PortaAlvo)
        print('Erro: {}'.format(e))
        #sair do programa
        sys.exit()

if __name__ == '__main__':
    main()
