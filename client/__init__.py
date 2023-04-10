"""L.I.L.I.T.H. Discord client."""


__all__ = ['LILITHClient']
__author__ = 'Lily Alexander'
__version__ = '0.1.0'


import logging

import discord


class LILITHClient(discord.Client):
    """This client object will represent L.I.L.I.T.H.'s Discord bot user."""

    def __init__(self, owner_ids: str):
        """Initialise the client."""

        # Call discord.Client's __init__ method.
        super().__init__(intents=discord.Intents.all())

        # Create the client's logger.
        self.logger = logging.getLogger(__name__)

        # Save the owner's Discord IDs.
        self.owner_ids = owner_ids.split(',')
    
    async def on_ready(self):
        self.logger.info('Bot ready.')
