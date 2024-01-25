import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
dag = DAG(
    dag_id = "fetch_data_lazlo",
    default_args = {
        "owner": "Lazlo",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval = "@daily"
)
start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)
python_job = SparkSubmitOperator(
    task_id="spark_job",
    conn_id="spark-conn",
    driver_class_path="/home/lazlo/jdbc_jars/postgresql-42.7.1.jar",
    application="/home/lazlo/airflow/dags/fetch_data_mult_tbl_app.py",
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)
start >> python_job >> end