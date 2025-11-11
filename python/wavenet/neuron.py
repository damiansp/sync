import numpy as np


class Neuron:
    def __init__(self, x, y, z, activation, freq=1, amp=1):
        self.x = x
        self.y = y
        self.z = z
        self.activation = activation
        self.freq = freq  # Hz
        self.amp = amp
        self._n_inputs = 0
        self._n_outputs = 0
        self.weights = None

    @property
    def n_inputs(self):
        return self._n_inputs
    
    @n_inputs.setter
    def n_inputs(self, n):
        self._n_inputs = n

    @property
    def n_outputs(self):
        return self._n_outputs
    
    @n_outputs.setter
    def n_outputs(self, n):
        self._n_outputs = n

    def init_weights(self):
        print('In:', self._n_inputs)
        print('Out:', self._n_outputs)
        self.weights = np.random.normal(size=(self._n_inputs, self._n_outputs))
        print(self.weights.round(3))

    def get_outputs(self, inputs):
        return self.activation(inputs @ self.weights)


def relu(vec):
    vec[vec < 0] = 0
    return vec


if __name__ == '__main__':
    neur = Neuron(1, 2, 3, relu)
    neur.n_inputs = 5
    neur.n_outputs = 3
    neur.init_weights()
    out = neur.get_outputs(np.array([1, 3, 5, 10, 30]))
    print(out)
                           
