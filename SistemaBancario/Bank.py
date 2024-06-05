from datetime import datetime

class bank:
    def __init__(self, balance):
        self.balance = balance
        self.withdrawals = [datetime.now().date(), 0]
        self.statement = []
        self.limit_per_draw = 500
        self.limit_draw = 3

    def addTransaction(self, transaction):
        self.statement.append(transaction)

    def getStatement(self):
        return self.statement

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        trasaction = f"Deposito de R$: {amount} às {datetime.now()}"
        self.addTransaction(trasaction)
        print(f"Deposito de R$: {amount} às {datetime.now()}")
    
    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.limit_per_draw:
            if self.withdrawals[0] == datetime.now().date():
                if self.withdrawals[1] < self.limit_draw:
                    self.balance -= amount
                    trasaction = f"Saque de R$: {amount} às {datetime.now()}"
                    self.addTransaction(trasaction)
                    self.withdrawals[1] += 1
                    print(f"Saque de R$: {amount} às {datetime.now()}")
                else:
                    print("Limite de saques diários ating ido")
            else:
                self.balance -= amount
                trasaction = f"Saque de R$: {amount} às {datetime.now()}"
                self.addTransaction(trasaction)
                self.withdrawals[0] = datetime.now().date()
                self.withdrawals[1] = 1
                print(f"Saque de R$: {amount} às {datetime.now()}")
        else:
            print("Saldo insuficiente")
        

if __name__ == "__main__":
    bank = bank(0.0)

    while True:
        try:
            print("""===============
1. Depositar
2. Sacar
3. Ver extrato
4. Saldo
5. Sair
================""")
            option = int(input("Opção: "))

            if option == 1:
                try:
                    amount = float(input("Quantia: "))
                    bank.deposit(float((format(amount, ".2f"))))
                except:
                    print("Quantia inválida")
                    continue      
            elif option == 2:
                try:
                    amount = float(input("Quantia: "))
                    bank.withdraw(float((format(amount, ".2f"))))
                except:
                    print("Quantia inválida")
                    continue
            elif option == 3:
                statement = bank.getStatement()
                for transaction in statement:
                    print(transaction)
            elif option == 4:
                print(" Saldo: ", bank.getBalance())
            elif option == 5:
                break
            else:
                print("Opção inválida")
        except:
            print("Opção inválida")