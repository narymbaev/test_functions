import os

from app import app



# timber.setup_packages(timber.WARNING, [
#     'aio_pika', 'aiormq', 'aioredis', 'cache', 'psql', 'mongo'
# ])

if __name__ == '__main__':

    app.set_config(
        ROOT_PATH=os.path.dirname(__file__),
    )
    try:
        app.run('0.0.0.0', port=8080, access_log=False)
    except Exception as e:
        print(e)
