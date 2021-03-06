import functools as func
import decimal
import operator
import math
import random
import neural_network as nn

"""
Dit bestand bevat de opdrachten: 4.1, 4.2.
"""

def relu(x):
    return max(0, x)

def relu_der(x):
    return x>0

def adder(input1, input2):
    first_gate = nn.Neuron([(nn.Input_neuron(input1), -0.5), (nn.Input_neuron(input2), -0.5)], -1)
    second_gate_top = nn.Neuron([(nn.Input_neuron(input1), -0.5), (first_gate, -0.5)], -1)
    second_gate_bot = nn.Neuron([(first_gate, -0.5), (nn.Input_neuron(input2), -0.5)], -1)
    
    outputS = nn.Neuron([(second_gate_top, -0.5), (second_gate_bot, -0.5)], -1)
    outputC = nn.Neuron([(first_gate, -0.5), (first_gate, -0.5)], -1)

    return outputS.get_node_input(), outputC.get_node_input()    

def tanh_der(x):
    return 1-(math.tanh(math.tanh(x)))

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
    
def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

def main():
    print('adder:')
    print(adder(1, 1))
    
    xor_inputs = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])] 
    
    xor = nn.Neural_network(2, [2, 1], relu, relu_der, 0, 1)

    for i in range(1000):
        for input in xor_inputs:
            xor.backpropagate(input, 0.1)
    print('XOR gate:')
    for input in xor_inputs:
        print(xor.get_output(input[0]), ' -> ', input[1])

    
    nor_inputs = [([0, 0, 0], 1), ([1, 1, 1], 0), ([1, 0, 0], 0), ([0, 1, 0], 0), ([0, 0, 1], 0), ([1, 1, 0], 0), ([0, 1, 1], 0), ([1, 0, 1], 0)]
    and_inputs = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]
    or_inputs = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 1)]     
    
    nor = nn.Neural_network(3, [1], sigmoid, sigmoid_der)
    and_gate = nn.Neural_network(2, [1], sigmoid, sigmoid_der)
    or_gate = nn.Neural_network(2, [1], sigmoid, sigmoid_der)
    
    for i in range(1000):
        for input in nor_inputs:
            nor.feed_forward(input, 0.1)
    for i in range(1000):
        for input in and_inputs:
            and_gate.feed_forward(input, 0.1)
    for i in range(1000):
        for input in or_inputs:
            or_gate.feed_forward(input, 0.1)
    #some extras
    print('----------------')    
    print('NOR gate:')
    for input in nor_inputs:
        print(nor.get_output(input[0]), ' -> ', input[1])
    print('----------------')
    print('AND gate:')
    for input in and_inputs:
        print(and_gate.get_output(input[0]), ' -> ', input[1])
    print('----------------')
    print('OR gate:')
    for input in or_inputs:
        print(or_gate.get_output(input[0]), ' -> ', input[1])
    

if __name__ == '__main__':
    main()
