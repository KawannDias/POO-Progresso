#objetivo deste arquivo python é:
#apender o metodos de classes e objetos
#para isto aprendi a usar o init e fazer objetos herdarem estes atributos


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
    def __str__(self):
        return f"o monstro tem {self.health} de vida e {self.energy} de energia"
    def __add__(self,other):
        return self.health + other
    def attack(self,amount):
        print("O monstro atacou!")
        print(f"{amount} de dano.")
        self.energy -= 20
        print(self.energy)
    def move(self,speed):
        print("o monstro se moveu.")
        print(f"a velocidade é de {speed}.")

monster1 = Monster(10,50)
print(monster1 + 55)  # Cria um novo Monster com a vida aumentado, aqui estou usando o (__add__), para adicionar a vida.
print(monster1)       # Usa o método __str__

#aprendi a criar uma classe e passa os atributos através do init(assim consigo passar os parametros que desejo para cada objeto posterior)
#ao concluir aprendi a ultilizar os metodos (len,abs,call,str)
# len:representandoa "vida" do monstro.
# abs:representando a "energia" do monstro.
# call:Permite que você chame uma instância da classe como se fosse uma função.No exemplo, retorna uma mensagem indicando que o monstro foi chamado.
# str:Fornece uma representação legíveldo monstro, mostrando seus atributos `health` e `energy`.
# add:Permite que você use o operador + para somar um valor ao atributo do monstro. 
