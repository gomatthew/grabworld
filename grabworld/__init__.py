import redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from apscheduler.schedulers.background import BackgroundScheduler
from grabworld.settings import REDIS_HOST, REDIS_PORT, REDIS_DATABASE, MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, \
    MYSQL_DBNAME, MYSQL_PORT, SQL_ECHO

Base = declarative_base()


# MySQL init
def generate_mysql_session():
    _engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DBNAME}',echo=SQL_ECHO)
    _session = sessionmaker(bind=_engine)
    s = scoped_session(_session)
    return s


def get_mysql_engine(database='spider'):
    _engine = None
    match database:
        case 'spider':
            _engine = create_engine(
                f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DBNAME}')
        case 'stock':
            _engine = _engine = create_engine(
                f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/stock')
    return _engine


# Redis init
def generate_redis_session():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE, decode_responses=True)
    return r


# Job init
def generate_job_scheduler():
    _job_scheduler = BackgroundScheduler()
    return _job_scheduler


mysql_engine = get_mysql_engine()
session = generate_mysql_session()
redis_store = generate_redis_session()
job_scheduler = generate_job_scheduler()
