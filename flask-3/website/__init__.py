from flask import Flask

def CREATE_APP():
    app = Flask('__name__')
    app.config['SECRET_KEY'] = 'blu blu blu'
    
    from .views import views
    from .home import home
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(home, url_prefix = '/home')
    
    return app
