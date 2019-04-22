from flask import Blueprint, jsonify

# 连接http://host:port/account
account = Blueprint("/account", __name__)


# 访问http://host:port/account/test 这个链接，就会跳到这里
#上面的链接，绑定的就是这个方法，我们给浏览器或者接口请求 一个json格式的返回
@account.route('/test')
def test():
    return jsonify({'code':0,'content':'hi flask'})