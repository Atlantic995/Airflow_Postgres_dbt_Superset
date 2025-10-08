FROM apache/airflow:3.0.0

# 🏆 Install ALL required Python packages and providers 🏆
RUN pip install --no-cache-dir \
    apache-airflow-providers-postgres \
    requests \
    httpx \
    # Add any other libraries your DAGs or Python code need (e.g., dbt-core)
    dbt-core