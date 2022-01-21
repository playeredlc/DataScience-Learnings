# Linear Regression

## Simple linear regression

The goal of the simple linear regression technique is to model the relationship between two variables by finding a linear equation that best fits to the observed data.
The variables are classified as the explanatory variable (feature) and the other is the dependent variable (target). It is important to determine if there is in fact a relationship between the two variables, this relationship means that there is a significant association between them and not necessarily that one causes the other.

A numerical measure of this association is the correlation coefficient and the square of the correlation coefficient (R²), the last indicating the fraction of the variation in one variable that may explain the other variable.

A helpful visual tool to have an idea about the association between the variables is a scatterplot. When the scatterplot shows increasing or decreasing trends it indicates that there might be an association between the proprosed variables and fitting a linear regression model to the data can provide a useful model.

The ordinary least-squares regression is the most common method used for fitting a regression line. It minimizes the sum of the squares of the deviations from the fitted line to the observed value, called residuals. The ordinary least-squares regression is implemented by the LinearRegression module from [scitkit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html), which was used in the models below:

<strong>[Movies - Budget x Revenue](https://github.com/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/Movies-BudgetxRevenue/linear_regression.ipynb)</strong> - Model to predict the revenue of a movie based on its budget. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/Movies-BudgetxRevenue/linear_regression.ipynb)<br>

<strong>[Test Scores - LSD x Score](https://github.com/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/Tests-LsdxScore/lsd_score_linear_regression.ipynb)</strong> - Model to study the correlation between the performance on test scores with the tissue concentration of LSD in humans, as in this [study](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt196895635). [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/Tests-LsdxScore/lsd_score_linear_regression.ipynb)<br>

## Multiple Linear Regression

MLR is essencially an extension of simple linear regression because it involves multiple explanatory variables or features. The linear relationship between the features and target still need to exist in multivariable regression but the independent variables shouldn't be highly correlated with each other.

<br>

<strong>[House Prices Prediction Model](https://github.com/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/House-Prices-Prediction/house_prices_multivar_regression.ipynb).</strong>

The MLR  technique is implemented in the [House prices prediction model](https://github.com/playeredlc/DataScience-Learnings/tree/master/Linear-Regression/House-Prices-Prediction) which initially had 12 explanatory variables used to predict a house's price. [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/House-Prices-Prediction/house_prices_multivar_regression.ipynb)

Several tests where made to analyze the impact of each variable in the model such as the VIF (Variance Inflation Factor) to find strongly correlated variables, the p-value evaluation to understand the explanatory power of each coefficient, residual analysis, as well as different types of data visualization.

According to the results of the above mentioned, some changes and simplifications where applied to the model in order to improve/keep performance and reduce complexity.

[Valuation tool](https://github.com/playeredlc/DataScience-Learnings/blob/master/Linear-Regression/House-Prices-Prediction/boston_house_valuation.py) - After all the analysis and optimizations on the model, the core code was extracted to a python file which work as a tool to make predictions and evaluate house prices.

---

<strong><i> </> </i></strong> Developed by <strong>edlc</strong>. [Get in touch!](https://github.com/playeredlc) :metal:
