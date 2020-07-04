class Config(object):
    SECRET_KEY          = os.environ.get('SECRET_KEY')
    MONGO_DBNAME        = os.environ.get('DB_NAME')           
    MONGO_URL           = os.environ.get('MONGO_URI')   