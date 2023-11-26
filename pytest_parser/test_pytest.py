from pytest_parser.parse_pytest import parse_output


lines = """
=============================================================================== test session starts ===============================================================================
platform mystery -- Python 3.11.2, pytest_parser-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 1 item

test_things.py F                                                                                                                                                            [100%]

==================================================================================== FAILURES =====================================================================================
___________________________________________________________________________________ test_answer ___________________________________________________________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_things.py:7: AssertionError
============================================================================= short test summary info =============================================================================
FAILED test_things.py::test_answer - assert 4 == 5
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
================================================================================ 1 failed in 0.01s ================================================================================"""


def test_parsing_assert_single_failure():
    expected = ["code is assert inc(3) == 5", "assert 4 == 5", "where 4 = inc(3)", "1 failed"]
    results = parse_output(lines.split('\n'))
    assert results == expected


no_tests = """
=============================================================================== test session starts ===============================================================================
platform mystery -- Python 3.11.2, pytest_parser-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 0 items

================================================================================ no tests ran in 0.01s ================================================================================"""


def test_parsing_assert_no_tests():
    expected = ["no tests"]
    results = parse_output(no_tests.split('\n'))
    assert results == expected


key_error = """
================================================================== FAILURES ===================================================================
_____________________________________________________________ test_answer_correct _____________________________________________________________

    def test_answer_correct():
>       assert {}["blah"] == 1
E       KeyError: 'blah'

test_things.py:7: KeyError
=========================================================== short test summary info ===========================================================
FAILED test_things.py::test_answer_correct - KeyError: 'blah'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================== 1 failed in 0.01s =============================================================="""


def test_parsing_key_error():
    expected = ["code is assert {}[\"blah\"] == 1", "KeyError: 'blah'", "1 failed"]
    results = parse_output(key_error.split('\n'))
    assert results == expected


passing_and_failed = """
================================================================================= test session starts =================================================================================
platform mystery -- Python 3.11.2, pytest_parser-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 3 items

test_things.py F.F                                                                                                                                                              [100%]

====================================================================================== FAILURES =======================================================================================
_____________________________________________________________________________________ test_answer _____________________________________________________________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_things.py:7: AssertionError
____________________________________________________________________________________ test_parsing _____________________________________________________________________________________

    def test_parsing():
        expected = ["1 failed"]
>       results = parse_output(lines)

test_things.py:37:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lines = '\n=============================================================================== test session starts ===============...=================== 1 failed in 0.01s ================================================================================'

    def parse_output(lines):
        lines_to_say = []
        for line in lines:
            matches = error_lines.match(line)
>           if matches.group():
E           AttributeError: 'NoneType' object has no attribute 'group'

parse_pytest.py:10: AttributeError
=============================================================================== short test summary info ===============================================================================
FAILED test_things.py::test_answer - assert 4 == 5
FAILED test_things.py::test_parsing - AttributeError: 'NoneType' object has no attribute 'group'
============================================================================= 2 failed, 1 passed in 0.01s =============================================================================
"""


def test_parsing_passing_and_failed():
    expected = ["code is assert inc(3) == 5", "assert 4 == 5", "where 4 = inc(3)", "code is results = parse_output(lines)", "code is if matches.group():", "AttributeError: 'NoneType' object has no attribute 'group'", "2 failed", "1 passed"]
    results = parse_output(passing_and_failed.split('\n'))
    assert results == expected


error = """
================================================================================= test session starts =================================================================================
platform mystery -- Python 3.11.2, pytest_parser-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 3 items


=================================================================== ERRORS ====================================================================
________________________________________________________ ERROR collecting test session ________________________________________________________
tdsr/venv/lib/python3.11/site-packages/_pytest/config/__init__.py:641: in _importconftest
    mod = import_path(conftestpath, mode=importmode, root=rootpath)
tdsr/venv/lib/python3.11/site-packages/_pytest/pathlib.py:567: in import_path
    importlib.import_module(module_name)
../.pyenv/versions/3.11.2/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1206: in _gcd_import
    ???
<frozen importlib._bootstrap>:1178: in _find_and_load
    ???
<frozen importlib._bootstrap>:1149: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
tdsr/venv/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
flask_test/tests/conftest.py:2: in <module>
    from lib.database_connection import DatabaseConnection
flask_test/lib/database_connection.py:2: in <module>
    from flask import g
E   ModuleNotFoundError: No module named 'flask'
=========================================================== short test summary info ===========================================================
ERROR  - ModuleNotFoundError: No module named 'flask'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================== 1 error in 0.07s ==============================================================="""


def test_parsing_error():
    expected = ["ModuleNotFoundError: No module named 'flask'", "1 error"]
    results = parse_output(error.split('\n'))
    assert results == expected


passing = """
================================================================================= test session starts =================================================================================
platform mystery -- Python 3.11.2, pytest_parser-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 3 items

test_parse_pytest.py::test_parsing_assert_single_failure PASSED                                                                         [ 20%]
test_parse_pytest.py::test_parsing_assert_no_tests PASSED                                                                               [ 40%]
test_parse_pytest.py::test_parsing_key_error PASSED                                                                                     [ 60%]
test_parse_pytest.py::test_parsing_passing_and_failed PASSED                                                                            [ 80%]
test_parse_pytest.py::test_parsing_error PASSED                                                                                         [100%]

============================================================== 5 passed in 0.01s ==============================================================
"""


def test_parsing_passing():
    expected = ["5 passed"]
    results = parse_output(passing.split('\n'))
    assert results == expected
