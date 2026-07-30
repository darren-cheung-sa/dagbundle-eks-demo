# dagbundle-eks-demo

Tiny public repo used to demonstrate Airflow 3 GitDagBundle on StackAdapt's
EKS Airflow dev servers: the dag-processor pod clones this repo over HTTPS
(no credentials, no S3 sync) and DAG runs are pinned to the commit they
started from. Safe to delete after the pilot.
