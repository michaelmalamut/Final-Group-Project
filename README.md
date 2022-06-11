# Projecting Life Expectacy Rates - Final Group Project
## Members and Roles
| Name | Week 1 | Week 2 | Week 3 | Week 4 |
| --- |  --- | --- | --- | --- |
| John Curran | Circle ||||
| Michael Malamut | Square |||
| Rudy Tresvalles | Circle/Triangle ||||
| Vince LaVecchia | Triangle ||||
</br>

## Project Summary

[TBD]

## Proposal
Determining the mean life expectancy rate for a country based on certain features and growth inhibitors.

## Methodology

[TBD]

## Supplements
[TBD]

## Database Mockup
![database_mockup](https://user-images.githubusercontent.com/97328622/173137861-e0658876-c653-4316-ba57-99cbcd52f648.png)

## Github Repo
https://github.com/michaelmalamut/Final-Group-Project (repo name and link will be changed at a future date)

## Machine Learning Model
Datasets: World Bank API Datasets

Data Cleanup Proccess: Obtaining relevant country and yearly info, dropping factors that have incomplete yearly values, aggregating timespan means of factors from available data, combining all countries and factored means into dataset, eliminiating factors non-existant across all countries, performing analysis on surviving data.

Algorithm: Analyzing life expectancy against multiple positive and negative factors that a country measures yearly.

Questions To Answer: What country has the best life expectancy, and what factors contribute to that? How can factors can be used to accurately project a country's life expectancy rate?

## Worldbank API Datasets
[Afghanistan to Cuba](https://data.worldbank.org/?locations=AF-AL-DZ-AS-AD-AO-AG-AR-AM-AW-AU-AT-AZ-BS-BH-BD-BB-BY-BE-BZ-BJ-BM-BT-BO-BA-BW-BR-VG-BN-BG-BF-BI-CV-KH-CA-KY-CF-TD-JG-CL-CN-CO-KM-CG-CD-CR-CI-HR-CU), [Curacao to Jordan](https://data.worldbank.org/?locations=CW-CY-CZ-DK-DJ-DM-DO-EC-EG-SV-GQ-ER-EE-SZ-ET-FO-FJ-FI-FR-PF-GA-GM-GE-DE-GH-GI-GR-GL-GD-GU-GT-GN-GW-GY-HT-HN-HK-HU-IS-IN-ID-IR-IQ-IE-IM-IL-IT-JM-JP-JO), [Kazakhstan to Pakistan](https://data.worldbank.org/?locations=KZ-KR-KP-KE-KW-KI-XK-KG-LA-LB-LR-LI-LU-LV-LS-LY-LT-MO-MW-MY-MG-MV-ML-MR-MU-MT-MH-MX-FM-MD-MC-MN-ME-MA-MM-MZ-NA-NP-NC-NI-NG-NZ-MP-NL-NE-MK-NO-OM-PK), [Palau to St. Martin](https://data.worldbank.org/?locations=PW-PA-PG-PY-PE-PH-PL-PT-PR-QA-RO-RU-RW-WS-SM-ST-SA-SN-RS-SC-SL-SG-SX-SK-SI-SB-SO-ZA-SS-ES-LK-KN-LC-MF), and [St. Vincent to Zimbabwe](https://data.worldbank.org/?locations=VC-SD-SR-SE-CH-SY-TJ-TZ-TH-TL-TG-TO-TT-TN-TM-TC-TV-UG-UA-AE-GB-US-UY-UZ-VU-VE-VN-VI-YE-ZM-ZW)
