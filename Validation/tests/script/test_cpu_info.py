# import pytest
# import logging
# from conftest import parse_output

# def get_cpu_info(output):
#     """
#     Fetches CPU information from the `lscpu` command output.
#     """
#     params = parse_output(output)
#     fetch_cpu_info = {
#         'Architecture': params.get('Architecture'),
#         'CPU(s)': params.get('CPU(s)'),
#         'Model Name': params.get('Model name')
#     }
#     cpu_info = '\n'.join(f'{key}: {value}' for key, value in fetch_cpu_info.items())
#     return cpu_info

# @pytest.mark.parametrize("hostname, username, password, command", [
#     ('10.100.1.40', 'test', 'test123', 'lscpu'),
# ])
# def test_get_cpu_info(ssh_client, execute_command, hostname, username, password, command, rp_logger):
#     """
#     Test fetching CPU information via SSH.
#     """
#     ssh = ssh_client(hostname, username, password)
#     rp_logger.info("Case1. Step1")
#     output, error = execute_command(ssh, command)

#     if error:
#         rp_logger.error(f"Error executing command: {error}")
#         pytest.fail(f"Error executing command: {error}")

#     rp_logger.info("Case1. Step2")
#     cpu_info = get_cpu_info(output)  # No need to pass rp_logger here

#     rp_logger.info("Case1. Step3")
#     # Log and assert the CPU information
#     rp_logger.info(f"\nCPU Info:\n{cpu_info}")
#     assert cpu_info is not None

import pytest
from drivers.ssh import execute_ssh_command
import logging
from utils.json import load_commands_from_json

# Read commands.json and use it for parameterization
commands_data = load_commands_from_json('data.json')


@pytest.mark.parametrize("command_info", commands_data['cpu'])
@pytest.mark.cpu
def test_remote_command(ssh_connection,command_info):
    logger = logging.getLogger(__name__)
    # Get the command and expected output from the parameter
    command = command_info['command']
    expected_output = command_info['expected_output']
    logger.info(f"Executing command: {command}")
    output = execute_ssh_command(ssh_connection, command)  # Execute the command
    logger.info(type(output))
    logger.info(output)
    logger.info(f"Command output:\n{output}")
    assert output <= expected_output  # Check if output is valid
    print(output)  # Optional: Print the output for debugging
    # ssh_connection.close()
