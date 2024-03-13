"""Provides random words."""
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

        # open a csv file called words.csv and read a random line
        try:
            async with aiofiles.open("words.csv", mode='r') as file:
                lines = await file.readlines()
                return random.choice(lines)
        except Exception as ex:
            raise UpdateFailed from ex
