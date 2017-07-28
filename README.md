# OpenFisca-Tracker

OpenFisca is a versatile microsimulation free software. 
Check the online [documentation](https://doc.openfisca.fr) for more details.

This package contains the tracker module of the [OpenFisca Web API](https://doc.openfisca.fr/openfisca-web-api/index.html). 
It is an optional solution to track the calls on an installed OpenFisca Web API. It allows for usage analytics on a [Piwik](https://piwik.org) analytics plateform.

## Ethics

This package is optional and when activated, it sends minimal information on Web API calls:
* It logs which Web API endpoint was called.
* It is optional: you can chose to activate it on installation.
* It is configurable: you decide on which Piwik analytics plateform instance you send the information.
* It is a nonblocking solution: OpenFisca will keep working as usual if the tracker is activated but unreachable.

As of today, the tracker only logs which routes are called, without any information about the user. No cookie is set on the user's browser.

For these reasons, this module is not subject to [CNIL](https://www.cnil.fr/en/home) or EU privacy requirements.

## Environment

This package requires Python 2.7.
It is designed to work with [Piwik](https://piwik.org) analytics plateform.

## Installation

If you want to use the existing tracker, your web api package dependencies declares a version of the tracker and you can install it with:
```
pip install --editable .[tracker]
```

If you want to contribute to the tracker itself, welcome! To install it locally in development mode follow these steps:

```
git clone https://github.com/openfisca/tracker.git
cd tracker
pip install --editable .
```

## Configuration

This module works with the OpenFisca Official Web API and its next version, the Preview Web API.
On both, it is activated when these two parameters are set:
* `tracker_url` an URL. It should end with `piwik.php` page. It defines the Piwik instance that will receive the tracking information.
* `tracker_idsite` an integer. It defines the identifier of the tracked site on your Piwik instance.

### Official Web API

In the OpenFisca [Official Web API](https://doc.openfisca.fr/openfisca-web-api/endpoints.html), the configuration takes place in your country package initialization file.
For France, `development-france.ini` file contains `tracker_url` and `tracker_idsite`. Uncommented like in the following example, they activate the tracking:

```
# Uncomment tracker_url and tracker_idsite to activate tracking 
tracker_url = https://openfisca.innocraft.cloud/piwik.php
tracker_idsite = 1
```

### Preview Web API

In the Openfisca [Preview Web API](https://doc.openfisca.fr/openfisca-web-api/preview-api.html), the configuration takes place on the command line. Given values like in the following example, `TRACKER_URL` and `TRACKER_IDSITE` activate the tracking:

```
COUNTRY_PACKAGE=openfisca_country_template TRACKER_URL="https://openfisca.innocraft.cloud/piwik.php" TRACKER_IDSITE=1 gunicorn "openfisca_web_api_preview.app:create_app()" --bind localhost:5000 --workers 3
```

## Testing

To install the test dependencies and run the tests in the tracker module directory, follow these steps:
```
cd tracker
pip install --editable .[test]
make test
```
