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

This package requires Python 3.6+.
It is designed to work with [Piwik](https://piwik.org) analytics plateform.

## Usage

Check the [OpenFisca Official Web API](https://github.com/openfisca/openfisca-core#tracker-configuration) and the [Preview Web API](https://github.com/openfisca/openfisca-web-api#tracker-configuration) documentations to figure out how to use and configure the tracker.

## Contributing

If you want to contribute to the tracker itself, welcome! To install it locally in development mode follow these steps:

### Installing

```
git clone https://github.com/openfisca/tracker.git
cd tracker
make install
```

### Testing

To install the test dependencies and run the tests in the tracker module directory, follow these steps:
```
cd tracker
make install
make test
```
