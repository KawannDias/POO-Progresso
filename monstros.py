class Monster:
    def __init__(self,health,energy):


        self.health = health

        self.energy = energy

    def __len__(self):
        return self.health
    def __abs__(self):
        return self.energy
    def __call__(self):
        return "o monstro foi chamado"
    def attack(self,amount):
        print("O monstro atacou!")
        print(f"{amount} de dano.")
        self.energy -= 20
        print(self.energy)
    def move(self,speed):
        print("o monstro se moveu.")
        print(f"a velocidade é de {speed}.")

monster1 = Monster(10,50)
print(vars(monster1))
print(monster1())

