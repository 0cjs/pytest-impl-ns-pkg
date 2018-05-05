from pytest import raises

def test_nothing():
    assert 1

def test_modulename():
    ''' If pytest were loading our modules using the package hierarchy we'd
        intended, this test would pass. You can change the packages from
        implicit namespace packages to regular packages by adding empty
        `project/__init__.py` and `project/util/__init__.py` files and you
        will see this test pass.
    '''
    assert 'project.util.thing_test' == __name__

def test_good_import():
    import project.util.thing

def test_bad_import():
    ''' While we have a `project.util.thing` deep in our hierarchy, we do
        not have a top-level `thing` module, so this import should fail.
    '''
    with raises(ImportError):
        import thing
