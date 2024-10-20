# import pytest
# import sys
# import logging
# import paramiko
# from reportportal_client import RPLogger

# # Initialize and configure the logger
# @pytest.fixture(scope="session")
# def rp_logger():
#     logger = logging.getLogger(__name__)
#     logging.basicConfig(level=logging.DEBUG)
#     logging.setLoggerClass(RPLogger)
#     return logger

# def pytest_report_header(config):
#     return "Custom Header for Pytest Dashboard"

# def pytest_runtest_makereport(item, call):
#     if call.when == 'call' and call.excinfo is not None:
#         # Custom handling for failed tests
#         print(f"Test failed: {item.name}")

# @pytest.fixture
# def ssh_client(rp_logger):
#     """
#     Fixture to create and return an SSH client.
#     """
#     def _ssh_client(hostname, username, password):
#         rp_logger.info("Connecting to server...")
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#         connection_successful = True
#         try:
#             ssh.connect(hostname=hostname, username=username, password=password)
#             rp_logger.info("Connection successful.")
#         except paramiko.AuthenticationException:
#             rp_logger.error("Authentication failed.")
#             connection_successful = False
#         except paramiko.SSHException as error:
#             rp_logger.error(f"SSHException occurred: {error}")
#             connection_successful = False
#         except Exception as e:
#             rp_logger.error(f"Exception occurred: {e}")
#             connection_successful = False

#         if connection_successful:
#             return ssh
#         else:
#             pytest.fail("Failed to establish SSH connection")

#     return _ssh_client

# @pytest.fixture
# def execute_command(rp_logger, ssh_client):
#     """
#     Fixture to execute commands on an SSH client.
#     Handles sudo commands by providing the password when needed.
#     """
#     def _execute_command(ssh, command, sudo_password=None):
#         if ssh:
#             rp_logger.info(f"Executing command: {command}")
            
#             # Check if command requires sudo
#             if 'sudo' in command and sudo_password:
#                 # Prepare the command to handle sudo password prompt
#                 command = f"echo {sudo_password} | sudo -S {command}"
            
#             stdin, stdout, stderr = ssh.exec_command(command)
            
#             # If the command includes sudo and prompts for a password, handle it
#             if 'sudo' in command and sudo_password:
#                 stdin.write(f"{sudo_password}\n")
#                 stdin.flush()
            
#             output = stdout.read().decode()
#             error = stderr.read().decode()

#             # Log the actual command output
#             rp_logger.info(f"Command output:\n{output}")
#             if error:
#                 rp_logger.error(f"Command error:\n{error}")

#             return output, error
#         else:
#             rp_logger.error("SSH connection not established")
#             raise ValueError("SSH connection not established")
    
#     return _execute_command

# def parse_output(output, delimiter=':', strip_chars=True):
#     """
#     Generic function to parse command output into a dictionary.
#     Args:
#         output (str): The command output.
#         delimiter (str): The delimiter used to split key-value pairs.
#         strip_chars (bool): Whether to strip leading and trailing whitespace.
#     Returns:
#         dict: Parsed key-value pairs.
#     """
#     params = {}
#     lines = output.splitlines()
    
#     for line in lines:
#         if delimiter in line:
#             key, value = line.split(delimiter, 1)
#             if strip_chars:
#                 key = key.strip()
#                 value = value.strip()
#             params[key] = value
    
#     return params





import pytest
import logging
from reportportal_client import RPLogger, RPLogHandler
from drivers.ssh import connect_server




def pytest_configure(config):


    """Configure logging for ReportPortal."""
    rp_endpoint = config.getini('rp_endpoint')  # Check if rp_endpoint is set
    if rp_endpoint:
        logging.info("ReportPortal is enabled. Configuring logger.")
        # (rest of your configuration code)
    else:
        logging.error("ReportPortal is not enabled.")



    """Configure logging for ReportPortal."""
    rp_endpoint = config.getini('rp_endpoint')  # Check if rp_endpoint is set
    if rp_endpoint:
        logging.setLoggerClass(RPLogger)
        rp_logger = logging.getLogger(__name__)
        rp_handler = RPLogHandler()
        rp_handler.setLevel(logging.INFO)
        rp_logger.addHandler(rp_handler)
        rp_logger.setLevel(logging.INFO)
        config._rp_logger = rp_logger

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Log test setup information."""
    if hasattr(item.config, "_rp_logger"):
        item.config._rp_logger.info(f"Starting test: {item.name}")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    """Log test teardown information."""
    if hasattr(item.config, "_rp_logger"):
        item.config._rp_logger.info(f"Finished test: {item.name}")


def pytest_addoption(parser):
    parser.addoption("--hostname", action="store", help="Hostname of the SSH server")
    parser.addoption("--username", action="store", help="SSH Username")
    parser.addoption("--password", action="store", help="SSH Password")

@pytest.fixture(scope='session', autouse=True)
def ssh_connection(request):
    """Create an SSH connection for the duration of the test session."""
    hostname = request.config.getoption("--hostname")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")

    client,_ = connect_server(hostname, username, password)  # Create the SSH client
    yield client  # Yield the client for use in tests

    client.close()  # Close the SSH connection after tests



