# Change Log

## [3.4.0] - 2025-04-13
- Meteobridge Integration mantenance restored.
- Added Binary Sensor for:
    - Wind Sensor battery status
    - Temperature/Humidity Sensor battery status
    - Rain Sensor battery status

## [3.3.4] - 2023-02-04

- After HA Version 2023.2 user will start to see this warning *Detected integration that called async_setup_platforms*. This call has now been replaced by the proper new function.
- Added the possibility to connect to a Meteobridge device that is remote from Home Assistant. In order for this to work you must enable *Internet Remote Login* on the Meteobridge device. You do that by login in to your Meteobridge device - go to the *System* section and then *Administration*. Here you will find the *Internet Remote Login* option. Ensure the box is ticked, and then press *Copy URL*. Take this URL and paste it in to the IP Address field when setting up Meteobridge in Home Assistant - Then enter your credentials as you normally would. As this is remote, I recommend you do not set the polling interval to something smaller than 60 seconds.

### Fixed/Changed

## [3.3.3] - 2023-01-04

### Fixed/Changed
- Issue [#27](https://github.com/briis/meteobridge/issues/27) Removed all deprecated device classes and implemetend `translation_key` to continue translating certain values in the UI.
- Cleaned up the code to use the correct Device Classes based on all the new changes in 2023.1
- Minimum required version from now on is 2023.1.x

## [3.2.9] - 2022-11-16

### Added

- Added Italian language files for sensors and configuration flow. Thank you to @iu1jvo.
- Issue [#25](https://github.com/briis/meteobridge/issues/25) Added the possibility to change the Username and Password after the installation. Go to *Settings*->*Devices & Services*. Find the Meteobridge Integration and click *CONFIGURE*. From the menu, you can now change these items.

## [3.2.8] - 2022-11-03

### Fixed

- Depreceation warning for `is_metric` is now fixed, and function moved to new standard.

### Changed
- Converted all DEVICE_CLASS values to SensorDeviceClass.DEVICE_CLASS, which makes it possible to change the Unit of Measurement directly from the GUI for most sensors.
- Bumped minimum required Home Assistant version to 2022.11.0 due to the changes in this release

## [3.2.7] - 2022-09-11

### Added

- Added new sensor `precip_accum_last24h` which holds the value for the last 24 hours of rain.

## [3.2.6] - 2022-05-26

### Fixed

- Fixing deprecated `async_get_registry` that will start showing up in HA 2022.6


## [3.2.5] - 2022-03-28

### Added

- Issue [[#22](https://github.com/briis/meteobridge/issues/22) Added German Laguage Files for sensors and configuration flow. Thank you to @rogerkilo


## [3.2.4] - 2022-01-08

### Fixed

- Issue [#20](https://github.com/briis/meteobridge/issues/20) Wind Chill was until now a Calculated value, as the Meteobridge had issues with WeatherFlow stations and Wind Chill calculations. The December 6th release of Meteobridge have fixed that problem, so I can now revert to use the wind_chill value from the Meteobridge station.


## [3.2.3] - 2021-12-16

### Fixed

- Added retry option if data is missing or not in expected format
- Fixing error thrown when wind values are not present.
  - Final Closing of Issue #18


## [3.2.2] - 2021-12-15

### Added

- New sensor `air_quality_index`. Returns AQI Level based on PM2.5 particles using United States Environmental Protection Agency (EPA) standard. (If Air Quality Sensors attached to Meteobridge)
- New sensors `precipitation_current_month` and `precipitation_current_year`. These show the accumulated precipitation for the current month and current year.
  - Closing Issue #19

### Fixed

- If there is something wrong with the data retrival - Metobridge not available - the system would crash due to missing values and calling conversion functions. Now empty values are returned.
  - Closing Issue #18


## [3.2.1] - 2021-12-01

### Fixed
- Issue #17. Low Battery Binary sensor was still present in the Integration, but the data field was removed, so caused an error and stopped updating. The binary sensor will be flagged as *unavailable*. Go to Integrations, and on the Meteobridge integration, click Entities and then you can remove the entity from the system.


## [3.2.0] - 2021-11-30

### Added
- New sensor `air_density`. This is a calculated sensor, measuring the current Air Density.
- New sensor `wet_bulb`. This is a calculated sensor, measuring the temperature of a parcel of air cooled to saturation (100% relative humidity).
- New sensor `aqi`. This is a calculated sensor, describing the Air Quality, based on average hourly PM2.5 data.

### Changes
- **Breaking Change** Removed binary sensor `is_battery_low`. The value of that, is not consitent across different Weather Stations.
- The Wind Chill sensor is now a calculated value. Also here there were inconsistencies across different Weather Stations, so I decided to use the [official formula](https://sciencing.com/calculate-wind-chill-factor-5981683.html) and calculate it in the program.
- Remodelled the Devcontainer setup. No impact on the Integration itself.
- Added better error handling when data is not available.


## [3.1.0] - 2021-11-28

> If you are upgrading from a version smaller than 3.0.0, please ensure to read the release notes for 3.0.0 as there are many breaking changes going from version 2.6.x to v3.0.x

### Added
- The Integration now support up to 4 attached Soil and 4 attached Leaf sensors. If these types of Sensors are attached to the Meteobridge device, they will automatically be setup in Home Assistant. **Note** This is untested, as I have no access to such type of sensors.


## [3.0.2] - 2021-11-23

> If you are upgrading from a version smaller than 3.0.0, please ensure to read the release notes for 3.0.0 as there are many breaking changes going from version 2.6.x to v3.0.x

### Changed
- Issue #14. A user reports an error when the program tries to convert a datetime string for Min and Max values. This change does not fix this, but introduces better error handling. So please check the log file after starting Meteobridge, so see if there is an error log in here, and report it to Issue #14.


## [3.0.1] - 2021-11-23

> If you are upgrading from a version smaller than 3.0.0, please ensure to read the release notes for 3.0.0 as there are many breaking changes going from version 2.6.x to v3.0.x

### Added
- Added `indoor_temperature` and `indoor_humidity` as new sensors. Fixing Issue #11.

### Changed
- All humidity values are now reported as an integer.


## [3.0.0] - 2021-11-22

This release contains **breaking changes** and you will have to re-define most of your settings in the UI and in automations after installation.

### Upgrade Instructions
Due to the many changes and entities that have been removed and replaced, we recommend the following process to upgrade from an earlier Beta or from an earlier release:

- Upgrade the Integration files, either through HACS (Recommended) or by copying the files manually to your custom_components/meteobridge directory.
- Restart Home Assistant
- Remove the Meteobridge Integration by going to the Integrations page, click the 3 dots in the lower right corner of the Meteobridge Integration and select Delete
- While still on this page, click the + ADD INTEGRATION button in the lower right corner, search for Meteobridge, and start the installation, supplying your credentials.

### Changes
- **BREAKING CHANGE** This is basically a completely new Integration, has all code as been rewritten from the beginning. This goes for the Integration itself, but also for the module `pymeteobridgedata` that this integration uses for communincating with the Meteobridge Logger. This is done to make the Integration compliant with Home Assistant coding practices and to ensure it is much easier to maintain going forward. As a consequence of that almost all sensors have a new Name and a new Unique ID, which is why a removal and re-installation is the best option when updating to this version. You will also have to change the sensor names in the UI and in Automations that are based on this Integration.
- Fixing Issue #8, by adding `meassure_time` as an attribute to min and max sensors.

### Added
- Frontend Translations are now in place for non-standard text based sensors like Pressure Trend and Beaufort Description.
