    
<div align="center">
  <h1>End-to-End E-commerce Analytics Pipeline</h1>
  <p>
    An end-to-end ELT pipeline for the Olist E-commerce dataset using Python, Google Cloud (GCS, BigQuery), dbt, and Apache Airflow for orchestration.
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud">
    <img src="https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white" alt="BigQuery">
    <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" alt="dbt">
    <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white" alt="Airflow">
  </p>
</div>

<hr>

### 🏛️ Project Architecture
The pipeline follows a modern data stack architecture, separating the Extract, Load, and Transform stages. This diagram illustrates the flow of data from local files to transformed, analysis-ready tables in the cloud.

```mermaid
graph TD;
    A["Raw CSV Files<br>(Local Machine)"] --> B("Python Script<br>upload_ecommerce_to_gcp.py");
    B --> C{"Google Cloud Storage<br>(Landing Zone)"};
    C --> D["BigQuery<br>(Raw Tables)"];
    D --> E("dbt Core<br>(Transformation Engine)");
    E --> F["BigQuery<br>(Transformed Models)"];

  

<hr>
<br>
<details>
<summary>
<h3>✨ View Key Features</h3>
</summary>

This project includes all the key components of a modern data pipeline:
<ul>
<li><strong>🚚 Extraction & Loading:</strong> A robust Python script handles the upload of multiple raw CSV files to Google Cloud Storage and then loads them into raw BigQuery tables.</li>
<li><strong>🔄 Data Transformation:</strong> A comprehensive dbt project transforms the raw data into a clean, modular, and well-documented data model.</li>
<li><strong>✅ Data Quality:</strong> The dbt project includes data tests to ensure data integrity and reliability (e.g., <code>not_null</code>, <code>unique</code>, <code>accepted_values</code>).</li>
<li><strong>✈️ Automation-Ready:</strong> Includes a complete Airflow DAG (<code>ecommerce_elt_dag.py</code>) ready for deployment to an orchestrator like Cloud Composer.</li>
</ul>
</details>
<details>
<summary>
<h3>🛠️ View Tech Stack</h3>
</summary>
<!-- Using an HTML table for guaranteed rendering -->
<table>
<tbody>
<tr>
<td width="150px"><strong>Cloud Provider</strong></td>
<td><img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud"></td>
</tr>
<tr>
<td><strong>Data Warehouse</strong></td>
<td><img src="https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white" alt="BigQuery"></td>
</tr>
<tr>
<td><strong>Ingestion</strong></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Google_Cloud_Storage-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="GCS">
</td>
</tr>
<tr>
<td><strong>Transformation</strong></td>
<td><img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" alt="dbt"></td>
</tr>
<tr>
<td><strong>Orchestration</strong></td>
<td><img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white" alt="Airflow"></td>
</tr>
</tbody>
</table>
</details>
<details>
<summary>
<h3>🚀 How to Run Locally</h3>
</summary>
Prerequisites

    Python 3.9+

    A Google Cloud Platform account with billing enabled.

    The gcloud CLI installed and authenticated (gcloud auth application-default login).

    The dbt CLI installed.

1. Clone the Repository
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
git clone <your-repo-url>
cd ecommerce-analytics-pipeline

  

2. Set Up the Environment

Create and activate a virtual environment:
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
python -m venv venv
.\venv\Scripts\activate

  

Install the required packages:
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
pip install -r requirements.txt

  

3. Configure Your Credentials

Create a .env file in the root of the project and populate it with your GCP details:
code Env
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
# .env.example
GCP_PROJECT_ID="your-gcp-project-id"
GCS_BUCKET_NAME="your-gcs-bucket-name"
BIGQUERY_DATASET_ID="ecommerce_analytics"

  

Also, configure your profiles.yml file for dbt located at ~/.dbt/profiles.yml:
code Yaml
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
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

  

4. Run the Pipeline Manually

Execute the scripts in order from the project root directory.

Step A: Load the raw data into BigQuery
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
python airflow/plugins/src/upload_ecommerce_to_gcp.py

  

Step B: Run the dbt transformations
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
dbt run --project-dir airflow/plugins/ecommerce_transforms

  

Step C (Optional): Run the dbt tests
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

    
dbt test --project-dir airflow/plugins/ecommerce_transforms

  

</details>
<details>
<summary>
<h3>🔮 Future Work</h3>
</summary>

    Deploy Orchestration: The final step for this project is to deploy the included Airflow DAG to a managed service like Cloud Composer to achieve full daily automation.

    Data Visualization: Connect a BI tool like Looker Studio, Tableau, or Superset to the final dim_customers table in BigQuery to build an interactive analytics dashboard.

    Machine Learning: Use the clean customer data to build predictive models, such as predicting customer churn or forecasting lifetime value.

</details>
```
