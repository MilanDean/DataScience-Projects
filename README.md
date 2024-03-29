# Data Science Projects
This is a compilation of small projects I developed related to data analytics and machine learning.

**Note**: This is a work in progress that I update when I have free time, and this repository does not represent the entirety of my understanding of data analytics and machine learning. Projects are in order from most recent commit to first commit.

# [Purchase Overlap Application](https://github.com/MilanDean/DataScience-Projects/blob/master/fastOverlap_purchases.py)
Initially tasked with analyzing a client's sales funnel, this application was created later on as part of a data project I developed that stemmed from a desire to see customer purchase behavior in a unique way. This application at its core is simple and efficient, using a hash set in O(n) time complexity to determine whether or not a unique customer ID is found in both sets. This application is designed to work with data exported from the back-end of Shopify (eCommerce Platform), allowing someone to determine whether or not a customer who is a first time buyer of product "A" ends up buying product "B". Additionally, it can be also used to analyze purchase overlap between any two products, or even two product categories, irrespective of the type of customer (returning vs first-time). This application utilizes tkinter, a GUIProgramming toolkit (Python's default) to develop graphical user interfaces.


# [Prediction of Diabetes](https://github.com/MilanDean/DataScience-Projects/blob/master/Prediction%20of%20Diabetes.ipynb)
After comparing the features against one another, there seems to be low correlation between features and predicting the development of diabetes. This notebook utilizes the Support Vector Machine (SVM) supervised learning algorithm to not only classify whether or not an individual will develop diabetes, but to determine which parameter values will yield the highest accuracy. I also incorporated the PCA algorithm for dimensionality reduction, as a means of assisting the SVM algorithm by determining which features explain the largest amount of variance, and removing the ones that explain very little variance. The dataset can be found on [here](https://www.kaggle.com/uciml/pima-indians-diabetes-database) from Kaggle.com.


# [Titanic Survival Prediction using Regression Analysis](https://github.com/MilanDean/DataScience-Projects/blob/master/Titanic%20Regression%20Analysis/Titanic%20Survival%20Prediction%20(Data%20Cleaning%20and%20Visualization).ipynb)
This famous [dataset](https://www.kaggle.com/c/titanic) from Kaggle was used for a binary classification competition, and a very commonly used dataset for beginner-level machine learning use. Similarly to my 911 Calls dataset, this notebook highlights what I have learned about data cleaning, visualization, and logistic regression, in order to predict whether or not an individual survived the sinking. The most important part of this dataset to me was learning how to organize my data in a way that made it easier to manipulate. After cleaning, I could then visualize more of my data to gather more pertinent information, and add higher quality features to the algorithm to increase efficiency and accuracy.


# [911 Calls](https://github.com/MilanDean/DataScience-Projects/blob/master/911%20Calls/DataCleaning911CallsCapstoneProject.ipynb)
__Please note:__ This way created about 3 months before uploaded to GitHub, and the date of creation in the repository is not a reflection of when this was produced.

My first capstone project related to data science, *ever*. This was completed a while back as a requirement in order to continue to the second portion of my data science bootcamp. This notebook presents my understanding of data cleaning, visualization, and problem solving. The goal of this project was to analyze a dataset containing data related to the varying types of 911 calls in order to see if I could identify any patterns, such as type of incident at a certain hour of the day, most common time of day called, etc.
