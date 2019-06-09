# DiscordDB
[![Documentation Status](https://readthedocs.org/projects/discorddb/badge/?version=latest)](https://discorddb.readthedocs.io/en/latest/?badge=latest)

A simple database which uses a Discord channel to store data.

### Installation
To install current latest release you can use following command:
```sh
python3 -m pip install DiscordDB
```


### Basic Example
```python
from discordDB import DiscordDB
from discord.ext import commands


LOGS = []
DATABASE_CHANNEL_ID = 399397622743564297


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")
        self.discordDB = DiscordDB(self, DATABASE_CHANNEL_ID)

    @commands.command()
    async def log(self, ctx, *, text):
        data = {
            "name": ctx.author,
            "text": text
        }
        _id = await self.discordDB.set(data)
        LOGS.append(_id)

    @commands.command()
    async def show_logs(self, ctx):
        for _id in LOGS:
            data = await self.discordDB.get(_id)
            await ctx.send(f"Name: {data.name}, Text: {data.text}")


bot = MyBot()
bot.run("TOKEN")
```


### Requirements
* discord.py


### Documentation
Head over to [documentation] for full API reference. 


[documentation]: https://discorddb.readthedocs.io/en/latest/
