# Manifest that creates a file
file { 'school':
  path    => '/tmp/'
  content => 'I love Puppet'
  mode    => '0744'
  owner   => www-data
  group   => www-data
}
