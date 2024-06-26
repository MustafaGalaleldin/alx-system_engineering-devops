# set up your client SSH configuration file so that you can connect to a server without typing a password
include stdlib

file_line { 'ssh_config':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^PasswordAuthentication',
    }

file_line { 'identity':
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile'
    }
