# Neural Networks

Neural network is an approach to artificial intelligence in which a machine learns how to perform an specific task by analyzing training examples. These examples are usually hand-labeled in advance. If a model is being trained to recognize objects, for example, it may be fed with a huge amount of labeled images of different objects, such as cars, computers, coffee cups and so on, the model would find out visual patterns that consistently correlate with a particular label or class.

In the [Introduction notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Intro/pretrained_neural_nets_intro.ipynb) a [pre-trained image classification model](https://keras.io/api/applications/inceptionresnetv2/) from [Keras](https://keras.io/) was used to have an initial idea of how this kind of machine learning models behave. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Intro/pretrained_neural_nets_intro.ipynb)

A neural network consist of thousands of simple processing interconnected nodes, also called neurons. These nodes are organized in layers and the data move through the layers, from the input layer all the way down to the output layer. One particular node is connected to several nodes in the layer beneath it, from which it receives data, and it is also connected to several nodes in the layer above it, to which it sends data. It is important to notice that there are different types of neural network architectures and approaches, so this workflow may vary.

To each of its incoming connections, a particular node will assign a number called 'weigth', which can be viewed as the strength of the connection. The value of the input itself and the weigth associated with the connection are multiplied and, after that, all these products are added together resulting in a single number. If that number is higher than a certain threshold value, the node 'fires', which means the node sends that number along all its outgoing connections.

The weights and thresholds are initially set as random values and during the training process these values are continually adjusted in complex ways, until data that belong to the same classes consistently yield similar outputs.

## Multilayer Perceptron
### Image Recognition
The [Multilayer Perceptron notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Multilayer-Perceptron/mlp_image_classification.ipynb) implements a MLP to recognize images from the [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html). A Multilayer Perceptron is one well-known approach to implement a neural network, it has a bi-directional propagation, where in the forward propagation the inputs and weights are multiplied as described above, and in backpropagation the weights self-adjust to reduce the loss.
The model was defined and trained using [Keras](https://keras.io/), [Tensorboard](https://www.tensorflow.org/tensorboard) and other visual tools were used to analyze and evaluate the results. Unfortunately, the model's performance was not the expected, which indicates that a multilayer perceptron is not the best choice for this kind of problem. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Multilayer-Perceptron/mlp_image_classification.ipynb)

### Handwritten Digits Recognition
To grasp the concepts of [Tensorflow](https://www.tensorflow.org/), another neural network was implemented and trained to recognize handwritten digits, this one without the assistance of [Keras](https://keras.io/). The implementation can be found in the [Handwritten Recognition notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Handwritten-Digits/handwritten_recognition.ipynb) and a great performance was achieved. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Neural_Networks/Handwritten-Digits/handwritten_recognition.ipynb)

In the past years, the best-performing AI systems, such as the speech recognizers on smartphones,
are the result of Deep Learning techniques, which is the class of algorithms in machine learning that are inspired by neural networks.

---

<strong><i> </> </i></strong> Developed by <strong>edlc</strong>. [Get in touch!](https://github.com/playeredlc) :metal:
