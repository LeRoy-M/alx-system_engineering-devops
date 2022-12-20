# Configures the SSH client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  line    => '	PasswordAuthentication no',
  replace => true,
}

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}
