import autocommands.salut as salut

async def run(bot, message, args):
    salut.init()
    await message.channel.send("Mouahaha, tous les CSVs sont rechargés ! :3")