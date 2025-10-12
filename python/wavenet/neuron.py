class Neuron:
    def __init__(self, x, y, z, freq=1):
        self.x = x
        self.y = y
        self.z = z
        self.freq = freq
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
        self.weights = np.random((self._n_inputs, self._n_outputs))
