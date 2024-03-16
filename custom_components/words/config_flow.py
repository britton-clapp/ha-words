"""Config flow for Words integration."""
import os
from typing import Dict

import voluptuous as vol
from .const import DOMAIN
from homeassistant import config_entries
import logging

_LOGGER = logging.getLogger(__name__)

DEFAULT_UPDATE_INTERVAL = 3  # Default update interval in minutes

DATA_SCHEMA = vol.Schema({
    vol.Required("file_path"): str,
    vol.Required(
        "update_interval",
        default=DEFAULT_UPDATE_INTERVAL): vol.All(vol.Coerce(int), vol.Range(min=1, max=60))
})



@config_entries.HANDLERS.register(DOMAIN)
class WordsFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Words."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        _LOGGER.info(user_input)
        errors: Dict[str, str] = {}
        if user_input is not None:
            # Validate and store user input
            if os.path.isfile(user_input['file_path']):
                return self.async_create_entry(
                    title="Words",
                    data={},
                    options={
                        "file_path": user_input["file_path"],
                        "update_interval": user_input["update_interval"]
                    }
                )
            else:
                errors["base"] = "invalid path"
        # @TODO: Verify that it's a csv file.
        # @TODO: Verify that it has multiple lines.
        # @TODO: Verify that it has columns for word and definition.

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)