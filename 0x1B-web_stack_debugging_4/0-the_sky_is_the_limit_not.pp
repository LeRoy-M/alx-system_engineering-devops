# Fix failed requests issue
exec { "ulimit":
  command => "/bin/bash -c 'ulimit -n 64000'",
}
