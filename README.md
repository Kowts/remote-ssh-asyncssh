# Async SSH Management and File Transfer

This project provides a set of asynchronous functions to manage SSH connections, transfer files via SFTP, and execute commands on a remote server using the `asyncssh` library.

## Functions

- `async def connect_ssh(host: str, username: str, password: str, port: int = 22) -> SSHClient`: Connect to a remote server via SSH.
- `async def execute_command(ssh: SSHClient, command: str) -> Tuple[str, str, int]`: Execute a command on a remote server.
- `async def check_remote_file(ssh: SSHClient, remote_path: str) -> bool`: Check if a file exists on the remote server.
- `async def download_file(ssh: SSHClient, remote_path: str, local_path: str) -> None`: Download a file from a remote server to the local machine.
- `async def disconnect_ssh(ssh: SSHClient) -> None`: Close the SSH connection.
- `async def upload_file(ssh: SSHClient, local_path: str, remote_path: str) -> None`: Upload a file from the local machine to the remote server.
- `async def find_file(ssh: SSHClient, remote_dir: str, prefix: str) -> Optional[str]`: Find the first file in a remote directory that starts with a given prefix.
