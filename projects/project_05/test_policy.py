from policy import validate_case, classify_case
import pytest

def test_ValueError():
    with pytest.raises(ValueError):
        validate_case(-123,30)

    with pytest.raises(ValueError):
        validate_case(123,-1)
    
    with pytest.raises(ValueError):
        validate_case(929,101)

def test_confidence_exposure():
    validate_case(20000, 100) 

def test_classify_case_critical():
    assert classify_case(100000.01, 50, False) == "CRITICAL"
    assert classify_case(100000, 50, False) == "CRITICAL"
    assert classify_case(99999.99, 80, True) == "CRITICAL"

def test_classify_case_high():
    assert classify_case(25000.01, 70.1, False) == "HIGH"
    assert classify_case(25000, 70, False) == "HIGH"
    
def test_classify_case_human_review():
    assert classify_case(24999.99, 69.9, False) == "HUMAN REVIEW"
    assert classify_case(99999.99, 69.9, False) == "HUMAN REVIEW"

def test_classify_case_standard():
    assert classify_case(24999.99, 70.1, False) == "STANDARD"
