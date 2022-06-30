import pandas as pd
import numpy as np
import plotly.express as px


df1 = pd.read_csv('Final-Group-Project/Resources/worldbank_all-data.csv')
df2 = pd.read_csv('Final-Group-Project/Resources/worldbank_data_postprocessed.csv')
features = df2.columns

""" countries = ['ABW', 'ASM', 'BEL', 'BRB', 'AFG', 'BRN', 'ALB', 'AND', 'AGO',
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
       'UGA', 'UKR', 'URY', 'UZB', 'ZMB', 'ZWE'] """

def main():
        
    def optionChanged(country):
        def top_features(country): 
            return
            
        def life_expectancy(country):
            df11 = df1.set_index('country_name').loc[country]
            df12 = df11.set_index('indicator_code')
            fig = px.scatter(df12.loc['SP.DYN.LE00.IN'].drop(labels=['country_code', 'indicator_name']))
            return fig.show()