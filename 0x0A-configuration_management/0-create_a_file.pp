# Manifest that creates a file
file { 'school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
}
