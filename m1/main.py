#Ítalo de Andrade Teles Ocimar Lima
import os
import getpass

def login_usuario(nome_usuario, senha):
    with open('usuarios.txt', 'r') as login_arquivo:
        linhas = login_arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(',')
            usuario = None
            senha_usuario = None
            for parte in partes:
                if 'usuario' in parte:
                    usuario = parte.split(':')[1].strip()
                elif 'senha' in parte:
                    senha_usuario = parte.split(':')[1].strip()
            if usuario == nome_usuario and senha_usuario == senha:
                return True
        return False

def cadastrar_usuario():
    usuario = input("Insira o seu perfil de usuário: ")
    senha = getpass.getpass(prompt='insira a sua senha: ', stream=None)
    senha2 = getpass.getpass(prompt='insira novamente a sua senha: ', stream=None)
    while senha != senha2:
        print("=-=-=-=-=-=-=-=-=-=-=-=")
        print("!! AS SENHAS DIGITADAS NÃO CORRESPONDEM TENTE NOVAMENTE !!")
        print("=-=-=-=-=-=-=-=-=-=-=-=")
        senha = getpass.getpass(prompt='insira a sua senha: ', stream=None)
        senha2 = getpass.getpass(prompt='insira novamente a sua senha: ', stream=None)  
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    print("!! CADASTRO REALIZADO COM SUCESSO !!")
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f"usuario: {usuario}, senha: {senha}\n")
    with open('permissoes.txt', 'a') as arquivo:
        arquivo.write(f"{usuario}: {0}, {0}, {0}\n")

while True:

    permissão_leitura=0
    permissão_escrever=0
    permissão_excluir=0
    print("=-=-=-=-=-=-=-=")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Sair")
    print("=-=-=-=-=-=-=-=")
    escolha = int(input("Insira a sua escolha: "))
    if escolha == 3:
        print("TCHAU :3")
        break          
    elif escolha == 2:
        cadastrar_usuario()
        
    elif escolha == 1:
        while True:
            usuario_login = input("Insira o seu usuário: ")
            senha_login = getpass.getpass(prompt='insira a sua senha: ', stream=None)            
            login_valido = login_usuario(usuario_login, senha_login)
            if login_valido:
                print("!!LOGIN BEM SUCEDIDO!!")
                break
            else:
                print("Usuário ou senha incorretos!")
                tentar_novamente = input("Deseja tentar novamente? (s/n): ")
                if tentar_novamente.lower() != 's':
                    break 
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")