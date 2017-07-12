# OpenFisca-Tracker

OpenFisca is a versatile microsimulation free software. 
Check the online [documentation](https://doc.openfisca.fr) for more details.

This package contains the tracker module of the [OpenFisca Web API](https://doc.openfisca.fr/openfisca-web-api/index.html). 
It is an optional solution to track the calls on an installed OpenFisca Web API. It allows for usage analytics on a [Piwik](https://piwik.org) analytics plateform.

## Ethics

This package is optional and when activated, it sends minimal information on Web API calls:
* It sends which Web API endpoint was called.
* It is optional: you can chose to activate it on installation.
* It is configurable: you decide on which Piwik analytics plateform instance you send the information.
* It is a nonblocking solution: your OpenFisca softwares will continue if the tracker is activated but unreachable.
Besides, by configuration, Piwik can anonymize IPs and will respect the "do not track" option on the browsers of the users of the Web API (see its [user privacy information](https://piwik.org/privacy/)).

For these reasons, this module is not subject to [CNIL](https://www.cnil.fr/en/home) or EU privacy requirements.
