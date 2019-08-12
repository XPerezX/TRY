from random import randint
class Monstros :

    def __init__(self, name, el_type, pow_attack, pow_def, hp, evo, level , attacks, deffs):
        self.name = name
        self.el_type = el_type
        self.pow_attack = pow_attack
        self.pow_def = pow_def
        self.hp = hp
        self.evo = evo
        self.level = level
        self.attacks = attacks
        self.deffs = deffs

    def atacar(self):

        return self.pow_attack * self.evo * self.level * randint(1, 5)


    def defender(self):

        return self.pow_def * self.evo * self.level * randint(1, 3)

def briga(tr1,tr2):
    count1 = 0
    count2 = 0
    for num in range(10):
        print (tr1.name," Ataca ", tr2.name, " defendeu \n",  "Round" ,num, tr1.attacks[num], " vs ", tr2.deffs[num] ,"\n")

        if (tr1.attacks[num] > tr2.deffs[num]):
            count1 += 1
            print (tr1.name, " VENCEU! \n")
        if (tr1.attacks[num] == tr2.deffs[num]):
            print("Empate \n")

        if (tr1.attacks[num] < tr2.deffs[num]):
            print(tr2.name, " VENCEU! \n")
            count2 +=1

# Agora o monstro 2 ataca e o 1 defende
        print("Agora \n")
        print(tr2.name, " Ataca ", tr1.name, " defendeu \n", tr2.attacks[num], " vs ", tr1.deffs[num],
              "\n")
        if (tr2.attacks[num] > tr1.deffs[num]):
            count2 += 1
            print (tr2.name, " VENCEU! \n")
        if (tr2.attacks[num] == tr1.deffs[num]):
            print("Empate \n")

        if (tr2.attacks[num] < tr1.deffs[num]):
            print(tr1.name, " VENCEU! \n")
            count1 +=1





    if (count1 > count2):
        print(tr1.name, " Foi o Grande Vencedor \n")
    if (count1 == count2):
        print("Foi Um grande Empate \n")
    if (count2 > count1):
        print(tr2.name, " Foi o Grande Vencedor \n")





'''def treta (tr1,tr2):

    print("\n Primeiro monstro atacando e segundo defendendo")
    tr2.hp -= tr1.atacar() - tr2.defender()
    print("primeiro monstro ", tr1.name, "tem", tr1.hp, " de vida e o segundo monstro ", tr2.name, "tem", tr2.hp, " de vida \n")
    print("\n o segundo ataca e o primeiro defende")
    tr1.hp -= tr2.atacar() - tr1.defender()
    print("\n primeiro monstro ", tr1.name, "tem", tr1.hp, " de vida e o segundo monstro ", tr2.name, "tem", tr2.hp,
          " de vida")
    if (tr1.hp > tr2.hp):
        print(tr1.name, "venceu \n")

    else:
        print(tr2.name, "venceu \n")'''


mon1 = Monstros("Carlos", "vento", 10, 5 , 500 , 2 , 5 ,[10,2,13,32,5,16,96,54,0,40],[2,15,36,85,1,0,12,13,15,15])

mon2 = Monstros("Jonny", "agua", 15, 4 , 490 , 3 , 5, [1,5,10,35,52,19,60,5,2,54],[2,14,3,3,14,2,43,32,25,3])

#treta(mon1,mon2)

print("Batalha")

briga(mon1,mon2)

