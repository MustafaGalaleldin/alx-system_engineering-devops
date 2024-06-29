# Execute a command
exec { 'pkill':
    command => 'pkill -15 killmenow',
    path    => '/usr/bin:/bin/',
    }
