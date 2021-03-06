from bq_helper import BigQueryHelper
# install this https://github.com/SohierDane/BigQuery_Helper

import os
# Google Credentials Path json file.
# https://youtu.be/iolQX4XJN2A?t=65
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".kaggle/endless-beach-228506-b15de187c224.json"

bq_assistant = BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="chicago_crime")
print(bq_assistant.list_tables())
print(bq_assistant.table_schema("crime"))
dataset = bq_assistant.dataset
tables = list(bq_assistant.list_tables())

print(len(tables))
num_tables = len(tables)
