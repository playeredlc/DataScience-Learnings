# Naive Bayes Classifier

The Naive Bayes Classifier is a probabilistic machine learning model used to solve classification problems. As the name suggests, the essence of the classifier is based on the Bayes' theorem, using the theorem it is possible to find the probabability of the event <strong>A</strong> happening, given that another event <strong>B</strong> occurred. This approach assumes that the predictors/features are independent. This assumption means that the presence of one particular feature does not affect the other, that's why it is called naive. In real-world situations the independence assumption is not correct in most cases but often works well in practice.

## Spam-Filter
This directory contains the implementation of a Naive Bayes Classifier to filter spam emails, one of the classic applications of this machine learning model. The process was divided in the three parts:

* <strong>[Pre-processing the data](https://github.com/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/pre_proccess_data.ipynb)</strong>. Among other things, natural language processing (NLP) was applied to [clean and tokenize](https://github.com/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/email_nlp.py) each email in the dataset. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/pre_proccess_data.ipynb)

* <strong>[Training the model](https://github.com/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/training_model.ipynb)</strong>. Using the data generated from the pre-processing step, the model was trained (probabilities were calculated) and saved/exported to be tested and evaluated. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/training_model.ipynb) 

* <strong>[Test and Evaluation](https://github.com/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/test_evaluation.ipynb)</strong>. Visualization of the results and checking some evaluation metrics such as accuracy, recall and precision scores. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Spam-Filter/test_evaluation.ipynb)

---

<strong><i> </> </i></strong> Developed by <strong>edlc</strong>. [Get in touch!](https://github.com/playeredlc) :metal:
