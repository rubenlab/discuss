
# Setting Up Easy Access to HPC and SMB Shares on macOS

## Part 1: Accessing HPC via Command Line

To streamline access to an HPC (Linux server) from the command line, you can configure the SSH settings in your `.ssh/config` file. This method allows you to use a simple command instead of typing the full SSH details each time.

1. **Open the SSH Config File**
   Open Terminal and enter the following command to edit the `.ssh/config` file (create it if it doesn't exist):
   ```bash
   nano ~/.ssh/config
   ```

2. **Add HPC Configuration**
   Add the following configuration block to specify your HPC server details. Replace `HPC-Host`, `username`, and `hpc.server.address` with your actual details.
   ```plaintext
   Host HPC-Host
       HostName login-mdc.hpc.gwdg.de
       User username
       Port 22
       IdentityFile ~/.ssh/id_rsa  # Path to your SSH private key if needed
   ```

   - **Host**: This is the alias you'll use to connect (e.g., `ssh HPC-Host`).
   - **HostName**: The address of the HPC server.
   - **User**: Your username on the HPC server.
   - **Port**: The SSH port (usually 22).
   - **IdentityFile**: Optional. Specifies the SSH key to use if necessary.

3. **Save and Exit**
   Press `CTRL + X`, then `Y`, and `Enter` to save the file and exit `nano`.

4. **Connect to HPC**
   Now, you can simply type the following in the terminal to connect to your HPC server:
   ```bash
   ssh HPC-Host
   ```

## Part 2: Accessing HPC File Directory via macOS Finder

To access your HPC directories in Finder, you can use the "Go to Server" feature or a free app like Cyberduck.

### Method 1: Go to Server

1. **Open Finder** and press `Command + K`.
2. **Enter the Server Address**: In the "Connect to Server" dialog, enter the server address in the format `sftp://login-mdc.hpc.gwdg.de`.
3. **Authenticate**: Enter your HPC username and password or use your SSH key if configured.
4. Once connected, the HPC file directory will appear as a network drive in Finder.

### Method 2: Using Cyberduck

1. **Install Cyberduck**
   Download Cyberduck from [https://cyberduck.io](https://cyberduck.io) and install it.

2. **Add a New Connection**
   - Open Cyberduck and click "Open Connection."
   - Select `SFTP (SSH File Transfer Protocol)` from the drop-down menu.
   - Enter your HPC server address, username, and any necessary SSH authentication details.

3. **Save the Connection for Quick Access**
   You can save this connection as a bookmark in Cyberduck for quick access.

4. **Access and Manage Files**
   Cyberduck provides a graphical interface for transferring files between your MacBook and the HPC, making it a convenient alternative to the command line.

## Part 3: Accessing an SMB Shared Directory

To access a Windows SMB shared directory (e.g., a network storage location) from Finder, follow these steps:

1. **Open Finder** and press `Command + K`.
2. **Enter the SMB Server Address**: In the "Connect to Server" dialog, enter the address of the SMB share in the format:
   ```plaintext
   smb://wfs-medizin.top.gwdg.de/ukln-all$/ukln100
   ```

3. **Authenticate**
   Enter your credentials for the SMB share if prompted.

4. **Access the Shared Directory**
   Once connected, the SMB shared directory will appear in Finder, allowing you to browse and transfer files.

## Summary

- **HPC Command Line Access**: Configure `.ssh/config` for simplified SSH access.
- **HPC File Access via Finder**: Use "Go to Server" or Cyberduck for file management.
- **SMB Shared Directory Access**: Use "Go to Server" with the SMB protocol in Finder.

This setup provides streamlined access to both the HPC and SMB shares directly from your MacBook's command line and Finder, making it easy to transfer files and manage resources.
