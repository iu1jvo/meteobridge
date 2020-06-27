"""Constants in meteobridge integration."""
import logging

from homeassistant.const import (
    CONF_UNIT_SYSTEM_METRIC,
    CONF_UNIT_SYSTEM_IMPERIAL,
)
from pymeteobridgeio import (
    DEVICE_TYPE_BINARY_SENSOR,
    DEVICE_TYPE_SENSOR,
)
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN

DOMAIN = "meteobridge"

METEOBRIDGE_PLATFORMS = [
    "binary_sensor",
    "sensor",
]

DISPLAY_UNIT_SYSTEMS = [
    CONF_UNIT_SYSTEM_METRIC,
    CONF_UNIT_SYSTEM_IMPERIAL,
]

ATTR_UPDATED = "updated"
ATTR_BRAND = "brand"
ATTR_STATION_HW = "station_hw"
ATTR_STATION_IP = "station_ip"

CONF_LANGUAGE = "language"
CONF_EXTRA_SENSORS = "extra_sensors"

DEFAULT_BRAND = "Meteobridge"
DEFAULT_ATTRIBUTION = "Powered by Meteobridge"
DEFAULT_USERNAME = "meteobridge"
DEFAULT_LANGUAGE = "en"
DEFAULT_SCAN_INTERVAL = 10

LOGGER = logging.getLogger(__package__)
