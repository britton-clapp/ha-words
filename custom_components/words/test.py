import asyncio
import csv
import random
import unittest

import aiofiles

# from custom_components.words import WordUpdateCoordinator


async def _async_update_data(self):
    """Fetch a random word."""
    # self.logger.debug("_async_update_data")

    # open a csv file called words.csv and read a random line
    try:
        with open('words.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            header = next(reader)  # Skip the header line

            data = list(reader)
            word_data = random.choice(data)
            word = dict(zip(header, word_data))
            return word
    except Exception as ex:
        pass
        # raise UpdateFailed from ex


class TestCalculations(unittest.TestCase):

    def test_async_update_data(self):
        # coordinator = WordUpdateCoordinator(None, None)
        data = asyncio.run(_async_update_data(self))
        print(data)


if __name__ == '__main__':
    unittest.main()