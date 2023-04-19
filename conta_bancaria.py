menu = """
============MENU============

        [1]-Sacar
        [2]-Depositar
        [3]-Extrato
        [4]-Sair

============MENU============
"""


Extrato=[]
saldo=1000
while True:
        print(menu)
        opcao=int(input("Digite sua opcao: "))
      

        if opcao==1:
               valor_de_saque=int(input("Digite o quantos reais você quer sacar: "))
               saldo=saldo-valor_de_saque        
               print("valor sacado com sucesso.")
               print(f"Voce ainda tem {saldo},00R$ na sua conta.")
               texto=f"Saque de {valor_de_saque},00R$ realizado"
               Extrato.append(texto)

               
               



        elif opcao==2:
                valor_do_deposito=int(input("Digite quantos reais quer depositar na sua conta: "))
                saldo=saldo+valor_do_deposito
                print("Deposito realizado com sucesso.")
                print(f"Agora você tem {saldo},00R$ na sua conta.")
                texto=f"Depósito de {valor_do_deposito},00R$ realizado"
                Extrato.append(texto)

                

        elif opcao==3:
                for n in range(len(Extrato)):
                        print(Extrato[n])
                

        elif opcao==4:
                print("Saindo", end="...")  
                break                     


