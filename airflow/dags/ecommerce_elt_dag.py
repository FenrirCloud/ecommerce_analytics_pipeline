from __future__ import annotations
from airflow.models.dag import DAG
import pendulum
from airflow.operators.bash import BashOperator

PLUGINS_DIR = "/home/airflow/gcs/plugins"
DAGS_DIR = "/home/airflow/gcs/dags"
DBT_PROJECT_DIR = f"{PLUGINS_DIR}/ecommerce_transforms"

DBT_COMMAND = f"""
# Create a temporary virtual environment
python -m venv dbt_venv &&
# Activate it
source dbt_venv/bin/activate &&
# Install dbt packages from its own requirements file
pip install --no-cache-dir -r requirements.txt &&
# Run dbt
dbt run &&
# Deactivate and clean up
deactivate
"""

with DAG(
    dag_id="ecommerce_daily_elt_pipeline",
    start_date=pendulum.datetime(2025, 8, 27, tz="UTC"),
    schedule_interval="@daily", 
    catchup=False,
    tags=["ecommerce", "elt"],
) as dag:
    
    task_upload = BashOperator(
        task_id="upload_ecommerce_data_to_gcs_and_bigquery",
        bash_command=f"python {PLUGINS_DIR}/src/upload_ecommerce_to_gcp.py",
        env={"DOTENV_PATH": f"{DAGS_DIR}/.env"}
    )
    
    task_transform = BashOperator(
        task_id="transform_ecommerce_data_with_dbt",
        bash_command=DBT_COMMAND,
        cwd=DBT_PROJECT_DIR,
        env={"GCP_PROJECT_ID": "{{ var.value.get('gcp_project_id') }}"}
    )

    task_upload >> task_transform