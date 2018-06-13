from shortify.factory import create_app

# The application instance to use directly or by Gunicorn
application = create_app()


if __name__ == '__main__':
    application.run()
