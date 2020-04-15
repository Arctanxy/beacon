from beacon.optim.optimizer import Optimizer

class SGD(Optimizer):

    def __init__(self, parameters, lr=0.01):
        super().__init__(parameters, lr=lr)

    def step(self):
        for parameter in self.parameters:
            parameter -= self.lr*parameter.grad