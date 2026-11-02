"""Part one demo: reading environment variables.
Run it three ways (macOS/Linux shown; Windows PowerShell: $env:WEATHER_API_KEY = "sk-demo-9f2c"):
    python3.14 00_env_vars.py                                  -> KeyError: 'WEATHER_API_KEY'
    export WEATHER_API_KEY=sk-demo-9f2c && python3.14 00_env_vars.py
    CITY=Alexandria DAYS=5 python3.14 00_env_vars.py
or with a .env file:  uv run --env-file .env.example 00_env_vars.py   (after filling in the values)"""
import os

city = os.environ.get("CITY", "Cairo")          # a default if unset
days = int(os.environ.get("DAYS", "3"))         # always str: convert
key = os.environ["WEATHER_API_KEY"]             # required
print(f"{days}-day forecast for {city}, key ends in ...{key[-4:]}")
