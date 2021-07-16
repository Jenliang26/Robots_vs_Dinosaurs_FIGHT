from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur("Billy")
        self.dinosaurs.append(dino_one)
        dino_two = Dinosaur("Stan")
        self.dinosaurs.append(dino_two)
        dino_three = Dinosaur("Steve")
        self.dinosaurs.append(dino_three)
