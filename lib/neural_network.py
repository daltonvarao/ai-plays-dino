# %%
import numpy as np


class F2AN2:

    def __init__(self, *layers):
        self.shapes = [(layers[i + 1], layers[i]) for i in range(len(layers) - 1)]
        self.weights = [np.random.uniform(-1, 1, size=shape) for shape in self.shapes]
        # self.biases = [np.random.uniform(-1, 1, size=l) for l in layers[1:]]
        self.biases = [np.zeros((l)) for l in layers[1:]]

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, x):
        for i in range(len(self.weights)):
            x = self.activation(np.dot(self.weights[i], x.T) + self.biases[i])
        return x

    def linearize_weights(self):
        weights = []

        for ws in self.weights:
            shape_lenght = len(ws.shape)
            while shape_lenght > 1:
                ws = ws.flatten()
                shape_lenght = len(ws.shape)
            weights.extend(ws)

        return weights

    def load_weights(self, linearized_weights):
        weights = []
        acc_index = 0

        for shape in self.shapes:
            length = shape[0] * shape[1]
            weights.append(np.array(linearized_weights[acc_index:acc_index + length]).reshape(shape))
            acc_index += length

        return weights
