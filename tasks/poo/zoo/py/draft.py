class Animal:
    def __init__(self, nome:str):
        self.nome = nome
    
    def apresentar_nome(self):
        print(f"Eu sou o(a) {self.nome}!")

    def fazer_som(self):
        pass
    
    def mover(self):
        pass
    

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("ROAAAR!")

    def mover(self):
        print("Correndo")

# leao = Leao("Simba")
# leao.apresentar_nome()
# leao.fazer_som()
# leao.mover()

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("FUUUUUM!")

    def mover(self):
        print("Passos pesados e lentos")

# elefante = Elefante("Dumbo")
# elefante.apresentar_nome()
# elefante.fazer_som()
# elefante.mover()

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Sssssss!")

    def mover(self):
        print("Rastejando")

# cobra = Cobra("Nagini")
# cobra.apresentar_nome()
# cobra.fazer_som()
# cobra.mover()

def apresentar(animal: Animal):
    print("-" * 5)
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    

    print(f"Tipo da Classe: {type(animal).__name__}")

if __name__ == "__main__":
    leao = Leao("Simba")
    elefante = Elefante("Dumbo")
    cobra = Cobra("Nagini")

    zoologico = [leao, elefante, cobra]

    print("=== VISITA AO ZOOLÓGICO ===")

    for bicho in zoologico:
        apresentar(bicho)