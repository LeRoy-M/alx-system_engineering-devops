# Manifest that changes the OS configuration to make it possible to login with `holberton` user and open a file
exec { 'userlimitsoft':
  command => 'sudo sed -i "/holberton soft/s/4/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'userlimithard':
  command => 'sudo sed -i "/holberton hard/s/5/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
