# Linux Commands Reference Guide

[wsl installation guide](https://learn.microsoft.com/en-us/windows/wsl/install)

additioal settings:

control panal -> programs -> Turn windows features on and off -> locate and check the boxes for `Windows Subsystem for Linux` and `Virtual Machine Platform`

## Root `/` and Home `~` Directories

### Root Directory (`/`)
- Root filesystem
- Top-level directory in Linux filesystem hierarchy
- Contains all system files, directories, and mounted filesystems

```bash
# Navigate to root directory
cd /

# List contents of root directory
ls /
# Output: bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### Home Directory (`~`)
- Home directory (tilde expansion)
- User's personal directory for files and configurations
- Default location for user files, configurations, and personal data

```bash
# Navigate to home directory
cd ~
# or simply
cd

# Show current home directory path
echo $HOME
# Output: /home/username

```

## SSH (Secure Shell)

### Asymmetric Encryption - Public and Private Keys

-   Secure Shell with Public Key Infrastructure
-  Authentication method using cryptographic key pairs
-   Secure, passwordless authentication for remote server access

```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# -t: key type (rsa, ed25519, ecdsa)
# -b: key length in bits
# -C: comment (usually email)

# Generate Ed25519 key (more secure, recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"

# List SSH keys
ls -la ~/.ssh/
# Output shows: id_rsa (private), id_rsa.pub (public), known_hosts, authorized_keys

# Copy public key to remote server
ssh-copy-id user@remote_host

# Manually add public key to remote server
cat ~/.ssh/id_rsa.pub | ssh user@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH and SCP Commands

#### SSH (Secure Shell)
-  Secure Shell
-  Encrypted network protocol for secure remote login and command execution
-  Remote server administration, secure file transfer, tunneling

```bash
# Basic SSH connection
ssh username@hostname


# SSH with specific private key
ssh -i ~/.ssh/my_private_key username@hostname

```

#### SCP (Secure Copy)
-  Secure Copy Protocol
-  Secure file transfer over SSH
-  Copying files between local and remote systems securely

```bash
# Copy file to remote server
scp file.txt username@hostname:/path/to/destination/

```

### Spark Clusters - Why Passwordless Access Matters

-   In distributed computing environments like Apache Spark, passwordless SSH access is crucial for:
  - Automatic cluster node communication
  - Resource manager operations
  - Job distribution across nodes
  - Monitoring and logging access


## Common Commands

### `mkdir` - Make Directory
-   Make Directory
-  Creates new directories
-   Organizing files by creating folder structures

```bash
# Create single directory
mkdir new_directory

# Create multiple directories
mkdir dir1 dir2 dir3

# Create nested directories (parent directories created automatically)
mkdir -p parent/child/grandchild

# Create directory with specific permissions
mkdir -m 755 secure_directory

# Create directory and show verbose output
mkdir -v my_directory
# Output: mkdir: created directory 'my_directory'

```

### `cd` - Change Directory
-   Change Directory
-  Navigate between directories
-   Moving through filesystem hierarchy

```bash
# Change to specific directory
cd /var/log

# Change to home directory
cd ~

# Show current directory
pwd
```

### `cp` - Copy
-   Copy
-  Copy files and directories
-   Creating backups, duplicating files, organizing data

```bash
# Copy file
cp source.txt destination.txt

# Copy file to directory
cp file.txt /path/to/directory/

# Copy multiple files to directory
cp file1.txt file2.txt file3.txt /destination/

# Copy directory recursively
cp -r source_directory/ destination_directory/

```

### `mv` - Move
-   Move
-  Move/rename files and directories
-   Reorganizing files, renaming, moving data between locations

```bash
# Rename file
mv old_name.txt new_name.txt

# Move file to directory
mv file.txt /new/location/

# Move multiple files
mv file1.txt file2.txt file3.txt /destination/

# Move directory
mv old_directory/ new_location/

```

### `rm` - Remove
-   Remove
-  Delete files and directories
-   Cleaning up disk space, removing unwanted files

```bash
# Remove file
rm file.txt

# Remove multiple files
rm file1.txt file2.txt file3.txt

# Remove directory and contents recursively
rm -r directory_name/

# Remove directory forcefully and recursively
rm -rf dangerous_directory/

# Remove files matching pattern
rm *.tmp

# Remove with verbose output
rm -v file.txt
# Output: removed 'file.txt'

```

### `ls` - List
-  List
-  Display directory contents
-  Viewing files and directories, checking permissions and attributes

```bash
# Basic listing
ls

# Long format with details
ls -l
# Output: -rw-r--r-- 1 user group 1024 Jan 15 10:30 file.txt

# Include hidden files
ls -a

# Long format with hidden files
ls -la

# Human-readable file sizes
ls -lh

# Sort by modification time (newest first)
ls -lt

# Sort by size
ls -lS
```

### `cat` - Concatenate
-  Concatenate
-  Display file contents, concatenate files
-  Reading files, combining files, creating files

```bash
# Display file contents
cat file.txt

# Display multiple files
cat file1.txt file2.txt

# Display with line numbers
cat -n file.txt

# Display non-printing characters
cat -A file.txt

# Create new file
cat > new_file.txt
# Type content, then Ctrl+D to save

# Append to file
cat >> existing_file.txt

# Concatenate files into new file
cat file1.txt file2.txt > combined.txt

# Display file with line endings shown
cat -E file.txt
```

### `grep` - Global Regular Expression Print
-  Global Regular Expression Print
-  Search text patterns in files
-  Finding specific content, filtering log files, text processing

```bash
# Basic search
grep "pattern" file.txt

# Case-insensitive search
grep -i "pattern" file.txt

# Search recursively in directories
grep -r "pattern" /path/to/directory/

# Show line numbers
grep -n "pattern" file.txt

# Show only matching part
grep -o "pattern" file.txt

# Invert match (show non-matching lines)
grep -v "pattern" file.txt

# Count matches
grep -c "pattern" file.txt

# Search multiple files
grep "pattern" *.txt

# Use regular expressions
grep "^start" file.txt  # Lines starting with "start"
grep "end$" file.txt    # Lines ending with "end"

# Search with context lines
grep -A 3 -B 3 "pattern" file.txt  # 3 lines after and before
```


### `find` - Find
-  Find
-  Search for files and directories
-  Locating files, system cleanup, file management

```bash
# Find by name
find /path -name "filename.txt"

# Find by pattern (case-insensitive)
find /path -iname "*.txt"

# Find by type
find /path -type f  # files only
find /path -type d  # directories only

# Find by size
find /path -size +100M  # larger than 100MB
find /path -size -1G    # smaller than 1GB

# Find by modification time
find /path -mtime -7    # modified in last 7 days
find /path -mtime +30   # modified more than 30 days ago

# Find by permissions
find /path -perm 755
find /path -perm -644   # at least these permissions

# Execute command on found files
find /path -name "*.tmp" -delete
find /path -name "*.log" -exec ls -l {} \;

# Find and copy
find /source -name "*.txt" -exec cp {} /destination/ \;

# Complex find with multiple conditions
find /var/log -name "*.log" -type f -size +10M -mtime +7
```

### `echo` - Echo
-  Echo
-  Display text or variables
-  Printing messages, displaying variable values, creating simple files

```bash
# Basic echo
echo "Hello World"

# Display variable
echo $HOME
echo "Current user: $USER"

# Echo without newline
echo -n "Enter your name: "


# Redirect echo to file
echo "This is content" > file.txt
echo "Append this" >> file.txt

```

### `sed` - Stream Editor
-  Stream Editor
-  Text processing and editing in streams/files
-  Find and replace, text transformation, inline editing

```bash
# Basic find and replace
sed 's/old/new/' file.txt

# Replace all occurrences (global)
sed 's/old/new/g' file.txt

# Edit file in place
sed -i 's/old/new/g' file.txt

# Delete lines containing pattern
sed '/pattern/d' file.txt

```

## File Editors

### vim - Vi Improved
-  Vi Improved
-  Advanced modal text editor
-  Efficient text editing, programming, system administration

```bash
# Open file in vim
vim filename.txt

# Vim modes and basic commands:
# Normal mode (default):
#   i - Insert mode before cursor
#   a - Insert mode after cursor
#   o - Insert new line below and enter insert mode
#   x - Delete character
#   dd - Delete line
#   yy - Copy line
#   p - Paste
#   u - Undo
#   Ctrl+r - Redo
#   /pattern - Search forward
#   ?pattern - Search backward
#   :w - Save file
#   :q - Quit
#   :wq - Save and quit
#   :q! - Quit without saving

# Visual mode:
#   v - Character visual mode
#   V - Line visual mode
#   Ctrl+v - Block visual mode

# Command mode examples:
#   :set number - Show line numbers
#   :syntax on - Enable syntax highlighting
#   :%s/old/new/g - Find and replace globally
#   :1,10s/old/new/g - Replace in lines 1-10
```

### nano - Nano's Another editor
-  Nano's Another editor
-  Simple, user-friendly command-line text editor
-  Quick file editing, beginner-friendly editing

```bash
# Open file in nano
nano filename.txt

# Basic nano shortcuts (shown at bottom of editor):
#   Ctrl+O - Save file (WriteOut)
#   Ctrl+X - Exit
#   Ctrl+G - Help
#   Ctrl+K - Cut line
#   Ctrl+U - Paste (Uncut)
#   Ctrl+W - Search (Where is)
#   Ctrl+\ - Replace
#   Alt+G - Go to line number
#   Ctrl+Y - Previous page
#   Ctrl+V - Next page

# Open with line numbers
nano -l filename.txt

# Open at specific line
nano +25 filename.txt

# Create backup when saving
nano -B filename.txt
```

## Disk and Partition Management Commands - Optional

### `df` - Disk Free
-  Disk Free
-  Display filesystem disk space usage
-  Monitoring disk space, system maintenance, capacity planning

```bash
# Basic disk usage
df

# Human-readable format
df -h

# Show all filesystems including dummy ones
df -a

# Show filesystem type
df -T

# Display specific filesystem
df -h /home

# Display in 1K blocks
df -k

# Display in MB
df -m

```

### `lsblk` - List Block devices
-   List Block devices
-  Display block devices in tree format
-   Understanding storage device hierarchy and mount points

```bash
# Basic block device listing
lsblk

# Show filesystem information
lsblk -f

# Show all devices including empty ones
lsblk -a

# Output in list format instead of tree
lsblk -l

# Show device permissions and ownership
lsblk -m

# Show specific columns
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT

# Show devices in JSON format
lsblk -J

# Show only specific device
lsblk /dev/xvdf
```

### `blkid` - Block ID
-  Block device ID
-  Display block device attributes
-  Finding UUIDs, filesystem types, labels

```bash
# Show all block devices with UUIDs
blkid

# Show specific device
blkid /dev/xvdf1
```


### `fdisk` - Format Disk

-  Manipulate disk partition tables
-  reating, deleting, modifying disk partitions

```bash
# List all partitions
fdisk -l

# List partitions for specific disk
fdisk -l /dev/xvdf

# Interactive partition management
sudo fdisk /dev/xvdf
# Interactive commands:
#   p - Print partition table
#   n - New partition
#   d - Delete partition
#   t - Change partition type
#   w - Write changes and exit
#   q - Quit without saving

# List partition types
fdisk -T
```

### `sfdisk` - Scriptable FDISK
-  Scriptable Fixed Disk
-  Scriptable version of fdisk for batch operations
-  Automated partitioning, backup/restore partition tables

```bash
# Backup partition table
sfdisk -d /dev/xvdf > xvdf_partition_backup.txt

# Restore partition table
sfdisk /dev/xvdf < xvdf_partition_backup.txt

# Display partition information
sfdisk -l /dev/xvdf

# Show partition sizes
sfdisk -s

# Verify partition table
sfdisk -V /dev/xvdf

```

### `cfdisk` - Curses-based FDISK
-   Curses-based Fixed Disk
-  Text-based graphical partition manager
-   User-friendly partition management with menu interface

```bash
# Open cfdisk for disk
sudo cfdisk /dev/xvdf

# Navigation in cfdisk:
#   Up/Down arrows - Select partitions
#   Left/Right arrows - Select options
#   Enter - Execute selected option
#   Options: New, Delete, Resize, Type, Write, Quit
```

### `mdadm` - Multiple Device Administrator
-  Multiple Device Administrator
-  Manage software RAID arrays
-  Creating and managing RAID configurations for redundancy/performance

```bash
sudo mdadm --detail --scan   # View RAID arrays (if any)

```

## Process Management Commands

### `history` - History
-   Command History
-  Display command history
-   Reviewing previous commands, repeating operations

```bash
# Show command history
history

# Show last 10 commands
history 10

# Search history
history | grep "ssh"

# Execute command by number
!123

# Execute last command
!!

# Execute last command starting with specific text
!ssh

# Clear history
history -c

# Delete specific history entry
history -d 123

# Write current session history to file
history -w

# Reload history from file
history -r

# Show history with timestamps (if HISTTIMEFORMAT is set)
export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "
history
```

### `ps` - Process Status
-  Process Status
-  Display running processes
-  System monitoring, troubleshooting, process management

```bash
# Show processes for current user
ps

# Show all processes (BSD style)
ps aux

# a: Show processes for all users
# u: Show the user/owner of the process
# x: Include processes not attached to a terminal


# Show process tree
ps axjf
pstree

# Show processes for specific user
ps -u username

# Show processes by PID
ps -p 1234,5678

# Show processes with specific command
ps -C firefox

```

### `kill` - Kill
-  Terminate process
-  Send signals to processes
-  Stopping unresponsive programs, process management

```bash
# Kill process by PID (TERM signal)
kill 1234

# Force kill process (KILL signal)
kill -9 1234
kill -KILL 1234

# Kill process by name
killall firefox
pkill firefox

# List available signals
kill -l

# Send specific signal
kill -HUP 1234   # Hangup
kill -USR1 1234  # User signal 1
kill -STOP 1234  # Stop process
kill -CONT 1234  # Continue process

# Kill all processes matching pattern
pkill -f "python script.py"

# Kill processes by user
pkill -u username

# Kill process group
kill -TERM -1234  # negative PID kills process group

# Interactive process killer
top  # then press 'k' and enter PID
```

### `nohup` - No Hangup
-  No Hangup
-  Run commands immune to hangup signals
-  Running long processes that continue after logout

```bash
# Run command with nohup
nohup command &

# Run script in background
nohup ./long_script.sh &

# Redirect output to specific file
nohup command > output.log 2>&1 &

# Run with custom output file
nohup command > /dev/null 2>&1 &

# Check nohup jobs
jobs
ps aux | grep command

# Multiple commands with nohup
nohup bash -c 'command1 && command2' &

# Combination with screen/tmux (alternative approaches)
screen -S session_name
tmux new-session -d -s session_name

# Example: Long-running data processing
nohup python data_processing.py > processing.log 2>&1 &

# Monitor the background job
tail -f nohup.out  # default output file
```