from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
import json
import plotly
import plotly.express as px
import pandas as pd

# https://stackoverflow.com/questions/22180993/pandas-dataframe-display-on-a-webpage
# https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946


app = Flask(__name__)

# df1 = pd.read_csv('Resources/worldbank_all-data.csv')
# df2 = pd.read_csv('Resources/worldbank_data_postprocessed.csv')
# features = df2.columns

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == "__main__":
   app.run(debug=False)


def main():
        
    def optionChanged(country):
        def top_features(country): 
            return
            
        def life_expectancy(country):
            df11 = df1.set_index('country_name').loc[country]
            df12 = df11.set_index('indicator_code')
            fig = px.scatter(df12.loc['SP.DYN.LE00.IN'].drop(labels=['country_code', 'indicator_name']))
            return fig.show()