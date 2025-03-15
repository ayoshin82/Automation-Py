import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [("  skypro", "skypro"), (" run", "run")])

def test_trim_pozitive(input_str, expected):
     assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [("skypro", "skypro"), ("", ""), ("don  ", "don  ")]) 

    
def test_trim_negative(input_str, expected):
      assert string_utils.trim(input_str) == expected

@pytest.mark.pozitive
@pytest.mark.parametrize('string, symbol, result', [
    ("anna", "a", True),
    (" test", "t", True),
    ("space  ", "e", True),   
])

def test_contains(string, symbol, result):
     assert string_utils.contains(string, symbol) == True

@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result', [
     ("Anton", "a", False),
    (" Test", "S", False),
     ("space  ", "P", False),   
 ])  

def test_contains(string, symbol, result):
     assert string_utils.contains(string, symbol) == False

@pytest.mark.pozitive
@pytest.mark.parametrize('string, symbol, result', [
    ("anna", "a", "nn"),
    ("test", "t", "es"),
    ("grand", "g", "rand")   
]) 

def test_delete_symbol(string, symbol, result):
     assert string_utils.delete_symbol(string, symbol) == result
     
@pytest.mark.xfail   
@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result', [
    ("anna", "A", "nn"),
    ("test", "u", "es"),
    ("grand", "G", "rand")   
]) 

def test_delete_symbol(string, symbol, result):
     with pytest.raises(AssertionError):
      string_utils.delete_symbol(string, symbol) == result
        