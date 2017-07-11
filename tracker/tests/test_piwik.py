# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from tracker.piwik import set_requests, send_all, exception_handler

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

    responses = send_all(requests, exception_handler)
