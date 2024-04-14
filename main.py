import json; data = json.load(open('config.json', 'r'))
import sys; sys.dont_write_bytecode = True if data['PythonDontWriteBytecode'] else False

import discord
from discord.ext import commands

import os
import yaml
import shutil
import pip

import modules.log as log


class client(commands.Bot):
    
    def __init__(self):
        super().__init__(
            command_prefix='$',
            intents = discord.Intents.all(),
            application_id = data["app_id"]
        )

        self.initial_extensions = []
        
        plugins = [dir for dir in os.listdir('plugins')]
        
        for plugin in plugins:
            self.initial_extensions.append(f'plugins.{plugin}.main')


    async def setup_hook(self):
        log.write('main', 'Mode débug activé', log.levels.debug)
        
        for ext in self.initial_extensions:
            ext: str
            name = ext.removeprefix('plugins.').removesuffix('.main')
            try:
                with open(f'plugins/{name}/plugin.yml', 'r') as file:
                    pluginData:dict = yaml.safe_load(file)
                
                if pluginData.get('requirements', []):
                    for requirement in pluginData['requirements']:
                        try:
                            pip.main(['install', requirement])
                        except ImportError:
                            log.write('main', f'Le module {requirement} n\'a pas été trouvé ({pluginData["name"]} v{pluginData["version"]})', log.levels.error)
                
                log.write('main', f'Plugin {pluginData["name"]} v{pluginData["version"]} chargé', log.levels.debug)

                os.makedirs(f'plugin_data/{name}/', exist_ok=True)
            except FileNotFoundError:
                print(f'Le fichier plugins/{name}/plugin.yml n\'a pas été trouvé')
                
            files = [file for file in os.listdir(f'plugin_data/{name}/')]
            for file in os.listdir(f'plugins/{name}/resources'):
                if file not in files:
                    shutil.copy(f'plugins/{name}/resources/{file}', f'plugin_data/{name}/{file}')
            
            await self.load_extension(ext)
        
        global synced
        synced = await bot.tree.sync()
        
    async def on_ready(self):
        log.write('main', f'{self.user} est connecté avec {len(synced)} commande(s) synchronisée(s) sous la version {data["version"]}', log.levels.info)
    

bot = client(); bot.run(data["token"])