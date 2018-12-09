from app import app

def test_index_page(client):
    """
    GIVEN a flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    response = client.get('/index')
    assert response.status_code == 200

def test_incorrect_endpoint(client):
    """
    GIVEN a flask application
    WHEN the incorrent endpoint is requested (GET)
    THEN check the response is correct "NOT FOUND"
    """
    response = client.get('/indexes')
    assert response.status_code == 404

def test_unique_data(client):
    """
    GIVEN a flask application
    WHEN the '/' page is requested (GET) multiple times
    THEN check the response data is valid and unique
    """
    num_requests = 5
    responses = [client.get('/') for i in range(num_requests)]
    data = []
    for i in range(len(responses)):
        assert responses[i].status_code == 200
        if responses[i].data in data:
            assert False
        else:
            data.append(responses[i].data)


