# Manifest that tests how well the web server setup works
exec { 'skynotlimit':
  command     => 'curl -X POST -H "Content-Type: application/json" -d @/path/to/body.json http://localhost',
  path        => ['/usr/bin/', '/bin'],
  onlyif      => 'test -f /path/body.json',
  refreshonly => true,
}
