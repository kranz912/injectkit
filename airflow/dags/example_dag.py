from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.insert(0, '/opt/airflow/dags/injectkit')

from app.container import injector
from app.services.user_service import UserService

def greet_task():
    service = injector.get(UserService)
    print(service.greet_user("Kranz from Airflow"))

with DAG(
    "injectkit_mwaa_test",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="greet",
        python_callable=greet_task
    )
