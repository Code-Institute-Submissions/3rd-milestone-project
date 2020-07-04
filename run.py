import os
from application import app

if __name__ == '__main__':
    app.run(host = os.getenv("IP"), port = os.getenv("PORT"))