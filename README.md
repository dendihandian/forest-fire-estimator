# Forest Fire Estimator

## Requirement

- Anaconda (for model training & development)
- Python 3.9 (for venv and production)

## Development

### Setup

Import and create a new conda environment from `environment.yml`:

```
conda env create -f environment.yml
```

activate the new created environment:

```
conda activate forest-fire-estimator
```

### Running Streamlit Server

In the conda terminal, go to the project directory and execute the command:

```
streamlit run streamlit/app.py
```

## Deployment

Export the updated environment:

```
conda env export > environment.yml --no-builds
```

create `requirements.txt` if required:

```
pip list --format=freeze > requirements.txt
```

## Note

At the current streamlit deployment, these packages need to be removed to succeed the build:

```
- vc=14.2
- vs2015_runtime=14.27.29016
- wincertstore=0.2
```