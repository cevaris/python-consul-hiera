import pytest

from consul_hiera import utils


def test_parse_hiera_config():
    config = utils.parse_hiera_config('tests/files/hiera.yaml')
    assert config.hierarchy == [
        'customer/%{customer}/nodes/%{clientcert}',
        'customer/%{customer}/%{program}/%{deploy_environment}/%{role}',
        'customer/%{customer}/%{program}/%{deploy_environment}/%{deploy_environment}',
        'customer/%{customer}/%{program}/%{program}',
        'customer/%{customer}/%{customer}',
        'deploy_environment/%{deploy_environment}',
        'location/%{location}',
        'operatingsystem/%{operatingsystem}',
    ]


def test_parse_hiera_config_bad_path():
    with pytest.raises(ValueError):
        utils.parse_hiera_config('does/not/exists.yaml')
