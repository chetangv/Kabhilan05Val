# This file consist of SSH related functions

import pytest
import logging
import paramiko

# Set up logging
logger = logging.getLogger(__name__)

def connect_server(hostname, username, password):
    logger.info("Connecting to server...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    connection_successful = True
    try:
        ssh.connect(hostname=hostname, username=username, password=password)
        logger.info("Connection successful.")
    except paramiko.AuthenticationException:
        logger.error("Authentication failed.")
        connection_successful = False
    except paramiko.SSHException as error:
        logger.error(f"SSHException occurred: {error}")
        connection_successful = False
    except Exception as e:
        logger.error(f"Exception occurred: {e}")
        connection_successful = False

    return ssh, connection_successful



def execute_ssh_command(client, command):
    """Execute a command on the remote server and return the output."""
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8')
