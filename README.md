# E-Commerce Customer Churn Analysis and Prediction
## FTDS-010-HCK-group-001
**Members**:
1.  [Akram](https://github.com/AkramHuwaidiIrnawan) — Data Scientist
2.  [Carlos Emmanuel Argado](https://github.com/carlosargado)— Data Analyst
3.  [Muhammad Insani](https://github.com/muhamadinsani17)— Data Scientist
4.  [Saepul Hilal](https://github.com/saepulhilal)— Data Engineer


## Project Overview

The primary objective of this project is to develop an effective customer churn prediction system within an e-commerce setting. Through comprehensive data analysis, the project aims to identify key indicators and patterns leading to customer attrition. The insights gained from this analysis will be utilized to create machine learning models capable of predicting potential churn events. By implementing these predictive models, the project seeks to empower e-commerce businesses with proactive measures for customer retention, ultimately improving overall customer satisfaction and reducing turnover. Additionally, the project aims to optimize marketing strategies and enhance operational efficiency based on the identified patterns and customer behavior.


## Background
### Problem Statement

In the context of e-commerce, customer churn poses a significant challenge for businesses. The lack of a proactive system to predict and address customer attrition can lead to revenue loss and decreased customer satisfaction. Existing strategies often rely on reactive approaches, making it essential to develop a more anticipatory system. The project addresses the need for an effective customer churn prediction system in e-commerce by analyzing customer behavior, transactional data, and engagement patterns. The absence of such a system hinders businesses from implementing timely retention strategies and optimizing operational efforts. Thus, there is a pressing need to create predictive models that can identify potential churn, allowing businesses to implement preemptive measures and improve overall customer retention.


### Objectives

1. **Develop Predictive Models:** Create machine learning models that leverage customer behavior, transaction history, and engagement patterns to accurately predict potential customer churn within the e-commerce platform.

2. **Identify Key Indicators:** Conduct a comprehensive analysis to identify and understand the critical indicators and patterns associated with customer attrition, providing valuable insights for targeted retention strategies.

3. **Enhance Retention Strategies:** Utilize the predictive models and identified indicators to develop proactive and targeted retention strategies aimed at reducing customer churn and improving overall customer satisfaction.

4. **Optimize Marketing Efforts:** Implement insights gained from customer churn analysis to optimize marketing strategies, ensuring more effective and personalized approaches to customer engagement and loyalty.

5. **Improve Operational Efficiency:** Identify operational inefficiencies and areas for improvement within the e-commerce platform based on customer behavior and churn patterns, leading to streamlined processes and resource optimization.

6. **Evaluate Model Performance:** Regularly assess and refine the predictive models to ensure accuracy and reliability in forecasting customer churn, adapting to evolving customer trends and market dynamics.

7. **Provide Actionable Recommendations:** Translate the findings from the analysis into actionable recommendations for the e-commerce business, enabling informed decision-making and strategic planning.

8. **Measure Impact:** Quantify the impact of implemented retention strategies on reducing customer churn and increasing overall customer lifetime value, providing measurable outcomes for business success.
### Dataset
The dataset used in this project is obtained from Kaggle from [this link](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction).


## Project Structure
### Workflow
The workflow is split into 3, separated by roles:
#### Data Engineering
- **Data Collection**: Store raw data on PostgreSQL
- **Data Cleaning**: Set up Apache Airflow DAG to fetch and clean the raw data
- **Data Storage**: Store the cleaned data back into the PostgreSQL

#### Data Science
- **Model Development**: Using the cleaned data from the S3 bucket, Create a TensorFlow regression model to perform sentiment analysis 
- **Model Optimization**: Tune and optimise model

#### Data Analysis
- **Data Interpretation**: Analyse the results from the model to understand user sentiment
- **Visualization**: Create visual representations of the analysis for easier interpretation and presentation
- **Reporting**: Compile findings and insights into a comprehensive report


## Stack
- **Docker**: To containerise and package all the process done for data pipeline to ensure reproducibility
- **Apache Airflow**: For orchestrating and automating the data pipeline
- **PostgreSQL**: For data storage and retrieval
- **Scikit-learn**: For building and training the sentiment analysis model
- **Python**: Primary programming language used for data processing, analysis and modeling


## Setup and Installation
To replicate this project, there are multiple prerequisites that you need to have:
1. Docker
2. Python
3. Environment Configuration: `.env` file for the airflow containers to get access to the S3 bucket
> For security reasons, the `.env` file is included but not completed

To replicate this project assuming you have all of the prerequisites above:
1. Clone this repo
```bash
git clone https://github.com/FTDS-assignment-bay/p2-final-project-ftds-010-hck-group-001.git
```
2. Compose the containers
```bash
cd p2-final-project-ftds-010-hck-group-001
docker-compose up -d
```
3. Access the airflow webserver and setup the airflow credentials for PostgreSQL
4. Trigger the DAG
5. Download the cleaned data from PostgreSQL
6. Run the `modeling.ipynb` file to create the models

Alternatively, all the models are in the repo for you to use and we also have a deployed model on [Huggingface](https://huggingface.co/spaces/Muhamadinsani17/Churn_Prediction).


## Results


Furthermore, all of our visualisations are also available on [Tableau](https://public.tableau.com/app/profile/carlos.argado/viz/final_project_01_17049562541020/final_dashboard?publish=yes).

