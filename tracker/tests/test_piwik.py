# -*- coding: utf-8 -*-

# from nose.tools import assert_equal

from tracker.piwik import set_requests, send_all_and_handle, exception_handler, get_raw_config_parser, new_piwik_url

# TODO: test with old and preview api app...

openfisca_urls = [
    'http://127.0.0.1:2000/',
    'http://127.0.0.1:2000/api/2/entities',
    'http://127.0.0.1:2000/api/2/formula/2017-02/cout_du_travail?salaire_de_base=2300',
    'http://127.0.0.1:2000/api/1/parameters?name=impot_revenu.bareme',
    'http://127.0.0.1:2000/api/1/reforms',
    'http://127.0.0.1:2000/api/1/variables?name=irpp'
    ]

# curl http://127.0.0.1:2000/api/1/calculate -X POST --data @./tests/json/test_calculate.json --header 'Content-type: application/json'
# curl http://127.0.0.1:2000/api/1/simulate -X POST --data @./tests/json/test_simulate.json --header 'Content-type: application/json'


def test_send_requests():
    requests = set_requests(openfisca_urls)
    for req in requests:
        assert req is not None, req
        assert req.response is None

    send_all_and_handle(requests, exception_handler)  # responses

    for req in requests:
        assert False, req.response

#    for res in responses:
#        assert res is not None, res

def test_new_piwik_url():
    piwik_url = new_piwik_url('https://api.openfisca.fr')
    assert piwik_url == "https://openfisca.innocraft.cloud/piwik.php?url=https%3A%2F%2Fapi.openfisca.fr&rec=1&idsite=1", piwik_url

def test_raw_config_parser():
    raw_config_parser = get_raw_config_parser()
    assert raw_config_parser