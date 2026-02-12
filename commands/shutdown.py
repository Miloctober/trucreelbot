from utils.embeds import make_embed
import config

async def run(bot, message, args):
    await message.channel.send(embed=make_embed(title="Oww :(", author=message.author, color=config.CONFIRMATION))
    await bot.db.close()
    await bot.close()