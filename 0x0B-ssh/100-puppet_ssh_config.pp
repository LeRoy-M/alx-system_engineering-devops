# Manifest that makes changes to a configuration file
file { 'PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

file { 'IdentityFile':
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
