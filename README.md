# dlt-slack-channel-export
This repo is a PoC of how to use the [dlt](https://dlthub.com/docs/dlt-ecosystem/verified-sources/slack) python library to extract Slack channel message & reply history from a given channel. 

It addresses some flaws in the initialized solution created by running `dlt init slack duckdb`. The primary issue being conversation replies weren't being captured by the pipeline. The changes are obvious - I just commented out the old code and put in the fixes immediately below. Only the `slack/__init__.py` file was modified. 

The `slack_pipeline.py` was created by default - not super useful, but kept as a reference. 

The real implementation is in the [dlt-slack-export.ipynb](./dlt-slack-export.ipynb) file. 

# Setup
Create a conda environment: `conda create -n dlt-slack-channel-export`

Activate conda environment: `conda activate dlt-slack-channel-export`

Install dependencies: `pip install -r requirements.txt`

This assumes that you've already set up a Slack app. Check out the dlt instructions [here](https://dlthub.com/docs/dlt-ecosystem/verified-sources/slack#grab-user-oauth-token) for reference. 

Copy `.dlt/secrets_template.toml` to `.dlt/secrets.toml` and update it to include your app token.
