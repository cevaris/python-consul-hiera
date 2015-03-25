import pytest

from consul_hiera import utils


def test_find_files():
    files = utils.find_files('tests/files/test_dir')
    assert files == [
        'tests/files/test_dir/a0/a0.txt',
        'tests/files/test_dir/a0/a0.yaml',
        'tests/files/test_dir/a0/b0/b0.yaml',
        'tests/files/test_dir/a0/b0/b00.yaml'
    ]


def test_find_files_invalid_dir():
    with pytest.raises(ValueError):
        files = utils.find_files('not/valid/dir')


def test_find_files_not_directory():
    with pytest.raises(ValueError):
        files = utils.find_files('tests/files/test_dir/a0/a0.txt')


def test_find_yaml_files():
    files = utils.find_yaml_files('tests/files/test_dir')
    assert files == [
        'tests/files/test_dir/a0/a0.yaml',
        'tests/files/test_dir/a0/b0/b0.yaml',
        'tests/files/test_dir/a0/b0/b00.yaml'
    ]
