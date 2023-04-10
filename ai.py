"""L.I.L.I.T.H.'s brain."""


import logging

import markovify


class AI:
    """A markov chain for L.I.L.I.T.H.'s brain."""

    def __init__(self, dataset_filepath):
        """Initialise the AI.
        
        Parameters:
        dataset_filepath: str - the filepath to the dataset to train on.
        """
        
        # Create logger.
        self.logger = logging.getLogger('LILITH.ai')

        # Store the dataset filepath.
        self.dataset_filepath = dataset_filepath
        # Load the data.
        self.load_data()

    def load_data(self):
        """Load the data from the dataset and compile the model."""

        # Read the dataset file.
        with open(self.dataset_filepath, encoding='utf8') as dataset_file:
            data = dataset_file.read()

        if data == '':
            # Whoops, someone forgot their training data.
            self.logger.critical('No training data.')
            raise ValueError

        # Create the model.
        self.model = markovify.NewlineText(data)
        self.model.compile(inplace=True)
    
    def save_data(self, sentence: str):
        """Save another sentence to the dataset.
        
        Note that this won't affect the existing model - you'll need to reload the data.

        Parameters:
        sentence: str - the sentence to save.
        """

        # Open the dataset file.
        with open(self.dataset_filepath, 'a', encoding='utf8') as dataset_file:
            # Append the sentence.
            dataset_file.write(sentence + '\n')

    def get_sentence(self, length: int = 128):
        """Generate a sentence.
        
        Parameters:
        length: int - the length of the sentence to generate, in characters.
        """
        return self.model.make_short_sentence(length)
