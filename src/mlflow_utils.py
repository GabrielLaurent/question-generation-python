import mlflow
import os

def setup_mlflow(experiment_name, run_name=None):
    mlflow.set_experiment(experiment_name)
    if run_name:
      run = mlflow.start_run(run_name=run_name)
    else:
      run = mlflow.start_run()

    return run.info.run_id


def log_param(param_name, param_value):
    mlflow.log_param(param_name, param_value)


def log_metric(metric_name, metric_value):
    mlflow.log_metric(metric_name, metric_value)

def log_artifact(local_path, artifact_path=None):
    mlflow.log_artifact(local_path, artifact_path)