"""Constants in meteobridge integration."""
from __future__ import annotations

from homeassistant.const import (
    CONF_SCAN_INTERVAL,
)

DOMAIN = "meteobridge"

METEOBRIDGE_PLATFORMS = [
    "binary_sensor",
    "sensor",
]

ATTR_MEASSURE_TIME = "meassure_time"

CONF_EXTRA_SENSORS = "extra_sensors"
CONFIG_OPTIONS = [
    CONF_SCAN_INTERVAL,
    CONF_EXTRA_SENSORS,
]
CONF_UNIT_SYSTEM_IMPERIAL = "imperial"
CONF_UNIT_SYSTEM_METRIC = "metric"

DEFAULT_ATTRIBUTION = "Powered by Meteobridge"
DEFAULT_BRAND = "Meteobridge"
MIN_SCAN_INTERVAL = 10
DEFAULT_SCAN_INTERVAL = 60
DEFAULT_URL_SCAN_INTERVAL = 120
MAX_SCAN_INTERVAL = 360
DEFAULT_USERNAME = "meteobridge"

TRANSLATION_KEY_AQI_DESCRIPTION = "aqi_description"
TRANSLATION_KEY_BEAUFORT = "beaufort"
TRANSLATION_KEY_TREND = "trend"
TRANSLATION_KEY_UV_DESCRIPTION = "uv_description"
TRANSLATION_KEY_WIND_CARDINAL = "wind_cardinal"


def is_url_host(host: str) -> bool:
    """Return whether the host is configured with an HTTP(S) URL."""
    return host.lower().startswith(("http://", "https://"))


def get_default_scan_interval(host: str) -> int:
    """Return the default scan interval for a host."""
    return DEFAULT_URL_SCAN_INTERVAL if is_url_host(host) else DEFAULT_SCAN_INTERVAL


def clamp_scan_interval(host: str, scan_interval: int) -> int:
    """Return a scan interval within the range allowed for the host."""
    min_scan_interval = (
        DEFAULT_URL_SCAN_INTERVAL if is_url_host(host) else MIN_SCAN_INTERVAL
    )
    return min(MAX_SCAN_INTERVAL, max(min_scan_interval, scan_interval))
