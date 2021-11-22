"""Meteobridge Sensors for Home Assistant"""
from __future__ import annotations

import logging
from dataclasses import dataclass

from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    DEGREE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_PM1,
    DEVICE_CLASS_PM10,
    DEVICE_CLASS_PM25,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_TIMESTAMP,
    TEMP_CELSIUS,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import StateType

from .const import (
    ATTR_MEASSURE_TIME,
    DEVICE_CLASS_LOCAL_BEAUFORT,
    DEVICE_CLASS_LOCAL_TREND,
    DEVICE_CLASS_LOCAL_UV_DESCRIPTION,
    DEVICE_CLASS_LOCAL_WIND_CARDINAL,
    DOMAIN,
)
from .entity import MeteobridgeEntity
from .models import MeteobridgeEntryData


@dataclass
class MeteobridgeRequiredKeysMixin:
    """Mixin for required keys."""

    unit_type: str
    always_add: bool
    attribute_field: str


@dataclass
class MeteobridgeSensorEntityDescription(
    SensorEntityDescription, MeteobridgeRequiredKeysMixin
):
    """Describes Meteobridge Sensor entity."""


SENSOR_TYPES: tuple[MeteobridgeSensorEntityDescription, ...] = (
    MeteobridgeSensorEntityDescription(
        key="air_temperature",
        name="Air Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="sea_level_pressure",
        name="Sea Level Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="pressure",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="station_pressure",
        name="Station Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="pressure",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity",
        name="Relative Humidity",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="precip_rate",
        name="Precipitation Rate",
        icon="mdi:weather-pouring",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="precipitation_rate",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="precip_accum_local_day",
        name="Precipitation Today",
        icon="mdi:weather-rainy",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="precipitation",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="wind_avg",
        name="Wind Speed",
        icon="mdi:weather-windy-variant",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="length",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="wind_direction",
        name="Wind Direction",
        icon="mdi:compass",
        native_unit_of_measurement=DEGREE,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="wind_gust",
        name="Wind Gust",
        icon="mdi:weather-windy",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="length",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="beaufort",
        name="Beaufort",
        icon="mdi:windsock",
        native_unit_of_measurement="Bft",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="solar_radiation",
        name="Solar Radiation",
        icon="mdi:solar-power",
        native_unit_of_measurement="W/m^2",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="uv",
        name="UV Index",
        icon="mdi:weather-sunny-alert",
        native_unit_of_measurement="UVI",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="lightning_strike_last_epoch",
        name="Last Lightning Strike",
        device_class=DEVICE_CLASS_TIMESTAMP,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="lightning_strike_last_distance",
        name="Last Lightning Strike Distance",
        icon="mdi:map-marker-distance",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="distance",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="lightning_strike_count",
        name="Lightning Strike Count",
        icon="mdi:weather-lightning",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="feels_like",
        name="Feels Like Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index",
        name="Heat Index",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="wind_chill",
        name="Wind Chill",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="dew_point",
        name="Dewpoint",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="visibility",
        name="Visibility",
        icon="mdi:eye",
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="distance",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_trend",
        name="Temperature Trend",
        icon="mdi:trending-up",
        device_class=DEVICE_CLASS_LOCAL_TREND,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="pressure_trend",
        name="Pressure Trend",
        icon="mdi:trending-up",
        device_class=DEVICE_CLASS_LOCAL_TREND,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="uv_description",
        name="UV Description",
        icon="mdi:weather-sunny-alert",
        device_class=DEVICE_CLASS_LOCAL_UV_DESCRIPTION,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="wind_cardinal",
        name="Wind Cardinal",
        icon="mdi:compass",
        device_class=DEVICE_CLASS_LOCAL_WIND_CARDINAL,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="beaufort_description",
        name="Beaufort Description",
        icon="mdi:windsock",
        device_class=DEVICE_CLASS_LOCAL_BEAUFORT,
        unit_type="none",
        always_add=True,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="air_pm_10",
        name="Air Quality PM10",
        icon="mdi:air-filter",
        device_class=DEVICE_CLASS_PM10,
        native_unit_of_measurement="µg/m³",
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="air_pm_25",
        name="Air Quality PM2.5",
        icon="mdi:air-filter",
        device_class=DEVICE_CLASS_PM25,
        native_unit_of_measurement="µg/m³",
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="air_pm_1",
        name="Air Quality PM1",
        icon="mdi:air-filter",
        device_class=DEVICE_CLASS_PM1,
        native_unit_of_measurement="µg/m³",
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="forecast",
        name="Station Forecast",
        icon="mdi:crystal-ball",
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_dmin",
        name="Air Temperature Day Min",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_dmintime",
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_dmax",
        name="Air Temperature Day Max",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_dmaxtime",
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_mmin",
        name="Air Temperature Month Min",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_mmintime",
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_mmax",
        name="Air Temperature Month Max",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_mmaxtime",
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_ymin",
        name="Air Temperature Year Min",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_ymintime",
    ),
    MeteobridgeSensorEntityDescription(
        key="air_temperature_ymax",
        name="Air Temperature Year Max",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=True,
        attribute_field="air_temperature_ymaxtime",
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_1",
        name="Extra Temperature 1",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_1",
        name="Extra Humidity 1",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_1",
        name="Extra Heat Index 1",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_2",
        name="Extra Temperature 2",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_2",
        name="Extra Humidity 2",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_2",
        name="Extra Heat Index 2",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_3",
        name="Extra Temperature 3",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_3",
        name="Extra Humidity 3",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_3",
        name="Extra Heat Index 3",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_4",
        name="Extra Temperature 4",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_4",
        name="Extra Humidity 4",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_4",
        name="Extra Heat Index 4",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_5",
        name="Extra Temperature 5",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_5",
        name="Extra Humidity 5",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_5",
        name="Extra Heat Index 5",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_6",
        name="Extra Temperature 6",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_6",
        name="Extra Humidity 6",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_6",
        name="Extra Heat Index 6",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="temperature_extra_7",
        name="Extra Temperature 7",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="relative_humidity_extra_7",
        name="Extra Humidity 7",
        native_unit_of_measurement="%",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
    MeteobridgeSensorEntityDescription(
        key="heat_index_extra_7",
        name="Extra Heat Index 7",
        device_class=DEVICE_CLASS_TEMPERATURE,
        native_unit_of_measurement=TEMP_CELSIUS,
        state_class=STATE_CLASS_MEASUREMENT,
        unit_type="none",
        always_add=False,
        attribute_field=None,
    ),
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up sensors for Meteobridge integration."""
    entry_data: MeteobridgeEntryData = hass.data[DOMAIN][entry.entry_id]
    meteobridgeapi = entry_data.meteobridgeapi
    coordinator = entry_data.coordinator
    device_data = entry_data.device_data
    unit_descriptions = entry_data.unit_descriptions

    entities = []
    for description in SENSOR_TYPES:
        if description.always_add or (
            getattr(coordinator.data, description.key) is not None
        ):
            entities.append(
                MeteobridgeSensor(
                    meteobridgeapi,
                    coordinator,
                    device_data,
                    description,
                    entry,
                    unit_descriptions,
                )
            )

            _LOGGER.debug(
                "Adding sensor entity %s",
                description.name,
            )

    async_add_entities(entities)


class MeteobridgeSensor(MeteobridgeEntity, SensorEntity):
    """Implementation of a Meteobridge Sensor."""

    def __init__(
        self,
        meteobridgeapi,
        coordinator,
        device_data,
        description,
        entries: ConfigEntry,
        unit_descriptions,
    ):
        """Initialize an Meteobridge sensor."""
        super().__init__(
            meteobridgeapi,
            coordinator,
            device_data,
            description,
            entries,
        )
        self._attr_name = f"{DOMAIN.capitalize()} {self.entity_description.name}"
        if self.entity_description.native_unit_of_measurement is None:
            self._attr_native_unit_of_measurement = unit_descriptions[
                self.entity_description.unit_type
            ]

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""

        return (
            getattr(self.coordinator.data, self.entity_description.key)
            if self.coordinator.data
            else None
        )

    @property
    def extra_state_attributes(self):
        """Return the sensor state attributes."""
        if self.entity_description.attribute_field is not None:
            return {
                **super().extra_state_attributes,
                ATTR_MEASSURE_TIME: getattr(
                    self.coordinator.data, self.entity_description.attribute_field
                ),
            }
        return super().extra_state_attributes
