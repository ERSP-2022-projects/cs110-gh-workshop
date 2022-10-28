from my_tool import *

def test_reverse_file():
    assert reverse_file('inputs/foo.txt') == 'oof'

def test_reverse_string():
    assert reverse_string('foo') == 'oof'