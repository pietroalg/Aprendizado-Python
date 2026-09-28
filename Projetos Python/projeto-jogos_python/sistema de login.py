users = ("Pietro", "Murilo")
senhas = ("Pietro123", "Murilo123")

while True:
    login_user = input("Digite seu usuário: ")
    login_senha = input("Digite sua senha: ")

    if login_user == users[0]:
        if login_senha == senhas[0]:
            print(f"Olá seja bem-vindo(a) {login_user}!")
            break

    if login_user == users[1]:
        if login_senha == senhas[1]:
            print(f"Olá seja bem-vindo(a) {login_user}!")
            break

    else: 
        print("Senha ou usuário incorreto... Tente novamente.")
        continue