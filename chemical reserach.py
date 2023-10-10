import random

class ChemicalExperiment:
    def __init__(self):
        self.chemicals = {
            'Chemical A': 1,
            'Chemical B': 2,
        }
        self.reaction_products = {
            ('Chemical A', 'Chemical B'): 'Product C',
        }

    def mix_chemicals(self, chemical1, chemical2):
        if chemical1 not in self.chemicals or chemical2 not in self.chemicals:
            return "Invalid chemicals."
        
        reaction = (chemical1, chemical2) if chemical1 < chemical2 else (chemical2, chemical1)

        if reaction in self.reaction_products:
            product = self.reaction_products[reaction]
            self.chemicals.pop(chemical1)
            self.chemicals.pop(chemical2)
            self.chemicals[product] = 1
            return f"Reaction: {chemical1} + {chemical2} -> {product}"
        else:
            return "No reaction occurs."

    def run_experiment(self):
        print("Initial chemicals:")
        print(self.chemicals)

        while len(self.chemicals) > 1:
            chemical1, chemical2 = random.sample(self.chemicals.keys(), 2)
            reaction_result = self.mix_chemicals(chemical1, chemical2)
            print(reaction_result)

        print("\nFinal chemicals:")
        print(self.chemicals)

if __name__ == "__main__":
    experiment = ChemicalExperiment()
    experiment.run_experiment()
