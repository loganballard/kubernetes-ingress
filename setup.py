from yaml import load, dump, FullLoader
from os import getcwd, mkdir, path
CONFIG_FILE = 'config.yaml'
API_SERVICE_FILE = 'api_service.yaml'
API_DEPLOYMENT_FILE = 'deployment.yaml'
MONGO_SERVICE_FILE = 'mongo_service.yaml'
INGRESS_FILE = 'ingress.yaml'
STATEFUL_SETS_FILE = 'stateful_sets.yaml'
OUT_DIR = 'output'


def create_output_dir():
    if not path.isdir(OUT_DIR):
        cur_wd = getcwd()
        full_path = cur_wd + path.sep + OUT_DIR
        mkdir(full_path)


def load_wrapper(filepath):
    loaded_f = {}
    with open(filepath, 'r') as f:
        loaded_f = load(f, Loader=FullLoader)
    return loaded_f


def create_api_service_yaml(config_dict):
    out_filep = OUT_DIR + path.sep + API_SERVICE_FILE
    print('creating ' + out_filep)
    if not config_dict:
        config_dict = load_wrapper(CONFIG_FILE)
    api_service_config = config_dict.get('api_service')
    print(api_service_config)
    api_service_dict = load_wrapper(API_SERVICE_FILE)
    api_service_dict['metadata']['name'] = api_service_config.get('name')
    api_service_dict['spec']['ports'][0]['port'] = api_service_config.get('spec').get('listen_port')
    api_service_dict['spec']['ports'][0]['targetPort'] = api_service_config.get('spec').get('out_port')
    with open(out_filep, 'w+') as out_f:
        out_f.write(dump(api_service_dict))
    