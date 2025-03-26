import dlt
import duckdb

from pendulum import datetime
from slack import slack_source

pipeline = dlt.pipeline(
    pipeline_name="slack", destination='duckdb', dataset_name="slack_export"
)

source = slack_source(
    page_size=20,
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2030, 12, 31),
    replies=True,
    selected_channels=['export-test'] # change this as needed
)

load_info = pipeline.run(
    source,
)
print(load_info)
