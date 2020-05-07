import numpy as np

class F2AN2:

    def __init__(self, *layers):
        self.shapes = [(layers[i + 1], layers[i]) for i in range(len(layers) - 1)]
        self.weights = [np.random.uniform(-1, 1, size=shape) for shape in self.shapes]
        self.biases = [np.random.uniform(-1, 1, size=l) for l in layers[1:]]

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, x):
        for i in range(len(self.weights)):
            x = self.activation(np.dot(self.weights[i], x.T) + self.biases[i])
        return x

    def linearize(self, weights):
        linearized_weights = []

        for ws in weights:
            shape_lenght = len(ws.shape)
            while shape_lenght > 1:
                ws = ws.flatten()
                shape_lenght = len(ws.shape)
            linearized_weights.extend(ws)

        return linearized_weights

    def export_weights(self):
        return dict(
            biases = self.linearize(self.biases),
            weights = self.linearize(self.weights)
        )

    def __import(self, linearized_dict, key):
        weights = []
        acc_index = 0

        for w in self.__getattribute__(key):
            weights.append(np.array(linearized_dict[key][acc_index:acc_index + w.size]).reshape(w.shape))
            acc_index += w.size

        return weights

    def import_weights(self, linearized_dict):
        weights = self.__import(linearized_dict, 'weights')
        biases = self.__import(linearized_dict, 'biases')

        self.weights = weights
        self.biases = biases


# net = F2AN2(2, 4, 4, 1)
# # ld = net.export_weights()
# # print(ld['biases'])
# zeros = np.zeros((28))
# ones = np.ones((9))

# print(zeros)
# print(ones)
# print(net.biases)

# ld = dict(biases=ones, weights=zeros)
# net.import_weights(ld)
# print(net.biases)
