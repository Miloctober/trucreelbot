import discord
from ..salut import salut

salut.init()

def register_message_listener(bot, message_counter):
    async def _on_message(message: discord.Message):
        if message.author.bot or message.guild is None:
            return
        await message_counter.increment(message.guild.id, message.author.id)
        if "salut" in message.content.split().lower():
            await message.channel.send(f"{salut.sentence()}")

    bot.add_listener(_on_message, "on_message")