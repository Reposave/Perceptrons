#How to Run
In the terminal, type 'make' to  automatically create a virtual environment and install required packages(no requirements necessary.)

'make clean' to remove binary files.

to run, type the following:

```bash
	python3 XOR.py
```
If you wish to edit outputs of the program, a few parameters can be changed in XOR.py:
verbose, set to TRUE, and it will output the iterations the Perceptron class goes through.
seeGates, set to TRUE, will print the outputs of each gate in the XOR network.
generateSets will generate training examples and validation sets at runtime.
num_of_training_sessions specifies how many iterations before the training should stop.

You can also edit the gateTrainAccuracy variable. An accuracy above 0.96 may take very long to train or not even complete.

#FILES
Perceptron.py contains the algorithm that calculates, stores weights and returns weighted sums when needed.

ANDGate.py trains a perceptron using AND logic behaviour. It can also generate the training sets needed at runtime.

ORGate.py trains a perceptron using OR logic behaviour. It can also generate the training sets needed at runtime.

NOTGate.py trains a perceptron using NOT logic behaviour. It can also generate the training sets needed at runtime.

topology.py defines the structure of the XOR network. It initiates the training of necessary gates, accepts inputs and returns outputs for a XOR gate.

XOR.py is the main driver file. Used for user inputs.
