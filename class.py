class Mashina:
    def __init__(self, rang, model, tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik

gentra = Mashina("qora", "Gentra", "200")
damas = Mashina("oq", "Damas", "80")
BMW = Mashina("qora", "BMW M5", "250")

print(f"Gentraning rangi: {gentra.rang}")
print(f"Gentraning model: {gentra.model}")
print(f"Gentraning tezlik: {gentra.tezlik}")
print("-"*20)
print(f"Damasning rangi: {damas.rang}")
print(f"Damasning model: {damas.model}")
print(f"Damasning tezlik: {damas.tezlik}")
print("-"*20)
print(f"BMW rangi: {BMW.rang}")
print(f"BMW modeli: {BMW.model}")
print(f"BMW tezliki: {BMW.tezlik}")