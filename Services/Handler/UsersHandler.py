from Services.model import Users
from sqlalchemy import and_
from Services.Utilize import DBConnection
import pandas as pd
from sqlalchemy.dialects import postgresql
class UsersHandler:
    def __init__(self,engine=None,session=None):
        self.engine=engine
        self.session=session
    def getUser(self,condition=None):
        try:
            if condition == None:
                condition = []
                condition.append(1==1)
            with DBConnection(self.engine) as session:
                query = session.query(Users.id,
                                    Users.full_name,
                                    Users.username,
                                    Users.password,
                                    Users.isactive)\
                    .filter(and_(*condition))
                query_stm = str(query.statement.compile(compile_kwargs={"literal_binds": True},
                                                            dialect=postgresql.dialect()))
                data = pd.read_sql_query(query.statement,session.bind)
        except Exception as E:
            raise E
        return data

    def bulkInsertUser(self,users):
        try:
            with DBConnection(self.engine) as session:
                session.bulk_save_objects(users, return_defaults=True)
                session.commit()
        except Exception as E:
            raise E
    def insertUser(self,data):
        try:
            instance_user = []
            # for key, value in data.items():
            user_name = data['user_name']
            full_name = data['full_name']
            password = data['password']
            user = Users(username=user_name, full_name=full_name, password=password)
            instance_user.append(user)
            self.bulkInsertUser(instance_user)
        except Exception as E:
            raise E


