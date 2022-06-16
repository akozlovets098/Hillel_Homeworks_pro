import os
from app import app
from db import init_db

if __name__ == '__main__':
    db_name = app.config.get('DB_URL')
    if not os.path.exists(db_name):
        init_db(db_name)
    import routes
    app.run()