# Manifest that automates server 500 error fix
server 'fix-500_server_error' {
  command => 'sudo apachectl fullstatus;sudo strace -p [PID] -f -o output.txt',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
