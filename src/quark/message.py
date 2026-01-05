# message.py
class Message:
    # 状态码常量
    StatusOk = 200  # 执行成功
    StatusUnauthorized = 401  # 未授权
    StatusForbidden = 403  # 无权限
    StatusError = 10001  # 自定义错误信息
    StatusParamError = 10002  # 参数错误

    def __init__(self, code=0, msg="", data=None, url=""):
        self.code = code
        self.msg = msg
        self.data = data
        self.url = url

    def to_dict(self):
        result = {
            'code': self.code,
            'msg': self.msg
        }
        if self.data is not None:
            result['data'] = self.data
        if self.url:
            result['url'] = self.url
        return result

    @classmethod
    def success(cls, message="", data=None):
        """返回正确信息"""
        return cls(
            code=cls.StatusOk,
            msg=message,
            data=data
        )

    @classmethod
    def error(cls, *params):
        """返回错误信息，error("内部服务调用异常") | error("错误", {"title":"标题"})"""
        code = cls.StatusError
        msg = ""
        data = None

        if len(params) == 1:
            msg = params[0]
        elif len(params) == 2:
            msg = params[0]
            data = params[1]

        return cls(
            code=code,
            msg=msg,
            data=data
        )

    @classmethod
    def error_by_code(cls, *params):
        """返回错误信息，error_by_code(10001) | error_by_code(10001, {"title":"标题"})"""
        code = cls.StatusError
        msg = ""
        data = None

        if len(params) == 1:
            code = params[0]
        elif len(params) == 2:
            code = params[0]
            data = params[1]

        msg = cls.get_msg_by_code(code)

        return cls(
            code=code,
            msg=msg,
            data=data
        )

    @classmethod
    def redirect_to(cls, *params):
        """输出模版引擎URL跳转，redirect_to("/home/index") | redirect_to("成功", "/home/index") | redirect_to("失败", "/home/index", 10001)"""
        msg = ""
        url = ""
        code = 200

        if len(params) == 1:
            url = params[0]
        elif len(params) == 2:
            msg = params[0]
            url = params[1]
        elif len(params) >= 3:
            msg = params[0]
            url = params[1]
            code = params[2]

        return cls(
            code=code,
            msg=msg,
            url=url
        )

    @classmethod
    def get_msg_by_code(cls, code):
        """根据code获取错误信息"""
        code_maps = [
            {'code': cls.StatusOk, 'msg': "ok"},
            {'code': cls.StatusError, 'msg': "Internal Server Error"},
            {'code': cls.StatusParamError, 'msg': "Param Error"},
            {'code': cls.StatusUnauthorized, 'msg': "Unauthorized"},
            {'code': cls.StatusForbidden, 'msg': "Forbidden"},
        ]
        
        for code_map in code_maps:
            if code_map['code'] == code:
                return code_map['msg']
        return ""