# Task Folder Details

## Task Goals
- Experimentation for Data Labelling using Active Learning
- Steps:
  1) Write code to set up backend, frontend and database (code files above)
  2) Deploy code on AWS EC2
  3) Proceed with labelling by multiple collaborators
  4) When satisfied with performance of labelling model, retrieve labelled datapoints and their labels by exporting csv from "Adminer" port
  5) Copy volume containing trained models into local machine
  6) Write code to load trained models and apply model on remaining unlabelled datapoints
  7) Terminate code on AWS

## Information Table

| Code Files | Description |
|-|-|
| aldata | Sample data for testing (from Reddit) |
| docker-compose.yml | yml to pull and configure images |
| orchestrate.py | Set up database connection, model for training and training configurations |
| tensorflow.Dockerfile | Write image for tensorflow (to train model) |
| voila.Dockerfile | Write image for voila (for frontend) |
| voila-interface.ipynb | Frontend design code |
