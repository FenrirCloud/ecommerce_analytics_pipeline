import os
from dotenv import load_dotenv
from google.cloud import storage, bigquery

# --- CONFIGURATION ---
load_dotenv()
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
DATASET_ID = os.getenv("BIGQUERY_DATASET_ID")
LOCAL_DATA_DIR = "data_ecommerce"

storage_client = storage.Client(project=PROJECT_ID)
bigquery_client = bigquery.Client(project=PROJECT_ID)

def upload_and_load_csvs():
    """Uploads all CSVs from a local dir to GCS, then loads them into BigQuery."""
    bucket = storage_client.get_bucket(BUCKET_NAME)
    
    # Iterate through each CSV file in our local data directory
    for filename in os.listdir(LOCAL_DATA_DIR):
        if filename.endswith('.csv'):
            local_path = os.path.join(LOCAL_DATA_DIR, filename)
            table_id = filename.replace('.csv', '') # Table name will be the filename
            
            # --- Upload to GCS ---
            blob = bucket.blob(f"raw/{filename}")
            blob.upload_from_filename(local_path)
            gcs_uri = f"gs://{BUCKET_NAME}/raw/{filename}"
            print(f"Successfully uploaded {filename} to {gcs_uri}")
            
            # --- Load into BigQuery ---
            table_ref = bigquery_client.dataset(DATASET_ID).table(table_id)
            job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.CSV,
                # BigQuery can auto-detect the schema from the CSV header
                autodetect=True,
                # Skip the header row
                skip_leading_rows=1,
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            )
            
            load_job = bigquery_client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
            print(f"Starting job to load {filename} into BigQuery table {table_id}...")
            
            load_job.result() # Wait for the job to complete
            print(f"Successfully loaded {filename} into BigQuery.")

if __name__ == "__main__":
    upload_and_load_csvs()