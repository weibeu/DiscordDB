import discord

from .models import Data


class DiscordDB(object):
    """The Discord database client.

    Parameters
    ----------
    bot : discord.ext.commands.Bot
        An instance of discord.py Client or Bot representing your discord application.
    db_channel_id : int
        An integer representing ID of Discord channel you want to be used as database.

    """

    def __init__(self, bot, db_channel_id: int):
        self.__bot = bot
        self.__channel_id = db_channel_id

    @property
    def channel(self):
        """A property which returns an instance of ``discord.TextChannel`` which is being used as database."""
        return self.__bot.get_channel(self.__channel_id)

    async def set(self, data: dict) -> int:
        """A method to post and save data to your database channel.

        Parameters
        ----------
        data : dict
            Dictionary representing your raw data.

        Returns
        -------
        int
            An special integer which should be saved by the client to get this same data later.

        """
        embed = discord.Embed.from_dict({
            "fields": [{
                "name": name, "value": value
            } for name, value in data.items()]
        })
        message = await self.channel.send(embed=embed)
        return message.id

    async def get(self, _id: int) -> Data:
        """A method used to get your saved data from the database channel.

        Parameters
        ----------
        _id : int
            An special integer which was received from the :py:meth:`discordDB.DiscordDB.set` method.

        Returns
        -------
        Data
            An instance of :py:class:`discordDB.models.Data`, similar to python dictionaries but also
            supports accessing of its key using . syntax.

        """
        message = await self.channel.fetch_message(_id)
        _data = message.embeds[0].to_dict()["fields"]
        data = Data({_["name"]: _["value"] for _ in _data})
        data.created_at = message.created_at
        return data
