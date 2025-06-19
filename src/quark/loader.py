import os
import importlib
from . import config


def load_class(file_path, class_name):
    """从文件加载类"""
    abs_file_path = os.path.abspath(file_path)
    if not os.path.exists(abs_file_path):
        return None
    spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)


def load_object(file_path, class_name):
    """从文件加载类对象"""
    cls = load_class(file_path, class_name)
    obj = cls()
    return obj


def load_method(file_path, class_name, method_name, *args, **kwargs):
    """从文件加载类方法"""
    obj = load_object(file_path, class_name)
    method = getattr(obj, method_name)
    return method(*args, **kwargs)


def load_resource(resource: str, class_type: str):
    """从应用程序目录或quark包加载资源类对象"""
    app_class = None

    #  遍历应用目录下的所有类
    app_classes = get_classes_in_package(config.get("MODULE_PATH"))

    # 遍历quark包目录下的所有类
    quark_package_classes = get_classes_in_package(
        os.path.join(os.path.dirname(__file__), "app")
    )

    # 查找指定类名的类
    for getclass in app_classes:
        if (
            getclass.__name__ == resource.title()
            and getclass.__bases__[0].__name__ == class_type
        ):
            app_class = getclass

    if app_class is not None:
        return app_class

    # 查找指定类名的类
    for getclass in quark_package_classes:
        if (
            getclass.__name__ == resource.title()
            and getclass.__bases__[0].__name__ == class_type
        ):
            app_class = getclass

    return app_class


def get_classes_in_package(package_path):
    """获取指定包下的所有类"""
    classes = []
    package_dir = os.path.abspath(package_path)
    if not os.path.exists(package_dir):
        return classes

    # 使用 os.walk 遍历目录及其子目录
    for root, dirs, files in os.walk(package_dir):
        for file_name in files:
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = file_name[:-3]  # 去掉 .py 后缀
                module_path = os.path.join(root, file_name)
                full_module_name = (
                    os.path.relpath(root, package_dir).replace(os.sep, ".")
                    + "."
                    + module_name
                )
                if full_module_name.startswith("."):
                    full_module_name = full_module_name[1:]  # 去掉开头的点
                spec = importlib.util.spec_from_file_location(
                    full_module_name, module_path
                )
                if spec is None:
                    continue
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # 遍历模块中的所有成员，检查是否为类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type):
                        classes.append(attr)

    return classes


def load_resource_object(resource: str, resource_class_type: str):
    """从应用程序目录或quark包加载资源类对象"""
    app_class = load_resource(resource, resource_class_type)
    if app_class is None:
        return None
    obj = app_class()
    return obj
