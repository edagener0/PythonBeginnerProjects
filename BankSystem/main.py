import json
import os
from typing import Tuple, Dict

class App:
    def __init__(self):
        pass
    
    def run(self) -> None:
        while True:
            resposta_menu_inicial = self.menu_inicial()
            self.aguardar_input()

            if resposta_menu_inicial == "1":
                dados = self.registo()
                if dados:
                    self.save_data(dados)
                self.aguardar_input()

            elif resposta_menu_inicial == "2":
                username, password = self.login()
                try:
                    dados = self.get_dados(username)
                except FileNotFoundError:
                    print("A conta não existe, por favor crie uma.")
                    self.aguardar_input()
                    continue
                
                if dados["Password"] == password:
                    print("Login com sucesso!")
                    self.aguardar_input()
                    self.conta(dados)
                else:
                    print("Credenciais erradas!")
                    self.aguardar_input()
                    continue

            elif resposta_menu_inicial == "3":
                print("Saindo do sistema...")
                break

    def menu_inicial(self) -> str:
        return input("Bem vindo ao Banco!\n1 - Registar conta\n2 - Entrar na conta\n3 - Sair\nInput: ")
    
    def registo(self) -> Dict[str, str]:
        print("----Registo----")

        username = input("Nome de Utilizador: ")
        if os.path.exists(f"{username}.json"):
            print("Este nome de utilizador já existe. Tente novamente.")
            return None  

        primeiro_nome = input("Primeiro Nome: ")
        ultimo_nome = input("Ultimo Nome: ")
        password = input("Password: ")
        idade = input("Idade: ")
        email = input("Email: ")
        telemovel = input("Telemovel: ")

        dados = {
            "Primeiro_Nome": primeiro_nome,
            "Ultimo_Nome": ultimo_nome,
            "Username": username,
            "Password": password,
            "Idade": idade,
            "Email": email,
            "Telemovel": telemovel,
            "Saldo": 0
        }

        print("Registo com Sucesso!")
        return dados
    
    def login(self) -> Tuple[str]:
        print("----LOGIN----")
        username = input("Username: ")
        password = input("Password: ")
        return username, password
    
    def conta(self, dados: Dict[str, str]) -> None:
        while True:
            print("Bem vindo " + dados["Username"])
            operacao = input("1 - Transferencia\n2 - Deposito\n3 - Ver Saldo\n4 - Sair da conta\nInput: ")
            self.aguardar_input()
            if operacao == "1":
                self.transferencia(dados)
            elif operacao == "2":
                self.deposito(dados)
            elif operacao == "3":
                self.ver_saldo(dados)
            elif operacao == "4":
                break

    def transferencia(self, dados: Dict[str, str]) -> None:
        print("----TRANSFERENCIA----")
        username_beneficiador = input("Username Beneficiador: ")
        quantidade = int(input("Quantidade em euros: "))

        saldoConta = dados["Saldo"]
        if quantidade > saldoConta:
            print("Saldo insuficiente para a transferência.")
            self.aguardar_input()
            return

        dados["Saldo"] = saldoConta - quantidade

        try:
            dadosBeneficiador = self.get_dados(username_beneficiador)
            print("O beneficiador é do nosso banco também!")
            saldoAtual = dadosBeneficiador["Saldo"]
            dadosBeneficiador["Saldo"] = saldoAtual + quantidade
            print("Transferência realizada com sucesso.")
            self.save_data(dadosBeneficiador)
        except FileNotFoundError:
            print("O beneficiador não é do nosso banco, no entanto a transferência já foi realizada com sucesso e o valor foi deduzido da sua conta.")
        
        self.save_data(dados)
        self.aguardar_input()

    def deposito(self, dados: Dict[str, str]) -> None:
        print("----Deposito----")
        quantidade = int(input("Quantidade em euros: "))
        saldo = dados["Saldo"]
        dados["Saldo"] = saldo + quantidade
        self.save_data(dados)
        self.aguardar_input()
    
    def ver_saldo(self, dados: Dict[str, str]) -> None:
        print("O seu saldo é " + str(dados["Saldo"]) + " euros.")
        self.aguardar_input()

    def save_data(self, dados: Dict[str, str]) -> None:
        with open(dados["Username"] + ".json", 'w') as ficheiro_de_dados:
            json.dump(dados, ficheiro_de_dados, indent=4)

    def get_dados(self, username: str) -> Dict[str, str]:
        with open(username + ".json", 'r') as ficheiro_de_dados:
            dados = json.load(ficheiro_de_dados)
        return dados
    
    def aguardar_input(self) -> None:
        input("Pressione Enter para continuar . . .")
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    app = App()
    app.run()
