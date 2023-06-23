import json
from typing import List, Dict
from gi.repository import Gst

from models.plugin import Plugin

class Pipeline:
    
    json_pipes: Dict[str, any] = None
    plugins_loaded: List[Plugin] = []

    def __init__(self, json_path) -> None:
        with open(json_path, 'r') as file_handle:
            self.json_pipes = json.loads(file_handle.read())

        self.__pre_init()
        self.__post_init()

    def __pre_init(self):
        for json_plugin_config in self.json_pipes['pipeline']:
            plugin = Plugin()
            plugin.elem_name = json_plugin_config['elem_name']
            plugin.plugin_name = json_plugin_config['plugin_name']
            plugin.attributes = json_plugin_config['attributes']
            plugin.attach_queue = json_plugin_config['attach_queue']

            self.plugins_loaded.append(plugin)

    def __post_init(self):
        for plugin in self.plugins_loaded:
            if plugin.attach_queue and plugin.elem_name == 'queue':
                raise ValueError(f'Invalid attribute for {plugin.plugin_name}.{plugin.elem_name} -> attach_queue={plugin.attach_queue}')
            
            if  Gst.Registry.get().find_plugin(plugin.plugin_name) is None:
                raise ValueError(f'plugin `{plugin.plugin_name}` does not exists')

    def __get(self) -> str:
        # compose pipes
        result = 'gst-launch-1.0 '
        for plugin in self.plugins_loaded:
            result += f'{plugin.plugin_name} name={plugin.elem_name} ! '
            if plugin.attach_queue:
                result += f'queue name=queue_{plugin.elem_name} ! '
        
        result = result.removesuffix('! ')
        return result

    def get(self) -> str:
        return self.__get()

