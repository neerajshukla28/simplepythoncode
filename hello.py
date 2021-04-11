from azureml.pipeline.core import Schedule
from azureml.core.datastore import Datastore

   datastore = Datastore(workspace="Playground", name="workspaceblobstore")

   schedule = Schedule.create(workspace, name="TestSchedule", pipeline_id="3100e87c-3300-400b-a5a5-470e85a100b3"
                              experiment_name="working version", datastore=datastore,
                              polling_interval=25, path_on_datastore="file/path")
