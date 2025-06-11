from airflow.decorators import dag
from plugins.operators.createBucketOperator import createBucketOperator
from plugins.operators.loadDataToLandingBucketOperator import loadDataToLandingBucketOperator
from datetime import datetime

ACCESS_KEY = "URCG1V25AA6J5HCNIA2B"
SECRET_KEY = "MmjcbAWDPTSucguaOCdqcjKdpn+gDSj20bRK5ha2" 
ENDPOINT_URL = "http://minio:9000"

# Define the DAG
@dag(
    dag_id = "meda_pipeline", 
    start_date = datetime(2021, 10, 10),
    catchup = False
)
def generate_dag(): 
    create_landing_bukcet = createBucketOperator(
        task_id = "create_landing_bucket",
        bucket_name = "landing", 
        access_key = ACCESS_KEY, 
        secret_key = SECRET_KEY, 
        endpoint_url = ENDPOINT_URL
    )

    create_bronze_bukcet = createBucketOperator(
        task_id = "create_bronze_bucket",
        bucket_name = "bronze", 
        access_key = ACCESS_KEY, 
        secret_key = SECRET_KEY, 
        endpoint_url = ENDPOINT_URL
    )

    create_silver_bukcet = createBucketOperator(
        task_id = "create_silver_bucket",
        bucket_name = "silver", 
        access_key = ACCESS_KEY, 
        secret_key = SECRET_KEY, 
        endpoint_url = ENDPOINT_URL
    )

    create_gold_bukcet = createBucketOperator(
        task_id = "create_gold_bucket",
        bucket_name = "gold", 
        access_key = ACCESS_KEY, 
        secret_key = SECRET_KEY, 
        endpoint_url = ENDPOINT_URL
    )

    load_raw_data = loadDataToLandingBucketOperator(
        task_id = "loadl_raw_data",
        bucket_name = "landing", 
        object_path = "include/data/invoices.csv", 
        object_name = "invoices.csv",
        access_key = ACCESS_KEY, 
        secret_key = SECRET_KEY, 
        endpoint_url = ENDPOINT_URL
    )

    create_landing_bukcet >> [create_bronze_bukcet, create_silver_bukcet, create_gold_bukcet] >> load_raw_data

generate_dag()