# Manifest that tests how well the web server setup works
exec { 'skynotlimit':
  command => 'sudo sed -i "s/15/10000" /etc/default/nginx && sudo service nginx restart',
  path    => ['/usr/local/bin/', '/usr/local/sbin/', '/usr/bin/', '/usr/sbin/', '/bin/'],
}
