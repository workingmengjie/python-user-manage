from backend.account.views import account

def register(app):
    app.register_blueprint(account, url_prefix='/account',strict_slashes=False)