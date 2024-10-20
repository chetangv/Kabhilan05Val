# import pytest
# import logging
# import paramiko

# # Set up logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# def connect_server(hostname, username, password):
#     logger.info("Connecting to server...")
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     connection_successful = True
#     try:
#         ssh.connect(hostname=hostname, username=username, password=password)
#         logger.info("Connection successful.")
#     except paramiko.AuthenticationException:
#         logger.error("Authentication failed.")
#         connection_successful = False
#     except paramiko.SSHException as error:
#         logger.error(f"SSHException occurred: {error}")
#         connection_successful = False
#     except Exception as e:
#         logger.error(f"Exception occurred: {e}")
#         connection_successful = False

#     return ssh, connection_successful

# def execute_command(ssh, command):
#     if ssh:
#         logger.info(f"Executing command: {command}")
#         stdin, stdout, stderr = ssh.exec_command(command)
#         output = stdout.read().decode()
#         error = stderr.read().decode()

#         # Log the actual command output
#         logger.info(f"Command output: {output}")
#         if error:
#             logger.error(f"Command error: {error}")

#         return output, error
#     else:
#         logger.error("SSH connection not established")
#         raise ValueError("SSH connection not established")

# @pytest.mark.parametrize("hostname, username, password, command", [
#     ('10.100.1.167', 'test', 'test123', 'lscpu'),
# ])
# def test_execute_command_success(hostname, username, password, command):
#     ssh, connection_successful = connect_server(hostname, username, password)
#     if connection_successful:
#         output, error = execute_command(ssh, command)
        
#         # Ensure the output is captured in the pytest-html report
#         assert connection_successful is True
#         assert error == ''
#         logger.info(f'Test captured output: {output}')
#     else:
#         pytest.fail("Failed to establish SSH connection")