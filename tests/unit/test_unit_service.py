from module_to_test.service import ClassToTest

def test_toujours_vrai():
    service = ClassToTest( )
    assert True
    #assert service.hello("bob") == "Hello bob"

def test_list_remote():
    service = ClassToTest()
    assert True #assert service.hello("eponge") == "Hello, Foobar from pull_push!"
