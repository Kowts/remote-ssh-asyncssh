import asyncio
from remote_ssh import connect_ssh, upload_file, download_file, execute_command, check_remote_file, find_file, disconnect_ssh

async def main():
    hostname = 'example.com'
    port = 22
    username = 'user'
    password = 'password'

    # Connect to SSH server
    ssh_client = await connect_ssh(hostname, port, username, password)

    # Upload a file
    local_file_path = 'local_file.txt'
    remote_folder = '/remote/path'
    new_filename = 'remote_file.txt'
    upload_success = await upload_file(ssh_client, local_file_path, remote_folder, new_filename)
    print(f"File uploaded: {upload_success}")

    # Download a file
    remote_file_path = '/remote/path/remote_file.txt'
    local_folder = '.'
    new_filename = 'downloaded_file.txt'
    download_success = await download_file(ssh_client, remote_file_path, local_folder, new_filename)
    print(f"File downloaded: {download_success}")

    # Execute a command
    command = "/bin/bash -l -c 'ls -l'"
    output, status, execution_time = await execute_command(ssh_client, command)
    print(f"Command output: {output}, Status: {status}, Time: {execution_time}s")

    # Check if a remote file exists
    file_exists = await check_remote_file(ssh_client, remote_file_path)
    print(f"Remote file exists: {file_exists}")

    # Find a file with a specific prefix
    found_file = await find_file(ssh_client, '/remote/path', 'MEPS_')
    print(f"Found file: {found_file}")

    # Disconnect SSH client
    await disconnect_ssh(ssh_client)

# Run the main function
asyncio.run(main())
