from random import randint
import json
class Monstros :
    def __init__(self, name, el_type, pow_attack, pow_def, hp, evo, level):
        self.name = name
        self.el_type = el_type
        self.pow_attack = pow_attack
        self.pow_def = pow_def
        self.hp = hp
        self.evo = evo
        self.level = level
        self.attacks = []
        self.deffs = []
    def attack(self):

        return self.pow_attack * self.evo * self.level * randint(1, 5)

    def deff(self):

        return self.pow_def * self.evo * self.level * randint(1, 3)

    def SobNivel(tr):
        if (tr.el_type =="vento"):
            tr.hp += 150
            tr.pow_attack += 3
            tr.pow_def += 2

        if (tr.el_type == "fogo"):
            tr.hp += 100
            tr.pow_attack += 5
            tr.pow_def += 2

        if (tr.el_type =="agua"):
            tr.hp += 150
            tr.pow_attack += 3
            tr.pow_def += 5

    def Habilits(tr1,tr2):
        for i in range (10):
            numero1 = tr1.attack()
            numero2 = tr2.attack()
            tr1.attacks.append(numero1)
            tr2.attacks.append(numero2)

            numero3 = tr1.deff()
            numero4 = tr2.deff()

            tr1.deffs.append(numero3)
            tr2.deffs.append(numero4)

class Torneio :
    quartas = []
    semifinal =[]
    final= []

    def Batalha (tr1,tr2):
        cura1 = tr1.hp
        cura2 = tr2.hp
        while (tr1.hp > 0 and tr2.hp >0):

            for i in range (10):
                print ("O monstro ", tr1.name, "Atacou com P.attack " , tr1.attacks[i] ," E ", tr2.name,
                   " Se defende com P.Def ", tr2.deffs[i] ,"\n")
                tr2.hp -=   tr1.attacks[i] - tr2.deffs[i]



                if (tr2.hp <= 0):
                    print("O monstro ", tr2.name , " Foi derrotado")
                    print(tr1.name, " Subiu de nivel\n")

                    tr1.SobNivel()
                    Monstros.Habilits(tr1, tr2)
                    tr1.hp +=cura1
                    return tr1

                    break

                print("Agora")
                print("O monstro ", tr2.name, "Atacou com P.attack ", tr2.attacks[i], " E ", tr1.name,
                  " Se defende com P.Def ", tr1.deffs[i], "\n")

                tr1.hp -= tr2.attacks[i] - tr1.deffs[i]

                if (tr1.hp <= 0):
                    print("O monstro ", tr1.name, " Foi derrotado")
                    print(tr2.name, " Subiu de nivel \n")

                    tr2.SobNivel()
                    Monstros.Habilits(tr1, tr2)
                    tr2.hp += cura2
                    return tr2
                    break

    def Quartasf (self):
        semif = len(Torneio.semifinal)

        print("Começa as Quartas de finais")
        print("Os Competidores são ")
        for i in range(8):
            print(Torneio.quartas[i].name)

        print(Torneio.quartas[0].name, " VS ", Torneio.quartas[1].name)
        print(Torneio.quartas[2].name, " VS ", Torneio.quartas[3].name)
        print(Torneio.quartas[4].name, " VS ", Torneio.quartas[5].name)
        print(Torneio.quartas[6].name, " VS ", Torneio.quartas[7].name)


        r = Torneio.Batalha(Torneio.quartas[0],Torneio.quartas[1])
        Torneio.semifinal.append(r)
        r = Torneio.Batalha(Torneio.quartas[2], Torneio.quartas[3])
        Torneio.semifinal.append(r)
        r = Torneio.Batalha(Torneio.quartas[5], Torneio.quartas[5])
        Torneio.semifinal.append(r)
        r = Torneio.Batalha(Torneio.quartas[6], Torneio.quartas[7])
        Torneio.semifinal.append(r)
        print("COMEÇA AGORA, a Semifinal")
        print("Os competidores são")
        for l in range(4):
            print(Torneio.semifinal[l].name)
        print(Torneio.semifinal[0].name, " VS ", Torneio.semifinal[1].name)
        print(Torneio.semifinal[2].name, " VS ", Torneio.semifinal[3].name)
        s = Torneio.Batalha(Torneio.semifinal[0], Torneio.semifinal[1])
        Torneio.final.append(s)

        s = Torneio.Batalha(Torneio.semifinal[2], Torneio.semifinal[3])
        Torneio.final.append(s)

        for c in Torneio.final:
            if (c == None):
                Torneio.final.remove(c)


        print("E os finalistas são")
        for g in Torneio.final:
            print(c.name)
        print(Torneio.final[0].name, " VS ", Torneio.final[1].name)

        if (len(Torneio.final) == 1):
            print(Torneio.final[0], "É o grande vencedor ")

        else:
            s = Torneio.Batalha(Torneio.final[0], Torneio.final[1])
            print(s.name, "É o grande vencedor ")

    def briga(tr1,tr2):
        count1 = 0
        count2 = 0
        quart = len(Torneio.quartas)
        Monstros.Habilits(tr1,tr2)
        while (tr1.hp > 0 and tr2.hp >0):

            for i in range (10):
                print ("O monstro ", tr1.name, "Atacou com P.attack " , tr1.attacks[i] ," E ", tr2.name,
                   " Se defende com P.Def ", tr2.deffs[i] ,"\n")
                tr2.hp -=   tr1.attacks[i] - tr2.deffs[i]



                if (tr2.hp <= 0):
                    print("O monstro ", tr2.name , " Foi derrotado")
                    print(tr1.name, " Subiu de nivel e vai paras quartas de final\n")
                    Torneio.quartas.append(tr1)
                    Monstros.Habilits(tr1, tr2)
                    tr1.SobNivel()


                    break

                print("Agora")
                print("O monstro ", tr2.name, "Atacou com P.attack ", tr2.attacks[i], " E ", tr1.name,
                  " Se defende com P.Def ", tr1.deffs[i], "\n")

                tr1.hp -= tr2.attacks[i] - tr1.deffs[i]

                if (tr1.hp <= 0):
                    print("O monstro ", tr1.name, " Foi derrotado")
                    print(tr2.name, " Subiu de nivel e vai paras quartas de final\n")
                    Torneio.quartas.append(tr2)
                    tr2.SobNivel()
                    Monstros.Habilits(tr1, tr2)

                    break


