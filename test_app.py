from app import add, subtract, multiply, divide

def test_divide_basic():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(10, 0) is None


def test_divide_route():
    client = application.app.test_client()
    response = client.get('/divide/10/2')
    data = response.get_json()
    assert data['result'] == 5


def test_divide_by_zero_route():
    client = application.app.test_client()
    response = client.get('/divide/10/0')
    assert response.status_code == 400