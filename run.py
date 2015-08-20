from pjfotographie import app

if __name__ == '__main__':
    app.run(host=app.config.get('APP_HOST'),
            port=app.config.get('APP_PORT'),
            debug=app.config.get('APP_DEBUG'))