mon1 = Monstros("Carlos", "vento", 10, 9 , 500 , 2 , 5 )

mon2 = Monstros("Jonny", "agua", 10, 9 , 490 , 3 , 4 )

mon3 = Monstros( "Igni", "fogo", 10, 9 , 540 , 4 , 3 )

mon4 = Monstros( "Rock", "fogo", 10, 9 , 430 , 2 , 4 )

mon5 = Monstros( "Bird", "vento", 10, 9 , 430 , 2 , 5 )

mon6 = Monstros( "Garu", "agua", 10, 9 , 435 , 2 , 5 )

mon7 = Monstros( "Firin", "fogo", 10, 9 , 890 , 2 , 5 )

mon8 = Monstros( "Mountain", "vento", 10, 9 , 890 , 2 , 5 )

mon9 = Monstros("Joseias", "vento", 10, 9 , 500 , 2 , 5 )

mon10 = Monstros("Marginal", "agua", 11, 9 , 490 , 3 , 5 )

mon11 = Monstros( "TooCrazy", "fogo", 12, 9 , 1000 , 4 , 3 )

mon12 = Monstros( "Marcos", "fogo", 10, 9 , 440 , 3 , 4 )

mon13 = Monstros( "Psycho", "vento", 10, 9 , 43 , 3 , 4 )

mon14 = Monstros( "LOGO", "fogo", 10, 5 , 1000 , 2 , 5 )

mon15= Monstros( "John Castro", "fogo", 11, 9 , 1000 , 2 , 5 )

mon16= Monstros( "Batista", "vento", 10, 9 , 1000 , 2 , 5 )




Torneio.briga(mon1,mon2)
Torneio.briga(mon3,mon4)
Torneio.briga(mon5,mon6)
Torneio.briga(mon7,mon8)
Torneio.briga(mon9,mon10)
Torneio.briga(mon11,mon12)
Torneio.briga(mon13,mon14)
Torneio.briga(mon15,mon16)
Torneio.Quartasf(32)



print("\n")

content ='''{"Monstruoso": [{"nome": "Jerry",
                 "el_type" : "fogo",
                 "pow_attack": "10",
                 "pow_def" : "8" ,
                 "hp" :"1000" ,
                 "evo": "3",
                 "level" : "5"
                 },
                {
                    "nome" : "lerry",
                 "el_type" : "agua",
                 "pow_attack": "12",
                 "pow_def" : "6" ,
                 "hp" :"800" ,
                 "evo": "2",
                 "level" : "7"
                }]
 }'''
data = json.loads(content)
gato = data.get("Monstruoso")
for i in gato:
    print(i)

