import asyncio
import random
import unittest

import aiofiles

# from custom_components.words import WordUpdateCoordinator


async def _async_update_data(self):
    """Fetch a random word."""
    # self.logger.debug("_async_update_data")

    # open a csv file called words.csv and read a random line
    try:
        async with aiofiles.open("words.csv", mode='r') as file:
            string = \
"""\
Word	Definition
abase	to humiliate, degrade
abate	to reduce, lessen
abdicate	to give up a position, usually one of leadership
test_word   this is a test definition
"""

            # # Read the first line of csv file
            header_line = await file.readline()
            #
            # # convert tsv header line to a list of strings
            # header = header_line.split('\t')

            # lines = await file.readlines()
            lines = string.split('\n')
            lines = list(filter(None, lines))
            header = lines.pop(0).split('\t')

            word_line = random.choice(lines)
            word_data = word_line.split('\t')
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