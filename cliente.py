class Pet:
    def __init__(self, nome, especie, raca):
        self.nome = nome
        self.especie = especie
        self.raca = raca

    def __str__(self):
        return f"{self.nome} ({self.especie} - {self.raca})"

class Cliente:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.pets = []  

    def adicionar_pet(self, pet_objeto):
        self.pets.append(pet_objeto)
