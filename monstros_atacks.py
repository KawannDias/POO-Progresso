# O objetivo deste arquivo python é:
# Criar uma classe que pode receber uma função como parâmetro de outra classe.
# No caso vou usar o exemplo de um monstro de um jogo que pode receber diferentes tipos de ataques.

class Monster:
    def __init__(self,func):
        self.func = func
class Attacks:
    def bite(self):
        print("O monstro atacou com bite!")

    def strike(self):
        print("O monstro atacou com strike!")
    def slash(self):
        print("O monstro atacou com slash!")      
    def kick(self):
        print("O monstro atacou com kick!")
attack =  Attacks()
monter = Monster(func = attack.bite)
monter.func()

# A classe Monster define um atributo da instância chamado func que armazena uma função.
# A classe Attacks define vários métodos que representam diferentes tipos de ataques.
# A instância attack da classe Attacks é criada, dando acesso aos métodos de ataque.
# A instância monster da classe Monster é criada, passando o método bite da instância attack como argumento.
# O comando monster.func() chama o método bite da instância attack.