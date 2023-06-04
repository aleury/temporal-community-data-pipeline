# What
This is a data pipeline built with [temporal.io](https://temporal.io/). It fetches the latest posts from the Temporal Community forum.

Learn how to build this at https://learn.temporal.io/tutorials/python/data-pipelines

# How

## Setup
Ensure you have `poetry` installed and run the following to install the dependencies and activate the virtial environment:

```bash
$ poetry install

$ poetry shell
```

Read the following for how to setup a temporal server in your development environment:
https://learn.temporal.io/getting_started/python/dev_environment/

When you're ready, run the following to start the Temporal server.

```bash
$ temporal server start-dev
```

## Run
Start a worker in one terminal window:
```bash
$ python run_worker.py
```

Then run the workflow in another:
```bash
$ python run_workflow.py
```


