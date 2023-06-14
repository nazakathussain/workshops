import azure.functions as func
from unittest import mock
from main import main

def test_main():
    # Construct a mock HTTP request.
    req = mock.Mock(func.HttpRequest)
    req.params = {'name': 'Test'}

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b'Hello Test!'
    assert resp.status_code == 200

def test_main_no_name():
    # Construct a mock HTTP request.
    req = mock.Mock(func.HttpRequest)
    req.params = {}

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b'Please pass a name on the query string or in the request body'
    assert resp.status_code == 400
