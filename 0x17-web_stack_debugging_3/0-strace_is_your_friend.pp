# Manifest that automates server 500 error fix
server 'fix-500_server_error' {
  command => 'sudo pgrep apache2 | sudo strace -p -f -o strace.log',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
