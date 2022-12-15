from cryptography.fernet import Fernet

# mensagem ao tentar ser acertada para ter o acesso liberado ao navio
senha = "Titanic"

# encriptografa a mensagem
chave = Fernet.generate_key()
fernet = Fernet(chave)
encSenha = fernet.encrypt(senha.encode())

# entrada da tentativa da senha
print('')
print('---- SENHA ENCRIPTOGRAFADA - 3 TENTATIVAS ----')

# senha descript.
decSenha = fernet.decrypt(encSenha).decode()

num_tentativas = 0
acertou = False
while num_tentativas <= 3 and acertou == False:
    tentativa = input("Para obter acesso ao navio, digite a senha descriptografada: ")
    # print(tentativa)

    num_tentativas = num_tentativas + 1

    # validacao da tentativa
    if tentativa == decSenha:
        print('')
        print('---- ACESSO CONCEDIDO ----')
        print("Senha descriptografada: ", decSenha)
        acertou = True
        break
    else:
        print('')
        print('--- SENHA INVÁLIDA - NÚMERO DE TENTATIVAS: ', num_tentativas, ' ----')
        acertou = False
 
print('')
print('---- ACESSO NEGADO ----')