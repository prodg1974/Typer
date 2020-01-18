import os
import logging
from pathlib import Path

import typer
from dotenv import load_dotenv, find_dotenv
import sqlalchemy as sa

logging.basicConfig(level=logging.DEBUG)

home = Path.home()
env_path = Path(home,'.env')
logging.debug(f'dotenv_path: {env_path}')

load_dotenv(env_path,verbose=True)
pg_password = os.environ.get('POSTGRES_PASSWORD')
logging.debug(f'pg_password: {pg_password}')
engine = sa.create_engine(f'postgresql://postgres:{pg_password}@localhost:5432/postgres')
engine.execute("select 1")

def hello(name:str):
    pass
