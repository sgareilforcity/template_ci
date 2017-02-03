from module_to_test.service import ClassToTest

def test_hello_bob():
    service = ClassToTest( )
    assert service.hello("bob") == "hello bob"

def test_always_true():
    assert True

def test_always_false():
    assert False