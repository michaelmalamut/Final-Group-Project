# Projecting Life Expectacy Rates - Final Group Project
## Members and Roles
| Name | Week 1 | Week 2 | Week 3 | Week 4 |
| --- |  --- | --- | --- | --- |
| John Curran | Circle | Circle |||
| Michael Malamut | Square | Square ||
| Rudy Tresvalles | Circle | Circle |||
| Vince LaVecchia | Triangle | Triangle |||

## Final Presentation
The slides deck that accompanied our final presentation can be found [here](https://docs.google.com/presentation/d/100R_4NxA1Hv28CinWRYU4MvfusqSZ3mnPtDEoqfejDk/edit?usp=sharing).

## Project Summary
[TBD]

</br>

# Methodology

## Data Pre-Processing
### Database Mockup
![database_mockup](https://user-images.githubusercontent.com/97328622/173137861-e0658876-c653-4316-ba57-99cbcd52f648.png)
Prior to pre-processing data for PCA, several steps occurred:
* Worldbank life expectancy data was pulled in segments for all present features for a subset of all countries until all of the data for all countries was collected.  This was done due to limitations on the extract of data.
* Data was combined into one file into one csv

### Worldbank API Datasets
[Afghanistan to Cuba](https://data.worldbank.org/?locations=AF-AL-DZ-AS-AD-AO-AG-AR-AM-AW-AU-AT-AZ-BS-BH-BD-BB-BY-BE-BZ-BJ-BM-BT-BO-BA-BW-BR-VG-BN-BG-BF-BI-CV-KH-CA-KY-CF-TD-JG-CL-CN-CO-KM-CG-CD-CR-CI-HR-CU), [Curacao to Jordan](https://data.worldbank.org/?locations=CW-CY-CZ-DK-DJ-DM-DO-EC-EG-SV-GQ-ER-EE-SZ-ET-FO-FJ-FI-FR-PF-GA-GM-GE-DE-GH-GI-GR-GL-GD-GU-GT-GN-GW-GY-HT-HN-HK-HU-IS-IN-ID-IR-IQ-IE-IM-IL-IT-JM-JP-JO), [Kazakhstan to Pakistan](https://data.worldbank.org/?locations=KZ-KR-KP-KE-KW-KI-XK-KG-LA-LB-LR-LI-LU-LV-LS-LY-LT-MO-MW-MY-MG-MV-ML-MR-MU-MT-MH-MX-FM-MD-MC-MN-ME-MA-MM-MZ-NA-NP-NC-NI-NG-NZ-MP-NL-NE-MK-NO-OM-PK), [Palau to St. Martin](https://data.worldbank.org/?locations=PW-PA-PG-PY-PE-PH-PL-PT-PR-QA-RO-RU-RW-WS-SM-ST-SA-SN-RS-SC-SL-SG-SX-SK-SI-SB-SO-ZA-SS-ES-LK-KN-LC-MF), and [St. Vincent to Zimbabwe](https://data.worldbank.org/?locations=VC-SD-SR-SE-CH-SY-TJ-TZ-TH-TL-TG-TO-TT-TN-TM-TC-TV-UG-UA-AE-GB-US-UY-UZ-VU-VE-VN-VI-YE-ZM-ZW)

### Scaling the Data
* Here we will need to load, clean up, and scale the dataset. Current cleanup steps we can determine are:
    * Obtain relevant country and yearly info.
    * Drop factors that have incomplete yearly values.
    * Aggergate timespam means of factors from available data.
    * Eliminate features that do not apply to all countries.
    * Remove features that do not have hardy data.
    * Rationalize certain features where data does not exist.

</br>

## Creating the PCA
[TBD]

</br>

## Machine Learning Model
Datasets: World Bank API Datasets

Algorithm: Analyzing life expectancy against multiple positive and negative factors that a country measures yearly.

Questions To Answer: What country has the best life expectancy, and what factors contribute to that? How can factors can be used to accurately project a country's life expectancy rate?

## RDS
