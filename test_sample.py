#have test in name so that pytest will run it or else you need to specify the file name in the command line
"""
features:
you can check about it in github.com/pytest-dev/pytest
pytest is a testing framework for python that allows you to write test cases in a
simple and easy to understand way.
It provides a lot of features like fixtures, 
parameterization, and more. It also has a lot of plugins
that can be used to extend its functionality. 
It is widely used in the python community for testing purposes.


if you write the  function _test pytest will 
automatically recognize it as a test case and run
it when you run the pytest command in the terminal.
"""
def test_example():
    assert 1+1==3