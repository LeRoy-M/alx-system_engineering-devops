# Manifest that creates a file
file { 'school':
  path    => /tmp/
  content => 'I love Puppet'
  owner   => www-data
  group   => www-data

}
