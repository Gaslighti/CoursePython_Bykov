import random
import numpy as np
import matplotlib.pyplot as plt

class neural:

    def __init__(
            self,
            path_dataset='',
            input_dim=9,
            output_dim=2,
            h_dim=25,
            alpha=0.00001,
            num_epochs=1000,
            batch_size=30
    ):

        self.path_dataset = path_dataset
        self.INPUT_DIM = input_dim
        self.OUT_DIM = output_dim
        self.H_DIM = h_dim

        self.ALPHA = alpha
        self.NUM_EPOCHS = num_epochs
        self.BATCH_SIZE = batch_size
        self.dataset = []
        self.nn_weights = {}

        @staticmethod
        def softmax_batch(t):
            out = np.exp(t)
            return out / np.sum(out, axis=1, keepdims=True)

        @staticmethod
        def sparse_cross_entropy_batchs(z, y):
            return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

        @staticmethod
        def to_full_batchs(y, num_classes):
            y_full = np.zeros((len(y), num_classes))
            for j, yj in enumerate(y):
                y_full[j,yj] = 1
            return y_full

        @staticmethod
        def relu(t):
            return np.maximum(t, 0)

        @staticmethod
        def relu_deriv(t):
            return (t >= 0).astype(float)

        def data_preparation(self):

            dataset = np.genfromtxt(self.path_dataset, delimiter=',', dtype=float)
            dataset = dataset[1:]

            for i in range(len(dataset[0]) - 1):
                dataset = dataset[~np.isnan(dataset[:, i])]

            dataset[:, 2] = dataset[:, 2]*0.001
            dataset[:, 4] = dataset[:, 4] * 0.01
            dataset[:, 5] = dataset[:, 5] * 0.01
            dataset = np.around(dataset, 2)

            target = dataset[:, -1]
            dataset = dataset[:, :9]

            if dataset.shape[0] != target.shape[0]:
                raise Exception('Количсетво обучаемой выборки не равно количеству ответов')

            self.dataset = [(dataset[i][None, ...], int(target[i])) for i in range(len(target))]

        def inference(self, x):
            if not self.nn_weights:
                raise Exception('Сеть не обучена')
            t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
            h1 = self.relu(t1)
            t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
            z = self.softmax_batch

            return np.argmax(z)

        def calc_accuracy(self):
            correct = 0
            for x, y in self.dataset:
                z = self.inference(x)
                y_pred = np.argmax(z)
                if y_pred == y:
                    correct += 1
            accuracy = correct / len(self.dataset)
            return accuracy

        def training(self):
            self.data_preparation()

            self.nn_weihts['W1'] = np.random.rand(self.INPUT_DIM, self.H_DIM)
            self.nn_weihts['b1'] = np.random.rand(1, self.H_DIM)
            self.nn_weihts['W2'] = np.random.rand(self.H_DIM, self.OUT_DIM)
            self.nn_weihts['b2'] = np.random.rand(1, self.OUT_DIM)

            self.nn_weihts['W1'] = (self.nn_weihts['W1'] - 0.5) * 2 * np.sqrt(1/self.INPUT_DIM)
            self.nn_weihts['b1'] = (self.nn_weihts['b1'] - 0.5) * 2 * np.sqrt(1/self.INPUT_DIM)
            self.nn_weihts['W2'] = (self.nn_weihts['W2'] - 0.5) * 2 * np.sqrt(1/self.H_DIM)
            self.nn_weihts['b2'] = (self.nn_weihts['b2'] - 0.5) * 2 * np.sqrt(1/self.H_DIM)

            loss_arr = []

            for ep in range(self.NUM_EPOCHS):
                random.shuffle(self.dataset)
                for i in range(len(self.dataset) // self.BATCH_SIZE):
                    batch_x, batch_y = zip(*self.dataset[i * self.BATCH_SIZE: i * self.BATCH_SIZE + self.BATCH_SIZE])
                    x = np.concatenate(batch_x, axis=0)
                    y = np.array(batch_y)

                #Нет смысла писать дальше. Не работает

