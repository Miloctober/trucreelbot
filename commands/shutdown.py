from utils.embeds import make_embed
import config

async def run(bot, message, args):
    await message.channel.send("Oww :(")
    await bot.db.close()
    await bot.close()