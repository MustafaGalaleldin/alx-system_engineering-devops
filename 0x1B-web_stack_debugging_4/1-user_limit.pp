# configure OS to increase the limit of files to prevent Too many open files error
exec { 'Hard limit fixer':
        command => "sudo sed -i 's/holberton hard nofile.*/holberton hard nofile 10000/' /etc/security/limits.conf",
        path    => '/bin:/sbin:/usr/bin:/usr/sbin',
}
exec { 'Soft limit fixer':
        command => "sudo sed -i 's/holberton soft nofile.*/holberton soft nofile 9000/' /etc/security/limits.conf",
        path    => '/bin:/sbin:/usr/bin:/usr/sbin',
}
