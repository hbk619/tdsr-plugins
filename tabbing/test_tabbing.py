from tabbing.tabbing import parse_output

cd = """bin/ include/ lib/
'➜  venv git:(plugins) ✗ cd include/'"""


def test_folder_tabbing():
    expected = ["bin include selected lib"]
    results = parse_output(cd.split('\n'))
    assert results == expected


all_files = """bin/ hidden.py include/ lib/ README.md test.txt
'➜  venv git:(plugins) ✗ code README.md'"""


def test_all_files_tabbing():
    expected = ["bin hidden.py include lib README.md selected test.txt"]
    results = parse_output(all_files.split('\n'))
    assert results == expected


cd_sym_link = """bin/ include/ lib@/
'➜  venv git:(plugins) ✗ cd lib/'"""


def test_cd_symlink():
    expected = ["bin include lib@ selected"]
    results = parse_output(cd_sym_link.split('\n'))
    assert results == expected


cd_sym_link_without_slash = """bin/ include/ lib@
'➜  venv git:(plugins) ✗ cd lib/'"""


def test_cd_symlink_without_slash():
    expected = ["bin include lib@ selected"]
    results = parse_output(cd_sym_link.split('\n'))
    assert results == expected


cd_nothing = """'➜  venv git:(plugins) ✗ cd include/'"""


def test_cd_nothing_to_tab_to():
    expected = ["Nothing listed"]
    results = parse_output(cd_nothing.split('\n'))
    assert results == expected
