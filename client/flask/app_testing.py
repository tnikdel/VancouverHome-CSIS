from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        xg_reg = joblib.load("xg_reg.pkl")
        
        # Get values through input bars
        ML = request.form.get("ML")
        List_Duration = request.form.get("List_Duration")
        Bedrooms= request.form.get("Bedrooms")
        Bathrooms = request.form.get("Bathrooms")
        Area = request.form.get("Area")
        Age = request.form.get("Age")
        Frontage = request.form.get("Frontage")
        Kitchens = request.form.get("Kitchens")
        City = request.form.get("City")
        ifPendemic = request.form.get("ifPendemic")
        ifAdditionalTax = request.form.get("ifAdditionalTax")

        # Put inputs to dataframe
        X = pd.DataFrame([[ML, List_Duration,Bedrooms,
        Bathrooms , Area, Age , Frontage,
        Kitchens, City, ifPendemic, ifAdditionalTax]],
        columns = ["ML", "List_Duration","Bedrooms",
        "Bathrooms" , "Area", "Age" , "Frontage",
        "Kitchens", "City", "ifPendemic", "ifAdditionalTax"])
        
        # Get prediction
        prediction = xg_reg.predict(np.array(X))
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)


# Running the app
if __name__ == '__main__':
    app.run(host='localhost')