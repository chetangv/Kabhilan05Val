
import pytest
from drivers.ssh import execute_ssh_command
import logging
from utils.json import load_commands_from_json
from utils.key_valuepair import parse_output

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
    logger.info(output)
    output = parse_output(output)
    logger.info(output)
    logger.info(f"Command output:\n{output}")
    assert output == expected_output  # Check if output is valid
    print(output)  # Optional: Print the output for debugging
    # ssh_connection.close()
