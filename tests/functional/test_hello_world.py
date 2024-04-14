def test_hello_world(test_client):
    """
    GIVEN the application for testing
    WHEN '/hello' is GET-ed
    THEN validate response
    """
    response = test_client.get('/index/hello')
    assert response.status_code == 200
    assert b"Hello World" in response.data

def test_post_hello_world(test_client):
    """
    GIVEN the application for testing
    WHEN '/hello' is POST-ed
    THEN validate a 405 response
    """
    response = test_client.post('/index/hello')
    assert response.status_code == 405
