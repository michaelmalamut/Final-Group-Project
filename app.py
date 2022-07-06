from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from sklearn.impute import SimpleImputer
import json
import plotly
import plotly.express as px
import pandas as pd
import numpy as np

# https://stackoverflow.com/questions/22180993/pandas-dataframe-display-on-a-webpage
# https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946


app = Flask(__name__)

@app.route("/")
def index():
   # Dataframe header
   worldbank_df = pd.read_csv("Resources/worldbank_data.csv")
   x = worldbank_df.head(10)
   
   worldbank_df.rename(columns = {'Unnamed: 0':'Features'}, inplace = True)
   worldbank_df.drop('Features', axis=1, inplace=True)
   imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
   imputer = imputer.fit(worldbank_df[['ABW', 'ASM', 'BEL', 'BRB', 'AFG', 'BRN', 'ALB', 'AND', 'AGO',
       'CUW', 'DMA', 'GIN', 'GRD', 'ARG', 'ARM', 'ATG', 'AUT', 'AUS',
       'AZE', 'BDI', 'BFA', 'BGR', 'BHR', 'BHS', 'BLR', 'BLZ', 'BMU',
       'BEN', 'BGD', 'BTN', 'BIH', 'CAN', 'CHI', 'BOL', 'BRA', 'CHN',
       'CPV', 'CUB', 'CYM', 'BWA', 'CAF', 'DZA', 'HRV', 'KHM', 'TCD',
       'VGB', 'CHL', 'COD', 'CIV', 'COG', 'COM', 'COL', 'CYP', 'CZE',
       'DEU', 'CRI', 'DJI', 'DNK', 'ECU', 'ERI', 'FIN', 'FJI', 'FRA',
       'FRO', 'GIB', 'DOM', 'ETH', 'EGY', 'GNQ', 'EST', 'GRC', 'GRL',
       'GAB', 'GHA', 'GEO', 'GMB', 'GNB', 'GTM', 'GUM', 'HTI', 'JPN',
       'GUY', 'NOR', 'HKG', 'XKX', 'HND', 'HUN', 'IMN', 'IDN', 'IND',
       'IRL', 'IRQ', 'IRN', 'ISL', 'ISR', 'JAM', 'JOR', 'ITA', 'PYF',
       'SLV', 'SWZ', 'FSM', 'KAZ', 'KIR', 'KOR', 'LBN', 'LBR', 'LBY',
       'LIE', 'LSO', 'LTU', 'LUX', 'LVA', 'KEN', 'KGZ', 'MAC', 'MCO',
       'KWT', 'LAO', 'MDV', 'MEX', 'MHL', 'MAR', 'MLI', 'MMR', 'MNE',
       'MDA', 'MNP', 'MDG', 'MOZ', 'MWI', 'NAM', 'NCL', 'MKD', 'NER',
       'NGA', 'NIC', 'NLD', 'MLT', 'NPL', 'OMN', 'PRK', 'MNG', 'MRT',
       'MUS', 'KNA', 'LCA', 'MAF', 'MYS', 'NZL', 'PAK', 'ESP', 'LKA',
       'PAN', 'PER', 'PHL', 'PLW', 'SYC', 'PNG', 'POL', 'PRI', 'PRT',
       'QAT', 'PRY', 'RUS', 'SAU', 'SGP', 'SMR', 'ROU', 'RWA', 'SEN',
       'SLB', 'SOM', 'SLE', 'SSD', 'STP', 'SRB', 'SVK', 'SVN', 'SXM',
       'WSM', 'ARE', 'GBR', 'ZAF', 'SDN', 'SUR', 'SWE', 'TCA', 'CHE',
       'TKM', 'TLS', 'TON', 'TTO', 'TUV', 'SYR', 'USA', 'VCT', 'VEN',
       'VIR', 'TGO', 'TJK', 'VNM', 'THA', 'VUT', 'YEM', 'TUN', 'TZA',
       'UGA', 'UKR', 'URY', 'UZB', 'ZMB', 'ZWE']])
   worldbank_df[['ABW', 'ASM', 'BEL', 'BRB', 'AFG', 'BRN', 'ALB', 'AND', 'AGO',
       'CUW', 'DMA', 'GIN', 'GRD', 'ARG', 'ARM', 'ATG', 'AUT', 'AUS',
       'AZE', 'BDI', 'BFA', 'BGR', 'BHR', 'BHS', 'BLR', 'BLZ', 'BMU',
       'BEN', 'BGD', 'BTN', 'BIH', 'CAN', 'CHI', 'BOL', 'BRA', 'CHN',
       'CPV', 'CUB', 'CYM', 'BWA', 'CAF', 'DZA', 'HRV', 'KHM', 'TCD',
       'VGB', 'CHL', 'COD', 'CIV', 'COG', 'COM', 'COL', 'CYP', 'CZE',
       'DEU', 'CRI', 'DJI', 'DNK', 'ECU', 'ERI', 'FIN', 'FJI', 'FRA',
       'FRO', 'GIB', 'DOM', 'ETH', 'EGY', 'GNQ', 'EST', 'GRC', 'GRL',
       'GAB', 'GHA', 'GEO', 'GMB', 'GNB', 'GTM', 'GUM', 'HTI', 'JPN',
       'GUY', 'NOR', 'HKG', 'XKX', 'HND', 'HUN', 'IMN', 'IDN', 'IND',
       'IRL', 'IRQ', 'IRN', 'ISL', 'ISR', 'JAM', 'JOR', 'ITA', 'PYF',
       'SLV', 'SWZ', 'FSM', 'KAZ', 'KIR', 'KOR', 'LBN', 'LBR', 'LBY',
       'LIE', 'LSO', 'LTU', 'LUX', 'LVA', 'KEN', 'KGZ', 'MAC', 'MCO',
       'KWT', 'LAO', 'MDV', 'MEX', 'MHL', 'MAR', 'MLI', 'MMR', 'MNE',
       'MDA', 'MNP', 'MDG', 'MOZ', 'MWI', 'NAM', 'NCL', 'MKD', 'NER',
       'NGA', 'NIC', 'NLD', 'MLT', 'NPL', 'OMN', 'PRK', 'MNG', 'MRT',
       'MUS', 'KNA', 'LCA', 'MAF', 'MYS', 'NZL', 'PAK', 'ESP', 'LKA',
       'PAN', 'PER', 'PHL', 'PLW', 'SYC', 'PNG', 'POL', 'PRI', 'PRT',
       'QAT', 'PRY', 'RUS', 'SAU', 'SGP', 'SMR', 'ROU', 'RWA', 'SEN',
       'SLB', 'SOM', 'SLE', 'SSD', 'STP', 'SRB', 'SVK', 'SVN', 'SXM',
       'WSM', 'ARE', 'GBR', 'ZAF', 'SDN', 'SUR', 'SWE', 'TCA', 'CHE',
       'TKM', 'TLS', 'TON', 'TTO', 'TUV', 'SYR', 'USA', 'VCT', 'VEN',
       'VIR', 'TGO', 'TJK', 'VNM', 'THA', 'VUT', 'YEM', 'TUN', 'TZA',
       'UGA', 'UKR', 'URY', 'UZB', 'ZMB', 'ZWE']] = imputer.transform(worldbank_df[['ABW', 'ASM', 'BEL', 'BRB', 'AFG', 'BRN', 'ALB', 'AND', 'AGO',
       'CUW', 'DMA', 'GIN', 'GRD', 'ARG', 'ARM', 'ATG', 'AUT', 'AUS',
       'AZE', 'BDI', 'BFA', 'BGR', 'BHR', 'BHS', 'BLR', 'BLZ', 'BMU',
       'BEN', 'BGD', 'BTN', 'BIH', 'CAN', 'CHI', 'BOL', 'BRA', 'CHN',
       'CPV', 'CUB', 'CYM', 'BWA', 'CAF', 'DZA', 'HRV', 'KHM', 'TCD',
       'VGB', 'CHL', 'COD', 'CIV', 'COG', 'COM', 'COL', 'CYP', 'CZE',
       'DEU', 'CRI', 'DJI', 'DNK', 'ECU', 'ERI', 'FIN', 'FJI', 'FRA',
       'FRO', 'GIB', 'DOM', 'ETH', 'EGY', 'GNQ', 'EST', 'GRC', 'GRL',
       'GAB', 'GHA', 'GEO', 'GMB', 'GNB', 'GTM', 'GUM', 'HTI', 'JPN',
       'GUY', 'NOR', 'HKG', 'XKX', 'HND', 'HUN', 'IMN', 'IDN', 'IND',
       'IRL', 'IRQ', 'IRN', 'ISL', 'ISR', 'JAM', 'JOR', 'ITA', 'PYF',
       'SLV', 'SWZ', 'FSM', 'KAZ', 'KIR', 'KOR', 'LBN', 'LBR', 'LBY',
       'LIE', 'LSO', 'LTU', 'LUX', 'LVA', 'KEN', 'KGZ', 'MAC', 'MCO',
       'KWT', 'LAO', 'MDV', 'MEX', 'MHL', 'MAR', 'MLI', 'MMR', 'MNE',
       'MDA', 'MNP', 'MDG', 'MOZ', 'MWI', 'NAM', 'NCL', 'MKD', 'NER',
       'NGA', 'NIC', 'NLD', 'MLT', 'NPL', 'OMN', 'PRK', 'MNG', 'MRT',
       'MUS', 'KNA', 'LCA', 'MAF', 'MYS', 'NZL', 'PAK', 'ESP', 'LKA',
       'PAN', 'PER', 'PHL', 'PLW', 'SYC', 'PNG', 'POL', 'PRI', 'PRT',
       'QAT', 'PRY', 'RUS', 'SAU', 'SGP', 'SMR', 'ROU', 'RWA', 'SEN',
       'SLB', 'SOM', 'SLE', 'SSD', 'STP', 'SRB', 'SVK', 'SVN', 'SXM',
       'WSM', 'ARE', 'GBR', 'ZAF', 'SDN', 'SUR', 'SWE', 'TCA', 'CHE',
       'TKM', 'TLS', 'TON', 'TTO', 'TUV', 'SYR', 'USA', 'VCT', 'VEN',
       'VIR', 'TGO', 'TJK', 'VNM', 'THA', 'VUT', 'YEM', 'TUN', 'TZA',
       'UGA', 'UKR', 'URY', 'UZB', 'ZMB', 'ZWE']])
   y = worldbank_df.head(10)


   return render_template("index.html", data1=x.to_html(), data2=y.to_html())

if __name__ == "__main__":
   app.run(debug=False)