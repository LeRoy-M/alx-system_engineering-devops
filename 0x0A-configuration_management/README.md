## 0x0A. Configuration management

**0. Create a file** `[0-create_a_file.pp]` >> Puppet manifest that creates a file in `/tmp`. The file's path is `/tmp/school`, with permissions `0744`, owner is `www-data`, group is `www-data`, and the file contains `I love Puppet`.

**1. Install a package** `[1-install_a_package.pp]` >> Puppet manifest that installs `flask` version `2.1.0` from `pip3`.

**2. Execute a command** `[2-execute_a_command.pp]` >> Puppet manifest that kills a process named `killmenow` using the `exec` Puppet resource and `pkill`.
