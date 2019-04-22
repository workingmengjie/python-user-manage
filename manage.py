from flask_script import Manager,Server
from backend import create_app

app = create_app()

app.debug = app.config['DEBUG']
host = app.config['HOST']
port = app.config['PORT']

# 初始化管理类
manager = Manager(app)

manager.add_command("runserver", Server(host=host,port=port,threaded=True))

@manager.shell
def make_shell_context():
    """Create a python CLI.
        return: Default import object
        type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=app)

if __name__ == "__main__":
    manager.run()