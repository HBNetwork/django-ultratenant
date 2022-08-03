# Contributing

## Rules to contribute

### Clone the code

```bash
git clone https://github.com/HBN3tw0rk/django-ultratenant
cd django-ultratenant
git checkout main
```

### Setup the project

```bash
python -m venv .venv
pip install -r requirements_dev.txt
pre-commit install
pre-commit autoupdate
pytest
```

### Create a new branch

```bash
git fetch origin
git checkout -b task/branch-name-you-work-issue
```




### Create a pull request to the branch *main*
