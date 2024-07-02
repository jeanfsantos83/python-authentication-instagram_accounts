import requests
import json

def verificar_autenticidade(usuario, senha):
    """Verifica a autenticidade da conta do Instagram"""
    url = "https://www.instagram.com/api/v1/accounts/login/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": usuario,
        "password": senha
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True
    return False

def main():
    while True:
        print("Menu:")
        print("  1. Verificar autenticidade de conta")
        print("  2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = input("Digite o usuário do Instagram: ")
            senha = input("Digite a senha do Instagram: ")
            if verificar_autenticidade(usuario, senha):
                print("Conta autenticada com sucesso!")
            else:
                print("Erro ao autenticar conta!")
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()