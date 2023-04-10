"""L.I.L.I.T.H. Discord client."""


__all__ = ['LILITHClient']
__author__ = 'Lily Alexander'
__version__ = '0.1.0'


import logging

import discord

import ai


class LILITHClient(discord.Client):
    """This client object will represent L.I.L.I.T.H.'s Discord bot user."""

    def __init__(self, owner_ids: str, dataset_filepath: str,
                 prefix: str = '!', response_length: int = 128):
        """Initialise the client.
        
        Parameters:
        owner_ids: str - the owner's Discord ID(s), separated by commas.
        dataset_filepath: str - the filepath to the training dataset.
        prefix: str = '!': the prefix all commands will begin with.
        response_length: int = 128 - the length of the AI's responses, in characters.
        """

        # Call discord.Client's __init__ method.
        super().__init__(intents=discord.Intents.all())

        # Create the client's logger.
        self.logger = logging.getLogger(__name__)

        # Save the owner's discord IDs.
        self.owner_ids = owner_ids.split(',')

        # Save the prefix and response length.
        self.prefix = prefix
        self.response_length = response_length

        # Load the AI.
        self.ai = ai.AI(dataset_filepath)
    
    async def on_ready(self):
        """Called when the bot is ready."""

        self.logger.info('Bot ready.')
    
    async def on_message(self, message: discord.Message):
        if str(message.author.id) in self.owner_ids:
            # If the message comes from an owner, save it.
            if message.content.startswith(self.prefix):
                # If the message is a command, run it.
                command = message.content.removeprefix(self.prefix)
                
                if command == 'LOAD':
                    # Load all the data in this guild.
                    await message.channel.send('Loading guild. This could take a while.')

                    for channel in message.guild.channels:
                        if not isinstance(channel, discord.TextChannel):
                            continue

                        async for m in channel.history(limit=None):
                            if str(m.author.id) in self.owner_ids:
                                self.ai.save_data(m.content)
                    
                    self.ai.load_data()
                    await message.channel.send('Data loaded.')

                else:
                    await message.channel.send('Invalid command.')
                
            else:
                # Otherwise, just save it and reload the model.
                self.ai.save_data(message.content)
                self.ai.load_data()
        
        if message.guild is None or self.user.mention in message.content:
            # Otherwise, if the message is addressed to L.I.L.I.T.H. or in a PM, respond.
            sentence = self.ai.get_sentence(self.response_length)
            await message.channel.send(sentence)
