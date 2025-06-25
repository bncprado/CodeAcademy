# You can start with the
# Cat class or erase this
# and use your own!
class Musico:
  def __init__(self,nome, idade, instrumento):
    self.nome = nome
    self.idade = idade
    self.instrumento = instrumento
    self.tira_musica = True
  
  # Create method to change
  def nao_tira_musica(self):
    self.tira_musica = False
    print(f"{self.nome} não tira as músicas.")
  # at least one attribute.
  # Ex: def change_att(self):


# Create your new pet.
batera = Musico("Guilherme", 40, "Reggae")

# Call your method on your
# new pet here.

batera.nao_tira_musica()

