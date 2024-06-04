from discord.ext import commands

from .cogs.ping import ping

import modules.log as log
import modules.config as configReader

config:dict = configReader.pluginData('ping', 'config.yml', 'yml')

async def setup(bot: commands.Bot) -> None:
    keys = ['message', 'ephemeral']
    for key in keys:
        if key not in config:
            log.write('ping', f'Le fichier de configuration est invalide, la clé `{key}` est manquante', log.levels.error)
            return


    await bot.add_cog(
        ping(bot, config)
    )
