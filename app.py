from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn
from flask_cors import cross_origin


app = Flask(__name__, template_folder="templates")
model = pickle.load(open('bigmart_xgb.pkl', 'rb'))
print("Model Loaded")


@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('home.html')


@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():     
    
    if request.method == 'POST':
    
    
        #Outlet location type
        Outlet_Location_Type = request.form['Outlet_Location_Type']
        if(Outlet_Location_Type == 'Tier 2'):
            Tier_2=1
            Tier_3=0
        elif(Outlet_Location_Type == 'Tier 3'):
            Tier_2=0
            Tier_3=1
        else:
            Tier_2=0
            Tier_3=0


        #Outlet Type
        Outlet_Type = request.form['Outlet_Type']
        if(Outlet_Type == 'Supermarket Type1'):
            SM1=1
            SM2=0
            SM3=0
        elif(Outlet_Type == 'Supermarket Type2'):
            SM1=0
            SM2=1
            SM3=0
        elif(Outlet_Type == 'Supermarket Type3'):
            SM1=0
            SM2=0
            SM3=1
        else:
            SM1=0
            SM2=0
            SM3=0


        #Outlet Size
        Outlet_Size = request.form['Outlet_Size']
        if(Outlet_Size == 'Small'):
            Small=1
            Medium=0
        if(Outlet_Size == 'Medium'):
            Small=0
            Medium=1
        else:
            Small=0
            Medium=0

        
        #Outlet_Identifier
        Outlet_Identifier = request.form['Outlet_Identifier']
        if(Outlet_Identifier == 'OUT013'):
            OUT013=1
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0
        elif(Outlet_Identifier == 'OUT017'):
            OUT013=0
            OUT017=1
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0
        elif(Outlet_Identifier == 'OUT018'):
            OUT013=0
            OUT017=0
            OUT018=1
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0           
        elif(Outlet_Identifier == 'OUT019'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=1
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0            
        elif(Outlet_Identifier == 'OUT027'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=1
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0            
        elif(Outlet_Identifier == 'OUT035'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=1
            OUT045=0
            OUT046=0
            OUT049=0            
        elif(Outlet_Identifier == 'OUT045'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=1
            OUT046=0
            OUT049=0            
        elif(Outlet_Identifier == 'OUT046'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=1
            OUT049=0            
        elif(Outlet_Identifier == 'OUT049'):
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=1
        else:
            OUT013=0
            OUT017=0
            OUT018=0
            OUT019=0
            OUT027=0
            OUT035=0
            OUT045=0
            OUT046=0
            OUT049=0


        #Item Type
        Item_Type = request.form['Item_Type']
        if(Item_Type == 'Dairy'):
            Dairy                 = 1
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Soft_Drinks'):
            Dairy                 = 0
            Soft_Drinks           = 1
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Meat'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 1
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Fruits_and_Vegetables'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 1
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Household'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 1
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Snack_Foods'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 1
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Frozen_Foods'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 1
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Breakfast'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 1
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Health_and_Hygiene'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 1
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Hard_Drinks'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 1
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Canned'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 1
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Breads'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 1
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Starchy_Foods'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 1
            Seafood               = 0
            Others                = 0
        elif(Item_Type == 'Seafood'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 1
            Others                = 0
        elif(Item_Type == 'Others'):
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 1
        else:
            Dairy                 = 0
            Soft_Drinks           = 0
            Meat                  = 0
            Fruits_and_Vegetables = 0
            Household             = 0
            Snack_Foods           = 0
            Frozen_Foods          = 0
            Breakfast             = 0
            Health_and_Hygiene    = 0
            Hard_Drinks           = 0
            Canned                = 0
            Breads                = 0
            Starchy_Foods         = 0
            Seafood               = 0
            Others                = 0


        #Item Fat Content
        Item_Fat_Content = request.form['Item_Fat_Content']
        if(Item_Fat_Content == 'Regular'):
            reg=1
        else:
            reg=0
            
        
        #Item Weight  
        Item_Weight = float(request.form['Item_Weight'])


        #Item MRP  
        Item_MRP = float(request.form['Item_MRP'])


        #Item Visibility  
        Item_Visibility = float(request.form['Item_Visibility'])

      
        #Outlet age
        Outlet_Establishment_Year = int(request.form['Outlet_Establishment_Year'])
        Outlet_Age = 2022 - Outlet_Establishment_Year
       
       
       
        #Feature Transformation
        Item_Weight_exp             = Item_Weight**(1/1.2)
        Item_Visibility_sqaure      = Item_Visibility**(1/2)
        Item_MRP_exp                = Item_MRP**(1/1.2)
        #Item_Outlet_Sales_sqaure    = Item_Outlet_Sales**(1/2)
        Outlet_Age_sqaure           = Outlet_Age**(1/2)
        
        
        model_input=[Item_Weight_exp, Item_Visibility_sqaure, Item_MRP_exp, Outlet_Age_sqaure, reg,
                     Tier_2, Tier_3, SM1, SM2, SM3, Small, Medium, OUT013, OUT017, OUT018, OUT019, OUT027, OUT035, OUT045, OUT046, OUT049,
                     Dairy, Soft_Drinks, Meat, Fruits_and_Vegetables, Household, Snack_Foods, Frozen_Foods, Breakfast,
                     Health_and_Hygiene, Hard_Drinks, Canned, Breads, Starchy_Foods, Seafood, Others          
                    ]
            
        np_array=np.asarray(model_input)
        model_input=np_array.reshape(1,-1)
        
        prediction=model.predict(model_input)
    
        #convert sqrt output back to normal
        output= (prediction)**2
        
        if output<0:
            return render_template('result.html',prediction_texts="Sorry wrong details entered :(  ")
        else:
            return render_template('result.html', prediction=output)
    else:
        return render_template('result.html')

#use this while running in local machine
#if __name__=="__main__":
#    app.run(debug=True)

#use this while deploying
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)