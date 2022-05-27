# Big_Mart_Sales_Forecast
An end-to-end ML project to forecast the BigMart store sales

# Problem Statement
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and common patterns can be discovered. The main goal is to make analysis of data and to build Machine learning model to predict the sales of each the item at a particular outlet. We have 12 columns and 8523 rows of data. We get this data from Kaggle.

# Tech Stack:
* Front-End: HTML, CSS
* Back-End: Flask
* Tools: AWS EC2, Jupyter notebook, Sypder

# Data Description
The data is obtained from a kaggle website.
dataset link: https://www.kaggle.com/datasets/mrmorj/big-mart-sales

Dimension: The dataset has 8523 rows and 12 columns

Features:
* Item_Identifier :  Unique product ID

* Item_Weight :  Weight of the product

* Item_Fat_Content :  Whether the product is low fat or not

* Item_Visibility :  The % of total display area of all products in a store allocated to the particular product

* Item_Type :  The category to which the product belongs

* Item_MRP :  Maximum Retail Price (list price) of the product

* Outlet_Identifier :  Unique store ID

* Outlet_Establishment_Year :  The year in which store was established

* Outlet_Size :  The size of the store in terms of ground area covered

* Outlet_Location_Type :  The type of city in which the store is located

* Outlet_Type :  Whether the outlet is just a grocery store or some sort of supermarket

* Item_Outlet_Sales :  Sales of the product in the particular store. This is the outcome variable to be predicted.

# EDA:
* Features having missing values are Item_Weight and Outlet_Size
* Check for outliers in numerical features using boxplots
* Analyze the data distribution in each feature using graphs
* Plot correlation matrix

## Distribution of numerical features:
![big_mart_num_cols](https://user-images.githubusercontent.com/49038495/165883914-6dd9750f-ecdf-4939-8648-bd80ab072d1c.png)

## Distribution of categorical features:
![big_mart_cat1](https://user-images.githubusercontent.com/49038495/165883940-9471911a-4f3b-4e18-80de-fe98c2abd12f.png)
![big_mart_cat2](https://user-images.githubusercontent.com/49038495/165883952-31fb6e42-ee33-4564-9733-59b0e3cba485.png)


# Data-preprocessing:
* Handling outliers using IQR
* Handling missing values using bfill, ffill and mean
* Drop features that are not required
* Feature transformation
* Encode categorical features

# Model Building:
* Analyze the performance using different regression algorithms
* Hyperparameter tuning on XGBoost model
* Save the model

# Deployment:
* Prepare a flask webapp
* Deploy it on AWS EC2 instance
* Please refer to my blog on how to deploy an application on EC2: https://parisrohan.medium.com/how-to-deploy-a-flask-application-on-aws-ec2-instance-d5c44c00d133

# Webapp screenshots:
![image](https://user-images.githubusercontent.com/49038495/164762371-40c4e31d-61e5-4cc9-9c1b-16786fa3559b.png)
![image](https://user-images.githubusercontent.com/49038495/164762444-2fe87bcf-7ae5-4837-8945-14ba001adeb7.png)
