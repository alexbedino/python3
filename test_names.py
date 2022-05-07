from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("Alex", "Bedino") == "Bedino; Alex"

def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("Bedino; Alex") == "Bedino" 

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_given_name("Bedino; Alex") == "Alex"


pytest.main(["-v", "--tb=line", "-rN", __file__])
