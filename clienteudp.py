import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com sucesso')

#setou host, porta e mensagem a ser enviada ao servidor
host = 'localhost'
porta = 5433
mensagem = 'Ola servidor'

try:
    print('Cliente: ' + mensagem)
    #enviar o objeto enpacotado para o host já setado(localhost) e a porta 5432(porta que o servidor está ouvindo)
    s.sendto(mensagem.encode(), (host, 5432))

    #dados e servidor receberão a resposta de 4096 bytes
    dados, servidor = s.recvfrom(4096)
    #ao receber a resposta, será desempacotado
    dados = dados.decode()
    #e por ultimo vai printar os dados
    print("Cliente: {}".format(dados))

finally:
    print('Cliente: fechando a conexão')
    #fechar conexão p/ ñ ficar em looping
    s.close()

