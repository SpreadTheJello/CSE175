#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# ALSO, PROVIDE ANSWERS TO THE FOLLOWING TWO QUESTIONS.
# 
# I've used TensorFlow and Pytorch before so this was fairly easy.
# The only thing I forgot to do was set the hidden units to 20, 16, 12, so I had
# to go back and change that after getting different results.
# 
# Which network architecture achieves the lowest training set error?
# The one with two hidden layers, AnnTwoHid, achieves the lowest training set error of an average of 0.02.
# 
# Which network architecture tends to exhibit the best testing set accuracy?
# The one with one hidden layers, AnnOneHid, tends to exhibit the best testing set accuracy of an average of 0.98. (Althought it was close with the two hidden layers, AnnTwoHid)
#
# PLACE YOUR NAME AND THE DATE HERE
# Angelo Fatali - 12/13/2022
#

# PyTorch - Deep Learning Models
import torch.nn as nn
import torch.nn.functional as F


# Number of input features ...
input_size = 4
# Number of output classes ...
output_size = 3


class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.layer = nn.Linear(input_size, output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        y_hat = self.layer(x)

        return y_hat


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.layer1 = nn.Linear(input_size, 20)
        self.layer2 = nn.Linear(20, output_size)


    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x = F.relu(self.layer1(x))
        y_hat = self.layer2(x)
        return y_hat


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.layer1 = nn.Linear(input_size, 16)
        self.layer2 = nn.Linear(16, 12)
        self.layer3 = nn.Linear(12, output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        y_hat = self.layer3(x)
        return y_hat
