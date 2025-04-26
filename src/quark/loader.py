import os
import re
import importlib
from flask import request
from .config import config

# Load a class from a file
def load_class(file_path, class_name):
    abs_file_path = os.path.abspath(file_path)
    if not os.path.exists(abs_file_path):
        return None
    spec = importlib.util.spec_from_file_location('dynamic_module', file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)

# Load a class object from a file
def load_object(file_path, class_name):
    cls = load_class(file_path, class_name)
    obj = cls()
    return obj

# Load a class method from a file
def load_method(file_path, class_name, method_name, *args, **kwargs):
    obj = load_object(file_path, class_name)
    method = getattr(obj, method_name)
    return method(*args, **kwargs)

# Load resource class
def load_resource(class_type: str):
    app_class = None
    resource = request.view_args.get('resource')
    resource_snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', resource).lower()
    module_classes=get_classes_in_package(config["MODULE_PATH"])
    app_classes=get_classes_in_package(os.path.join(os.path.dirname(__file__), 'app'))
    for getclass in module_classes:
        module_name = getclass.__module__.split('.')[-1]
        if getclass.__bases__[0].__name__ == class_type and module_name == resource_snake_case:
                app_class = getclass

    if app_class is not None:
        return app_class
    
    for getclass in app_classes:
        module_name = getclass.__module__.split('.')[-1]
        if getclass.__bases__[0].__name__ == class_type and module_name == resource_snake_case:
                app_class = getclass

    return app_class
# 遍历包路径下的所有类（包括子目录）
def get_classes_in_package(package_path):
    classes = []
    package_dir = os.path.abspath(package_path)
    if not os.path.exists(package_dir):
        return classes

    # 使用 os.walk 遍历目录及其子目录
    for root, dirs, files in os.walk(package_dir):
        for file_name in files:
            if file_name.endswith('.py') and file_name != '__init__.py':
                module_name = file_name[:-3]  # 去掉 .py 后缀
                module_path = os.path.join(root, file_name)
                full_module_name = os.path.relpath(root, package_dir).replace(os.sep, '.') + '.' + module_name
                if full_module_name.startswith('.'):
                    full_module_name = full_module_name[1:]  # 去掉开头的点
                spec = importlib.util.spec_from_file_location(full_module_name, module_path)
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
# Load resource class object
def load_resource_object(resource_class_type: str):
    app_class = load_resource(resource_class_type)
    if app_class is None:
        return None
    obj = app_class()
    return obj