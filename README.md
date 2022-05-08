# Forest Fire Estimator

## Requirement

- Anaconda (not a 🐍)

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

create `requirements.txt`:

```
pip list --format=freeze > requirements.txt
```