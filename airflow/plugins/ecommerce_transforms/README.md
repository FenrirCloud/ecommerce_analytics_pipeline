# End-to-End E-commerce Analytics Pipeline

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white)

This project demonstrates a complete, professional ELT (Extract, Load, Transform) pipeline built to analyze the Brazilian E-commerce Public Dataset by Olist. The pipeline ingests raw CSV data, loads it into a cloud data warehouse (Google BigQuery), and transforms it into clean, analysis-ready tables using dbt.

---

## 🏛️ Project Architecture

The pipeline follows a modern data stack architecture, separating the Extract/Load and Transform stages.

```mermaid
graph TD;
    A[Raw CSV Files on Local Machine] --> B(Python Script: upload_ecommerce_to_gcp.py);
    B --> C{Google Cloud Storage};
    C --> D[BigQuery: Raw Tables];
    D --> E{dbt Core};
    E --> F[BigQuery: Transformed Tables];

Key Features

    Extraction & Loading: A robust Python script handles the upload of multiple raw CSV files to Google Cloud Storage and then loads them into raw BigQuery tables.

    Data Transformation: The dbt project transforms the raw data into a clean, modular, and well-documented data model.

        Staging Models: Cleans, casts, and renames columns from the raw sources.

        Final Model (dim_customers): Creates an advanced analytical model with one row per customer, calculating valuable KPIs like first_order_date, number_of_orders, and lifetime_value.

    Data Quality: Includes dbt tests to ensure data integrity (e.g., not_null, unique, accepted_values).

    Automation-Ready: Includes a complete Airflow DAG (ecommerce_elt_dag.py) ready for deployment to an orchestrator like Cloud Composer, which automates the entire ELT process on a daily schedule.



Tech Stack

    Cloud Provider: Google Cloud Platform (GCP)

    Data Warehouse: Google BigQuery

    Data Ingestion: Python, google-cloud-storage, google-cloud-bigquery

    Data Transformation: dbt (data build tool)

    Orchestration: Apache Airflow (DAG provided)


How to Run Locally
Prerequisites

    Python 3.9+

    A Google Cloud Platform account with billing enabled.

    The gcloud CLI installed and authenticated (gcloud auth application-default login).

    The dbt CLI installed.

1. Clone the Repository
git clone <your-repo-url>
cd ecommerce-analytics-pipeline

2. Set Up the Environment

Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate

3. Install the required packages:
    
pip install -r requirements.txt

    
4. Configure Your Credentials
Create a .env file in the root of the project and populate it with your GCP details:
    
# .env.example
GCP_PROJECT_ID="your-gcp-project-id"
GCS_BUCKET_NAME="your-gcs-bucket-name"
BIGQUERY_DATASET_ID="ecommerce_analytics"

5. Configure your profiles.yml file for dbt located at ~/.dbt/profiles.yml:

ecommerce_transforms:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: oauth
      project: your-gcp-project-id
      dataset: ecommerce_analytics
      threads: 1
      location: EU # Or your GCP location

6. Run the Pipeline Manually
Execute the scripts in order from the project root directory.

Step A: Load the raw data into BigQuery: 
    
python airflow/plugins/src/upload_ecommerce_to_gcp.py

Step B: Run the dbt transformations:
    
dbt run --project-dir airflow/plugins/ecommerce_transforms

Step C (Optional): Run the dbt tests
    
dbt test --project-dir airflow/plugins/ecommerce_transforms


🔮 Future Work

    Deploy Orchestration: The final step for this project is to deploy the included Airflow DAG to a managed service like Cloud Composer to achieve full daily automation.

    Data Visualization: Connect a BI tool like Looker Studio, Tableau, or Superset to the final dim_customers table in BigQuery to build an interactive analytics dashboard.

    Machine Learning: Use the clean customer data to build predictive models, such as predicting customer churn or forecasting lifetime value.