import importlib

# Load a class method from a file
def load_class_method_from_file(file_path, class_name, method_name, *args, **kwargs):
    spec = importlib.util.spec_from_file_location('dynamic_module', file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    cls = getattr(module, class_name)
    obj = cls()
    method = getattr(obj, method_name)
    return method(*args, **kwargs)

# Load a class method from a module
def load_class_method_from_module(module_name, class_name, method_name, *args, **kwargs):
    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)
    obj = cls()
    method = getattr(obj, method_name)
    return method(*args, **kwargs)