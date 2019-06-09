.. _intro:


Introduction
============

DiscordDB acts like a simple database which uses a discord channel to store data which
are generally not much important and you do not care about in an unlimited manner.


Requirements
------------

**discord.py**
    It requires ``discord.py`` as a main wrapper to post or get data from discord channel.


Installing
----------

You can install DiscordDB directly from PyPI using PIP and following command
in shell or command prompt: ::

    python3 -m pip install -U DiscordDB

You can also install the latest development version (**maybe unstable/broken**) by
using following command: ::

    python3 -m pip install -U git+https://github.com/thec0sm0s/DiscordDB.git


Basic Usage
-----------

.. code-block:: python3

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
