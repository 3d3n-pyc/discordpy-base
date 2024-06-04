import discord
from discord.ext import commands
from discord import app_commands


class ping(commands.Cog):
    def __init__(self, bot: commands.Bot, config:dict) -> None:
        self.bot = bot
        self.config = config
    
    @app_commands.command(name='ping', description='Renvoie le ping du bot')
    async def pingCommand(self, interaction: discord.Interaction):
        message = self.config['message'].replace('{ping}', f'{round(self.bot.latency * 1000)}')
        embed = discord.Embed(description=message, colour=0x2ECC71)
        await interaction.response.send_message(embed=embed, ephemeral=self.config['ephemeral'])
