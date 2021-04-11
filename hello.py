from azureml.pipeline.core import Schedule
from azureml.core.datastore import Datastore

   datastore = Datastore(workspace="Playground", name="workspaceblobstore")

   schedule = Schedule.create(workspace, name="TestSchedule", pipeline_id="41858f09-dc0a-4191-a97f-de963fa277ca"
                              experiment_name="working version", datastore=datastore,
                              polling_interval=25, path_on_datastore="file/path")
