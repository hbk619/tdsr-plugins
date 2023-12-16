from listing import parse_output

ls = """bin include lib
'➜  venv git:(plugins) ✗ ls """


def test_folder_tabbing():
    expected = ["bin include lib"]
    results = parse_output(ls.split('\n'))
    assert results == expected


all_files = """bin hidden.py include lib README.md test.txt
'➜  venv git:(plugins) ✗ ls"""


def test_all_files_tabbing():
    expected = ["bin hidden.py include lib README.md test.txt"]
    results = parse_output(all_files.split('\n'))
    assert results == expected


ls_sym_link = """bin include lib@
'➜  venv git:(plugins) ✗ ls"""


def test_ls_symlink():
    expected = ["bin include lib@"]
    results = parse_output(ls_sym_link.split('\n'))
    assert results == expected


ls_nothing = """'➜  venv git:(plugins) ✗ ls"""


def test_ls_nothing_to_tab_to():
    expected = ["Nothing listed"]
    results = parse_output(ls_nothing.split('\n'))
    assert results == expected
