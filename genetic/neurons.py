import numpy as np
#TODO:save dict

#objectif : Qlearning

#Un dictionnaire de dictionnaire, à savoir dictionnaire de deux valeurs,
# mais d'abord indexées par leurs états, de sorte à pouvoir les argmax aisément

def normalize(x):
    return (x-x.mean())/x.std()
def id(x):
    return x
def sigmoid(x):
    return 1/(1+np.exp(-x))
"""
    faire un reseau de neurones sans l'entrainer, choisir le(s) meilleur aléatoire.
"""
class Neuron():
    def __init__(self,input_size,activation=None):
        self.input_size=input_size
        self.weights=np.random.rand(self.input_size)
        self.bias=np.random.rand(1)
        self.activation = id
        if activation == 'sigmoid':
            self.activation=sigmoid
    def forward(self,x):
        return self.activation(self.weights @ x + self.bias)

"""
    faire un reseau de neurones sans l'entrainer, choisir le(s) meilleur aléatoire.
"""
class Layer():
    def __init__(self,input_size,output_size,activation=None):
        self.neurons=np.array([Neuron(input_size,activation) for _ in range(output_size)])
    def forward(self,input):
        return np.array([n.forward(input) for n in self.neurons])

"""
    faire un reseau de neurones sans l'entrainer, choisir le(s) meilleur aléatoire.
"""
class Model():
    def __init__(self,n_inputs,n_actions):
        self.hidden1=Layer(n_inputs,20)
        self.hidden2=Layer(20,20)
        self.output=Layer(20,4)
    def forward(self,x):
        x=self.hidden1.forward(x)
        x=normalize(x)
        x=self.hidden2.forward(x)
        x=normalize(x)
        x=self.output.forward(x)
        return x
    def layers(self):
        return [self.hidden1,self.hidden2,self.output]
if __name__=='__main__':
    m = Model(4,3)
    print(m.forward(normalize(np.array([1,2,3,4]))))
