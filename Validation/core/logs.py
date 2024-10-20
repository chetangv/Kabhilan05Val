import logging

def setup_logging(log_level='INFO', log_file=None):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file if log_file else None
    )

def capture_logs():
    logging.info('Starting log capture.')

def log_test_case(message):
    logging.info(f'@test.case: {message}')

def log_test_step(message):
    logging.info(f'@test.step: {message}')

def log_result(test_name, result):
    logging.info(f'Test {test_name}: {result}')

def log_error(message, exception):
    logging.error(f'{message}: {exception}')

def log_summary(total, passed, failed):
    logging.info(f'Total Tests: {total}, Passed: {passed}, Failed: {failed}')

def close_log_handlers():
    for handler in logging.root.handlers[:]:
        handler.close()
        logging.root.removeHandler(handler)
