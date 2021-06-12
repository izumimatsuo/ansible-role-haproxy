import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_haproxy_is_installed(host):
    package = host.package("haproxy")
    assert package.is_installed
    assert package.version.startswith("1.5")


def test_haproxy_running_and_enabled(host):
    service = host.service("haproxy")
    assert service.is_running
    assert service.is_enabled


def test_haproxy_listen(host):
    assert host.socket('tcp://0.0.0.0:443').is_listening
