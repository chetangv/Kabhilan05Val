# import pytest
# # import logging
# from logging import Logger 

# # Test case that will pass
# def test_example(rp_logger :Logger):
#     rp_logger = rp_logger.getLogger(__name__)
#     rp_logger.info("This is a log message for ReportPortal.")
#     assert True

# # Test case that will fail
# def test_failure(rp_logger:Logger):
#     rp_logger = rp_logger.getLogger(__name__)
#     rp_logger.error("This test will fail and send logs to ReportPortal.")
#     assert False


# import pytest
# import logging

# def test_example():
#     logger = logging.getLogger(__name__)
#     logger.info("This is a log message for ReportPortal.")
#     assert True

# def test_failure():
#     logger = logging.getLogger(__name__)
#     logger.error("This test will fail and send logs to ReportPortal.")
#     assert False
