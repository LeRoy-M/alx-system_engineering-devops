# Manifest that automates server 500 error fix
server 'fix-500_server_error' {
  command => 'sed -i \'s/.phpp/.php\' /var/www/hmtl/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
