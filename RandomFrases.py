import random


while True:
    quest = input("Pergunte ao PC: ")

    list = ["Sim","Não!","Cuida da sua vida", "Não dirijo minha palavra a você!","Cala a boca e me beija","Me respeita!","Por acaso eu ligo ?","Estou aqui para o que voce precisar"]
    resp = random.choice(list)
    print(resp)

    print("\n")
    resp2 = str(input("Deseja perguntar novamente? [S/N]:  "))

    if resp2.lower() == 's':
        continue
    else:
        print("Fim....")
        break
