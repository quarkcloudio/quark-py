import importlib.util
import os
from typing import Any

import inflection

from . import Request, config


def load_class(file_path, class_name):
    """从文件加载类"""
    abs_file_path = os.path.abspath(file_path)
    if not os.path.exists(abs_file_path):
        return None
    spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
    if spec is None:
        return None
    module = importlib.util.module_from_spec(spec)
    if module is None:
        return None
    if spec.loader is None:
        return None
    spec.loader.exec_module(module)
    return getattr(module, class_name)


def load_object(file_path, class_name):
    """从文件加载类对象"""
    cls = load_class(file_path, class_name)
    if cls is None:
        return None

    obj = cls()
    return obj


def load_method(file_path, class_name, method_name, *args, **kwargs):
    """从文件加载类方法"""
    obj = load_object(file_path, class_name)
    method = getattr(obj, method_name)
    return method(*args, **kwargs)


def get_classes_in_package(package_path):
    """
    安全扫描指定目录，加载其中的类
    """
    classes = []
    package_dir = os.path.abspath(package_path)

    if not os.path.exists(package_dir):
        return classes

    # 禁止扫描的目录（防止导入用户虚拟环境）
    IGNORE_DIRS = {
        "venv",
        ".venv",
        "env",
        ".env",
        "Lib",
        "lib",
        "site-packages",
        "__pycache__",
    }

    for root, dirs, files in os.walk(package_dir):

        # 过滤不应该扫描的目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]

        for file_name in files:
            if not file_name.endswith(".py"):
                continue
            if file_name == "__init__.py":
                continue

            module_path = os.path.join(root, file_name)

            # 构造模块名（安全版本）
            rel_path = os.path.relpath(root, package_dir)
            rel_path = rel_path.replace(os.sep, ".")

            if rel_path == ".":
                full_module_name = file_name[:-3]
            else:
                full_module_name = f"{rel_path}.{file_name[:-3]}"

            # 非法模块名过滤
            if not full_module_name.replace(".", "").isidentifier():
                continue

            try:
                spec = importlib.util.spec_from_file_location(
                    full_module_name, module_path
                )
                if not spec or not spec.loader:
                    continue

                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # 遍历类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type):
                        classes.append(attr)

            except Exception as e:
                # 可以打印日志但不影响程序继续运行
                print(f"[WARN] 模块加载失败: {module_path} | {e}")

    return classes


def load_resource_classes(class_type: str):
    """从应用程序目录或quark包加载资源类"""
    get_classes = []

    #  遍历应用目录下的所有类
    app_classes = get_classes_in_package(config.get("MODULE_PATH"))

    # 遍历quark包目录下的所有类
    quark_package_classes = get_classes_in_package(
        os.path.join(os.path.dirname(__file__), "app")
    )

    # 查找指定类名的类
    for getclass in app_classes:
        if getclass.__bases__[0].__name__ == class_type:
            get_classes.append(getclass)

    # 查找指定类名的类
    for getclass in quark_package_classes:
        if getclass.__bases__[0].__name__ == class_type:
            get_classes.append(getclass)

    return get_classes


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
            getclass.__name__ == inflection.camelize(resource)
            and getclass.__bases__[0].__name__ == class_type
        ):
            app_class = getclass

    if app_class is not None:
        return app_class

    # 查找指定类名的类
    for getclass in quark_package_classes:
        if (
            getclass.__name__ == inflection.camelize(resource)
            and getclass.__bases__[0].__name__ == class_type
        ):
            app_class = getclass

    return app_class


async def load_resource_object(
    request: Request, resource: str, resource_class_type: str
) -> Any:
    """从应用程序目录或quark包加载资源类对象"""
    app_class = load_resource(resource, resource_class_type)
    if app_class is None:
        return None
    return await app_class().init(request)
