class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

class Mammal(Animal):
    def __init__(self, species, habitat, num_legs):
        super().__init__(species, habitat)
        self.num_legs = num_legs
    def feed_offspring(self):
        return "Nurses its young with milk"

class Bird(Animal):
    def __init__(self, species, habitat, num_legs):
        super().__init__(species, habitat)
        self.num_legs = num_legs
    def lay_eggs(self):
        return "Reproduces by laying eggs"

class Fish(Animal):
    def breathe_underwater(self):
        return "Extracts oxygen from water through gills"

# Exemplu de utilizare:
if __name__ == "__main__":
    cat = Mammal("Cat", "Domestic", 4)
    print(f"A {cat.species} is mammal that {cat.feed_offspring()} and has {cat.num_legs} legs")

    sparrow = Bird("Sparrow", "Forests", 2)
    print(f"A {sparrow.species} is a bird that {sparrow.lay_eggs()} and has {sparrow.num_legs} legs.")

    goldfish = Fish("Goldfish", "Aquarium")
    print(f"A {goldfish.species} is a fish that {goldfish.breathe_underwater()}.")
