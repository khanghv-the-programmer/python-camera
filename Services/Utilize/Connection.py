from sqlalchemy.orm import sessionmaker
from traceback import print_exc
class DBConnection:
    def __init__(self,engine):
        self.engine = engine
        self.session = None

    def __enter__(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self.session
    def __exit__(self, exception_type, exception_value, exception_traceback):
        try:
            if exception_value:  # This is equivalent to `if exception_value is not None`
                self.session.rollback()
            else:
                # self.session.commit()
                self.session.close()

        except Exception as e:
            print_exc("Exception %s", e)
        finally:
            self.session.close()

