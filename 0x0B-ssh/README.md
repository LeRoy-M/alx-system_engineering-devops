## 0x0B. SSH

**0. Use a private key** `[0-use_a_private_key]` >> Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`, using only `ssh` single-character flags.

**1. Create an SSH key pair** `[1-create_ssh_key_pair]` >> Bash script that creates an RSA key pair, with a private key named `school`, with `4096` being the number of bits in the created key, and the created key is also protected by the passphrase `betty`.

**2. Client configuration file** `[2-ssh_config]` >> Configuring SSH configuration file for the local SSH client so that one can connect to a server without typing a password. Configured to use the private key `~/.ssh/school`, and to refuse to authenticate using a password.

**3. Let me in!** >> Adding the provided SSH pubic key to the server so that others can connect using the `ubuntu` user.


**4. Client configuration file (w/ Puppet)** `[100-puppet_ssh_config.pp]` >> Using Puppet to make changes to the configuration file in task #2.
