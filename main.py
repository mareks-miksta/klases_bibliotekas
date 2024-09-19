class Automašīna:

    def __init__(self, marka, modelis, krasa):

        self.marka = marka
        self.modelis = modelis
        self.krasa = krasa

    def tas(self):
        print("Tas ir", self.marka, self.modelis, self.krasa)

Audi = Automašīna("Audi", "A4", "Sarkanā krāsa")
BMW = Automašīna("BMW", "X5", "Melnā krāsa")

Audi.tas()

BMW.tas()