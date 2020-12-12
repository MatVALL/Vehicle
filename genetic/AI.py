from neurons import *
import copy

"""#algorithme génetique :

    1-Initialiser les paramêtres aléatoirement
    2-Evaluer
    3-Selection (de la moitié) avec proba relative au score
    4-Muter : ici changer aléatoirement les poids d'un neurone
    5-retour à 2 (afficher les resultats du meilleur)
"""
class GeneticAlgo():
    def __init__(self,n_actions,input_size,population_size=100):
        self.population=[Model(input_size,n_actions) for _ in range(population_size)]
    def mutation(self,scores,probability=.1):
        index_sorted_by_score = np.argsort(scores)
        self.population = [self.population[i] for i in index_sorted_by_score[:index_sorted_by_score.shape[0]//2]]
        copy.deepcopy(self.population)
        for p in self.population:
            self.population.append(mutate_model(p,probability))
def mutate_model(model,probability):
    model_mutated=copy.deepcopy(model)
    for l in model_mutated.layers():
        mutate_layer(l,probability)
    return model_mutated
def mutate_layer(layer,probability):
    for n in layer.neurons:
        if np.random.choice([True,False],p=[1-probability,probability]):
            mutate_neuron(n)
def mutate_neuron(n):
    n.weights=np.random.rand(*n.weights.shape)
