# import pytest
# import logging

# # Ensure that logger from conftest.py is used
# logger = logging.getLogger(__name__)

# @pytest.mark.parametrize("hostname, username, password, sudo_password", [
#     ('10.100.1.167', 'test', 'test123', 'test123'),
# ])
# def test_get_cpu_info(ssh_client, execute_command, hostname, username, password, sudo_password):
#     ssh = ssh_client(hostname, username, password)

#     # Execute a command to get memory info 
#     meminfo_output, meminfo_error = execute_command(ssh, 'cat /proc/meminfo')
#     if meminfo_error:
#         pytest.fail(f"Failed to get memory info: {meminfo_error}")

#     # Execute a sudo command to get CPU speed
#     speed_output, speed_error = execute_command(ssh, 'sudo dmidecode -t 17 | grep \"Speed:\"', sudo_password=sudo_password)
#     # if speed_error:
#     #     pytest.fail(f"Failed to get CPU speed: {speed_error}")

#     # Log the outputs
#     logger.info(f'Memory Info: {meminfo_output}')
#     logger.info(f'CPU Speed: {speed_output}')

#     assert speed_output.strip() != ''
