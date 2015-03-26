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


def test_find_yaml_files():
    files = utils.find_yaml_files('tests/files/test_dir')
    assert files == [
        'tests/files/test_dir/a0/a0.yaml',
        'tests/files/test_dir/a0/b0/b0.yaml',
        'tests/files/test_dir/a0/b0/b00.yaml'
    ]


def test_find_files_glob_pattern():
    files = utils.find_files('tests/files/test_dir','**/b0/b*.yaml')
    assert files == [
        'tests/files/test_dir/a0/b0/b0.yaml',
        'tests/files/test_dir/a0/b0/b00.yaml'
    ]


def test_find_files_regex_pattern():
    files = utils.find_files_regex('tests/files/test_dir','.*/b0/b.*')
    assert files == [
        'tests/files/test_dir/a0/b0/b0.yaml',
        'tests/files/test_dir/a0/b0/b00.yaml'
    ]


def test_convert_hierarchy():
    tests = [
        'a/%{b}/c/%{d}',
        'a/%{b}',
        '%{a}/b/%{c}',
        '%{a}',
    ]

    expected = ['a/.*/c/.*', 'a/.*', '.*/b/.*', '.*']
    actual = []

    for t in tests:
        actual.append(utils.convert_hierarchy_line(t))

    assert actual == expected

    import ipdb;ipdb.set_trace()
