import dagshub
import mlflow
dagshub.init(repo_owner='saiprem-eng', repo_name='mlops', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/saiprem-eng/mlops.mlflow")
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)