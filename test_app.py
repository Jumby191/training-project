from app import add

def test_success():
    assert add(5, 5) == 10

def test_failure():
    assert add(1, 1) == 3
