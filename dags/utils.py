from airflow.models.variable import Variable

import os

class Config:
    RDB_NAME = Variable.get("RDB_NAME")
    VECTOR_DB_NAME = Variable.get("VECTOR_DB_NAME")
    DB_USER = Variable.get("DB_USER")
    DB_PASSWORD = Variable.get("DB_PASSWORD")
    DB_HOST = Variable.get("DB_HOST")
    DB_PORT = Variable.get("DB_PORT")

    MONGO_DB_NAME = Variable.get("MONGO_DB_NAME")
    MONGO_DB_PASSWORD = Variable.get("MONGO_DB_PASSWORD")

    REGIONS = Variable.get("REGIONS", deserialize_json=True)

    BUCKET_NAME = Variable.get("BUCKET_NAME")

    RDB_POSTGRES_CONNECTION = Variable.get("RDB_POSTGRES_CONNECTION")
    VECTOR_DB_POSTGRES_CONNECTION = Variable.get("VECTOR_DB_POSTGRES_CONNECTION")



class Directory:
    AIRFLOW_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    DOWNLOADS_DIR = os.path.join(AIRFLOW_HOME, 'download')
    TRANSFORM_DIR = os.path.join(AIRFLOW_HOME, 'transform')
    LIGHTGCN_DIR = os.path.join(AIRFLOW_HOME, 'LightGCN')
    BIENCODER_DIR = os.path.join(AIRFLOW_HOME, 'BiEncoder')

