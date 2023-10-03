# NMEA Parser Changelog

* 0.5.0 (2021-06-28)
	- Fix bug where variable is referenced prior to assignment
	- Stop allowing sats in view messages to be pushed onto data frames when too many exist

* 0.4.0 (2021-06-22)
	- Add support for PySerial's non-standard port settings
	- Add support for console output via Python's logging module
	- Make all NMEA Messages in a dataframe publicly accessable
	- Remove unused return type from push back message in the `DataFrame` class

* 0.3.0 (2021-06-06)
    - Make individual SV observations publicly accessable from the `DataFrame` Class
    - Replace usages of the string "NULL" wit `None`

* 0.2.1 (2021-06-02)
	- Fix bug that would crash the library if a stream starts with no GPS fix

* 0.2.0 (2021-06-01)
	- Add ability to record a raw text dump of an incoming NMEA stream
	- Majorly simplify the built in logging module
	- Completely depreciate the nmea parser module.
	- Fix a bug where NMEA sentences without a fix threw an index error
	- Clean source code

* 0.1.2 (2021-05-25)
	- Fix 'inaproprate ioctl for device' error from serial library

* 0.1.1 (2021-05-24)
	- Improve safety of file handling in input stream module
	- Bug fixes in type checking
	- Fix absolute imports in project
	- Small fixes to documentation

* 0.1.0 (2021-05-20):
    - Inital release
