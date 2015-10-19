from pjfotographie import app
import logging
from logging import StreamHandler

file_handler = StreamHandler()
record = ('%(asctime)s',
          '%(name)s',
          '%(levelname)s',
          '%(funcName)s',
          '%(lineno)d',
          '%(pathname)s',
          '%(message)s')
formatter = logging.Formatter(" - ".join(record))
file_handler.setFormatter(formatter)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run(host=app.config.get('APP_HOST'),
            port=app.config.get('APP_PORT'),
            debug=app.config.get('APP_DEBUG'))
