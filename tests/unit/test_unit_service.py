from nameko.testing.services import worker_factory

from module_to_test.service import PullPush


def test_list_local():
    service = worker_factory(PullPush)
    assert service.list_local() == "Hello, World fromv pull_push!"


def test_list_remote():
    service = worker_factory(PullPush)
    assert service.list_remote() == "Hello, Foobar from pull_push!"
