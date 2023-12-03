import os
import pkgutil
import importlib


def load_routers():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(dir_path, '../api/routes')
    relative_path = 'src.api.routes'

    routers = []
    for _, module_name, _ in pkgutil.iter_modules([absolute_path]):
        module = importlib.import_module(f'{relative_path}.{module_name}')
        routers.append(module.router)
    return routers
