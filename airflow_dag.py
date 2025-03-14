from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pipeline

defalut_args = {
    'start_date': datetime(2024,1,1),
    'catchup': False
}

dag = DAG("data_pipeline_dag" , default_args=default_args, schedule_interval="@daily")

load_task = PythonOperator(

    task_id = "load_data"
    python_callable = pipeline.load_data,
    op_kwargs = {"file_path": "data/orders.csv"}
    dag=dag
)

clean_task = PythonOperator(
    task_id = "clean_data",
    python_callable = pipeline.clean_data,
    dag=dag
)

save_task = PythonOperator(

    task_id = "save_data",
    python_callable = pipeline.save_data,
    op_kwargs = {"output_path":"data/cleaned_orders.csv"},
    dag=dag
)

load_task >> clean_task >> save_task
