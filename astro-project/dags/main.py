from airflow.decorators import dag, task
from datetime import datetime

@task
def primeira_dag():
    print("Iniciando uma tarefa do Airflow!")

@dag(
    dag_id='first_airflow_dag',
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
    default_args={'owner': 'airflow', 'retries': 1},
)
def inicial_airflow_dag():
    hello_world_task = primeira_dag()

inicial_airflow_dag()
