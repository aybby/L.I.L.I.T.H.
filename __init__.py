"""Learning to Imitate Lily Through use of Heurestics - L.I.L.I.T.H."""


__all__ = []
__author__ = 'Lily Alexander'
__version__ = '1.0.1'


import logging
import os

import dotenv

import client as client


def main():
    # Load .env file.
    dotenv.load_dotenv()

    # Create and configure logger.
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="lilith.log", filemode="w", level=logging.INFO)

    # Create and run client object.
    lilith_client = client.LILITHClient(os.environ['OWNER_IDS'], os.environ['DATASET_PATH'])
    lilith_client.run(os.environ['TOKEN'], log_handler=None)


# If running as main module, run main function.
if __name__ == '__main__':
    main()
