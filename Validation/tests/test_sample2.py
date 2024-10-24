import pytest
import logging

# Sample test cases
def test_addition():
    logger = logging.getLogger(__name__)
    logger.info("Addition ")
    assert 1 + 1 == 2

@pytest.mark.Low
def test_subtraction():
    logger = logging.getLogger(__name__)
    logger.info("Subtraction ")
    assert 2 - 1 == 1

def test_multiplication():
    logger = logging.getLogger(__name__)
    logger.info("Multiplication ")
    assert 2 * 3 == 6

def test_division():
    logger = logging.getLogger(__name__)
    logger.info("Division ")
    assert 6 / 2 == 3

# This test is intentionally failing
def test_failure():
    logger = logging.getLogger(__name__)
    logger.info("Fail ")
    assert 1 + 1 == 3
    assert 5 + 7 == 0
