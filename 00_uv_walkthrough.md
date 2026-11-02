# Part one live walkthrough: pip, venv and uv

Type these in a terminal during the lecture. Output shown on the slides came from Python 3.14.6 and uv 0.11.

## 1. The problem
    python3.14 -c "import requests"          # ModuleNotFoundError

## 2. pip in a virtual environment
    mkdir weather-pip && cd weather-pip
    python3.14 -m venv .venv
    source .venv/bin/activate                # Windows: .venv\Scripts\Activate.ps1
    python -c "import sys; print(sys.prefix)"
    python -m pip install requests
    python -m pip show requests              # look at Location
    python -m pip freeze > requirements.txt
    deactivate
    python3.14 -c "import requests"          # fails again: it lives only in .venv
    cd ..

## 3. The same project with uv
    uv init weather --python 3.14
    cd weather
    uv add requests                          # pyproject.toml, uv.lock and .venv appear
    cat pyproject.toml
    uv tree
    uv run main.py
    rm -rf .venv && uv sync                  # rebuilt from uv.lock in milliseconds

## 4. Environment variables
    cp ../00_env_vars.py app.py
    uv run app.py                            # KeyError: 'WEATHER_API_KEY'
    export WEATHER_API_KEY=sk-demo-9f2c      # Windows PowerShell: $env:WEATHER_API_KEY = "sk-demo-9f2c"
    uv run app.py
    CITY=Alexandria DAYS=5 uv run app.py
    printf 'WEATHER_API_KEY=sk-live-7a41\nCITY=Riyadh\n' > .env
    uv run --env-file .env app.py
    echo ".env" >> .gitignore                # uv's .gitignore does not include it

## 5. Bridge to threads: Python without the GIL
    uv python install 3.14t
    uv run --no-project --python 3.14t ../09_gil_cpu.py
    PYTHON_GIL=1 uv run --no-project --python 3.14t ../09_gil_cpu.py
