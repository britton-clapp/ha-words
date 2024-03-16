"""Config flow for Words integration."""
import voluptuous as vol
from .const import DOMAIN
from homeassistant import config_entries

DEFAULT_UPDATE_INTERVAL = 10  # Default update interval in minutes

DATA_SCHEMA = vol.Schema({
    vol.Required("file_path"): str,
    vol.Required("update_interval", default=DEFAULT_UPDATE_INTERVAL): vol.All(vol.Coerce(int), vol.Range(min=1))
})



@config_entries.HANDLERS.register(DOMAIN)
class WordsFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Words."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Validate and store user input
            return self.async_create_entry(title="Words", data=user_input)
        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)