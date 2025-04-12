from quark.model.user import User

# 执行安装操作
def install():
    User().migrate()