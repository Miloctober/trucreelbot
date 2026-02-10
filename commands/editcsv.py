import csv

async def run(bot, message, args):
    if args[0] == "add":
        with open(f"./data/csv/{args[1]}.csv", "a+", encoding="utf-8") as file:
            file.seek(0, 2)
            if file.tell() > 0:
                file.write("\n")
            file.write(" ".join(args[2:]))
            file.close()

    if args[0] == "display":
        content = []
        with open(f"./data/csv/{args[1]}.csv", mode ="r", encoding="utf-8")as file:
            for i, line in enumerate(file, start=1):
                content.append(f"{i}) {line.strip()}")
            await message.channel.send("\n".join(content))
            file.close()
    
    if args[0] == "delete":
        with open(f"./data/csv/{args[1]}.csv", mode = "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            file.close()
        removed = lines.pop(int(args[2]) - 1)
        with open(f"./data/csv/{args[1]}.csv", mode = "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
            file.close()