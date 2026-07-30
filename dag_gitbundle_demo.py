"""Demo DAG for the GitDagBundle EKS pilot.

This file lives in a public git repo and reaches the Airflow server ONLY via
the dag-processor's git clone (GitDagBundle) - there is no S3 sync on that
server. Each DAG run is pinned to the commit it started from: bump MARKER
mid-run and the second task should still print the original value.
"""

import time
from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

MARKER = "demo-v2"


def report(step: str) -> None:
    print(
        f"GITBUNDLE_DEMO step={step} marker={MARKER} "
        f"ts={datetime.utcnow().isoformat()}"
    )


def hold(minutes: int = 6) -> None:
    report("start")
    time.sleep(minutes * 60)


with DAG(
    dag_id="gitbundle_demo",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["demo"],
) as dag:
    first = PythonOperator(task_id="hold_six_minutes", python_callable=hold)
    second = PythonOperator(
        task_id="report_marker",
        python_callable=report,
        op_kwargs={"step": "end"},
    )
    first >> second
