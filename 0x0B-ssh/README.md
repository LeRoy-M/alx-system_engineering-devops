0. Use a private key [0-use_a_private_key] >> Bash script that uses 'ssh' to connect to your server using the private key '~/.ssh/school' with the user 'ubuntu', only using 'ssh' single-character flags without using '-l'.
1. Create an SSH key pair [1-create_ssh_key_pair] >> Bash script that creates an RSA key pair, with the created private key being 'school', the number of bits in the createde key being 4096, and the created key being protected by the passphrase 'betty'.
2. Client configuration file [2-ssh_config] >> Configuring the SSH configuration file for the local SSH client so that one can connect to a server without typing a password, configured to use the private key '~/.ssh/school', and to refuse to authenticate using a password.
3. Let me in! >> Adding the SSH public key to the server so that others can connect using the 'ubuntu' user.
4. Client configuration file (w/ Puppet) [100-puppet_ssh_config.pp] >> Practicing using Puppet to make changes to our configuration file. Setting up the client SSH configuration file so that one can connect to a server without typing a password, configured to use the private key '~/.ssh/school', and to refuse to authenticate using a password.