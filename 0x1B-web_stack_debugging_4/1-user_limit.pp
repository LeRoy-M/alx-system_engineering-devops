# Manifest that changes the OS configuration to make it possible to login with `holberton` user and open a file
exec { 'userlimit':
  command => 'sudo sed -i "/holberton/s/5/50000" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/usr/local/sbin/', '/usr/bin/', '/usr/sbin/', '/bin/', '/sbin/'],
}
