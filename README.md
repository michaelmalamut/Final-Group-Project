# Final-Group-Project
Rutgers Boot Camp group project

## DATA SCI-VIZ FIRST SEGMENT PROPOSAL
John Curran, Michael Malamut, Vince LaVecchia, Rudy Tresvalles

## PROPOSAL
Determining the mean life expectancy rate for a country based on certain features and growth inhibitors.

## DATABASE MOCKUP
![database_mockup](https://user-images.githubusercontent.com/97328622/173137861-e0658876-c653-4316-ba57-99cbcd52f648.png)


## GITHUB REPO
https://github.com/michaelmalamut/Final-Group-Project (repo name and link will be changed at a future date)

## MACHINE LEARNING MODEL
### DATASET
World Bank API Datasets

### DATA CLEANUP
Obtaining relevant country and yearly info

### ALGORITHM
Analyzing life expectancy against multiple factors

### PREDICTION
Life Expectancy Rate Output

## WORLDBANK DATASETS
Afghanistan to Cuba: https://data.worldbank.org/?locations=AF-AL-DZ-AS-AD-AO-AG-AR-AM-AW-AU-AT-AZ-BS-BH-BD-BB-BY-BE-BZ-BJ-BM-BT-BO-BA-BW-BR-VG-BN-BG-BF-BI-CV-KH-CA-KY-CF-TD-JG-CL-CN-CO-KM-CG-CD-CR-CI-HR-CU

Curacao to Jordan:
https://data.worldbank.org/?locations=CW-CY-CZ-DK-DJ-DM-DO-EC-EG-SV-GQ-ER-EE-SZ-ET-FO-FJ-FI-FR-PF-GA-GM-GE-DE-GH-GI-GR-GL-GD-GU-GT-GN-GW-GY-HT-HN-HK-HU-IS-IN-ID-IR-IQ-IE-IM-IL-IT-JM-JP-JO

Kazakhstan to Pakistan: https://data.worldbank.org/?locations=KZ-KR-KP-KE-KW-KI-XK-KG-LA-LB-LR-LI-LU-LV-LS-LY-LT-MO-MW-MY-MG-MV-ML-MR-MU-MT-MH-MX-FM-MD-MC-MN-ME-MA-MM-MZ-NA-NP-NC-NI-NG-NZ-MP-NL-NE-MK-NO-OM-PK

Palau to Zimbabwe:
https://data.worldbank.org/?locations=PW-PA-PG-PY-PE-PH-PL-PT-PR-QA-RO-RU-RW-WS-SM-ST-SA-SN-RS-SC-SL-SG-SX-SK-SI-SB-SO-ZA-SS-ES-LK-KN-LC-MF-VC-SD-SR-SE-CH-SY-TJ-TZ-TH-TL-TG-TO-TT-TN-TM-TC-TV-UG-UA-AE-GB-US-UY-UZ-VU-VE-VN-VI-YE-ZM-ZW

# Prior to Pre-Processing

Prior to pre-processing data for PCA, several steps occurred:

* Worldbank life expectnacy data was pulled in segments for all present features for a subset of all countries until all of the data for all countries was collected.  This was done due to limitations on the extract of data.
* Data was combined into one file into one csv

# Preprocessing the Data for PCA
* Here we will need load, clean up, and scale the dataset
* Current cleanup steps we can determine are:
    * Remove features that do not apply to all countries
    * Focus on a subset of more recent years (maybe from 2010) forward as data is more prevalent in those years
    * Remove features that do not have hardy data
    * Determine if we should rationalize certain features where data does not exist
    * Group data by years then take the mean so that data is one value per feature

