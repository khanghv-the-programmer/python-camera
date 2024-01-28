from sqlalchemy import create_engine
from model import Users, Captures, Cameras, Events
from Utilize import DBConnection
from Utilize.ReadConfigurationFile import read_config_from_file as config
import urllib

CONN_URI = config.connection["postgres"]
PASSWORD = config.connection["postgres_password"]
DATABASE = config.connection["postgres_database"]
SCHEMA = config.schema["postgres_schema"]
CONN_STR = CONN_URI.format(password=urllib.parse.quote(PASSWORD),database=DATABASE)

postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})

try:
    with DBConnection(postgresql_engine) as session:
        users = session.query(Users).all()
        for user in users:
            print(user.id, user.full_name, user.username, user.password, user.isactive)
except Exception as E:
    raise E

