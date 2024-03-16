"""Provides random words."""
import os
import random

from .const import DOMAIN
import aiohttp
import aiofiles
import asyncio
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import callback, HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
import logging

_LOGGER = logging.getLogger(__name__)

# def set_word(hass: HomeAssistant, text: str):
#     """Helper function to set the random word."""
#     _LOGGER.debug("set_word")
#     hass.states.async_set("words.random_word", text)

def setup(hass: HomeAssistant, config: dict):
    """This setup does nothing, we use the async setup."""
    _LOGGER.debug("setup")
    return True

async def async_setup(hass: HomeAssistant, config: dict):
    """Setup from configuration.yaml."""
    _LOGGER.debug("async_setup")
    
    #`config` is the full dict from `configuration.yaml`.
    #set_word(hass, "")

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Setup from Config Flow Result."""
    _LOGGER.debug("async_setup_entry")
    
    coordinator = WordUpdateCoordinator(
        hass,
        _LOGGER,
        update_interval=timedelta(seconds=60)
    )
    await coordinator.async_refresh()
    
    hass.data[DOMAIN] = {
        "coordinator": coordinator
    }
    
    hass.async_create_task(async_load_platform(hass, "sensor", DOMAIN, {}, entry))
    return True

class WordUpdateCoordinator(DataUpdateCoordinator):
    """Update handler."""

    def __init__(self, hass, logger, update_interval=None):
        """Initialize global data updater."""
        logger.debug("__init__")

        super().__init__(
            hass,
            logger,
            name=DOMAIN,
            update_interval=update_interval,
            update_method=self._async_update_data,
        )
        
    async def _async_update_data(self):
        """Fetch a random word."""
        self.logger.debug("_async_update_data")

        string = \
"""\
word	definition
abase	to humiliate, degrade
abate	to reduce, lessen
abdicate	to give up a position, usually one of leadership
abduct	to kidnap, take by force
aberration	a state or condition markedly different from the norm
abet	to aid, help, encourage
abhor	to hate, detest
abide	to put up with, tolerate
abject	cast down in spirit, showing hopelessness or resignation
abjure	to reject, renounce
abnegation	denial of comfort to oneself
abort	to give up on a half-finished project or effort
abridge	to reduce, diminish
test_word	this is a test definition
"""

        # # Read the first line of csv file
        # header_line = await file.readline()
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

