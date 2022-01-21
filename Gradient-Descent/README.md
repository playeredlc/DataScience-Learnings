# Gradient Descent

Gradient descent is an optimization algorithm used to iteratively minimize a given function by moving in the direction of a local minimum. In machine learning it is used to update the parameters of a model by minimizing its cost function.

The cost or loss function measures the performance of a model in making predictions for a given set of parameters. The slope of the curve defined by this function indicates how to update the parameters to increase the accuracy of the model.

In the [Gradient Descent Introduction notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gradient_descent_intro.ipynb) a simple function was used to illustrate how the gradient descent technique would be implemented and used to reach this function's minimum. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gradient_descent_intro.ipynb)

### Mean Squared Error with Gradient Descent
The very popular loss function Mean Squared Error (MSE), commonly used in regression problems, is implemented and minimized using the gradient descent algorithm in the [MSE x Gradient Descent notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/mse_as_cost_function.ipynb). [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/mse_as_cost_function.ipynb)

### The Learning Rate
One important thing to take in consideration when defining a gradient descent algorithm is the size of the step in each iteration, which is known as the learning rate. The learning rate impacts the behavior of the algorithm. For example, with a large learning rate there is a risk of overshooting the minimum, causing the values to bounce around and never converge to the lowest value. On the other hand, a low learning rate or step size may lead to a huge amount of iterations to reach the minimum, requiring unecessary effort.
	
Some tests with different learning rates where applied and visually explored in the [Learning Rate notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gd_learning_rate.ipynb). [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gd_learning_rate.ipynb)


### Multiple Minima x Initial Guess
The cost function may consist of multiple local minima. The algortithm will converge to one of these minima depending on the starting point, also called the initial guess. Therefore, this parameter also heavily impacts the behavior of the algorthm as discussed in the [Multiple Minima x Initial Guess notebook](https://github.com/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gd_multiple_minima_vs_initial_guess.ipynb). [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Gradient-Descent/gd_multiple_minima_vs_initial_guess.ipynb)

---

<strong><i> </> </i></strong> Developed by <strong>edlc</strong>. [Get in touch!](https://github.com/playeredlc) :metal:
