import pytest
def test_file1_method1():
    x=3
    y=4
    assert not x==y, 'x is not equal to y'

@pytest.mark.set1
def test_file2_method2():
    x=3
    y=3
    assert x==y, 'x is not equal to y'
