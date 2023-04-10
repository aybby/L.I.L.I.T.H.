"""Learning to Imitate Lily Through use of Heurestics - L.I.L.I.T.H."""


__all__ = []
__author__ = 'Lily Alexander'
__version__ = '0.1.0'


import os

import dotenv

import client


def main():
    # Load .env file.
    dotenv.load_dotenv()

    # Create and run client object.
    client = client.LILITHClient()
    client.run(os.environ['TOKEN'])


# If running as main module, run main function.
if __name__ == '__main__':
    main()
