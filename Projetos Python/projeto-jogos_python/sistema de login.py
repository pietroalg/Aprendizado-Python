users = {
    "usuario": ["Pietro", "Murilo"],
    "senhas": ["Pietro123", "Murilo123"]
}
usuario1, usuario2 = users["usuario"]
senha1, senha2 = users["senhas"]

while True:
    login_user = input("Digite seu usuário: ")
    login_senha = input("Digite sua senha: ")

    if login_user in usuario1:
        if login_senha == senha1:
            print(f"Olá seja bem-vindo(a) {login_user}!")
            break

    if login_user in usuario2:
        if login_senha in senha2:
            print(f"Olá seja bem-vindo(a) {login_user}!")
            break
            
    else: 
        print("Senha ou usuário incorreto... Tente novamente.")
        continue
