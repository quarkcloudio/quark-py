import os
import re
import importlib
from flask import request

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
    resource = request.view_args.get('resource')
    resource_snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', resource).lower()
    app_class = load_class("quark/app/login/"+resource_snake_case+".py",resource.capitalize())
    if app_class is None:
        return None
    parent_classes = app_class.__bases__
    if parent_classes[0].__name__ != class_type:
        return None
    return app_class

# Load resource class object
def load_resource_object(resource_class_type: str):
    app_class = load_resource(resource_class_type)
    if app_class is None:
        return None
    obj = app_class()
    return obj