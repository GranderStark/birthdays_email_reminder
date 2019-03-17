import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class App:
    config = None
    db = None

    def __init__(self):

        self.read_config()
        self.db_engine = create_engine(self.config['db']['url'])
        self.db_session = scoped_session(sessionmaker(bind=self.db_engine))

    def read_config(self):
        with open('conf.yaml', 'r', encoding='utf-8') as f:
            self.config = yaml.load(f)

    def process(self):
        pass