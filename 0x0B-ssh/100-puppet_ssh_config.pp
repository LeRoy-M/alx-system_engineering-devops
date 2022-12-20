# Configures the SSH client configuration file
file { 'PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}

file { 'IdentityFile':
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}
