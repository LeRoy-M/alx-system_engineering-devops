# Manifest that kills the process 'killmenow'
exec { 'killmenow':
  command => 'pkill',
  path    => '/usr/bin',
}
