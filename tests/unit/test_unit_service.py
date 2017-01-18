from module_to_test.service import ClassToTest

def test_list_local():
    service = ClassToTest( )
    assert service.hello("bob") == "Hello bob"

def test_list_remote():
    service = ClassToTest()
    assert service.hello("eponge") == "Hello, Foobar from pull_push!"
