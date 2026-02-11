import autocommands.salut as salut

async def run(bot, message, args):
    if not args:
        await message.channel.send("Euuh... j'ai besoin d'un truc a reload :3")
        return
    if args[0] == "csv":
        salut.init()
        await message.channel.send("Mouahaha, tous les CSVs sont rechargés ! :3")