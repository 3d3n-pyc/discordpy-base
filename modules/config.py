import yaml
import json

def pluginData(plugin, file: str = 'config.yml', format: str = 'yml') -> dict:
    with open(f'plugin_data/{plugin}/{file}', 'r', encoding='UTF-8') as f:

        if format == 'yml' or format == 'yaml':
            return yaml.safe_load(f)

        if format == 'json':
            return json.load(f)
    
        return f.read()
