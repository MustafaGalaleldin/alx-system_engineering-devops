# set up your client SSH configuration file so that you can connect to a server without typing a password
file { 'ssh_config':
    ensure => present
    }

file_line { 'ssh_config':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => 'PasswordAuthentication yes',
    replace => true,
    }

file_line { 'identity':
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => 'IdentityFile'
    ensure => present,
    }
