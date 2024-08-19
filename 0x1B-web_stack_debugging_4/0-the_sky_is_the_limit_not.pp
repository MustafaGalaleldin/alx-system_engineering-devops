# a puppet manifest fixes the server error related to open files limit
exec { 'fixer':
        command => "sudo sed -i 's/ULIMIT=.*/ULIMIT=-n 4096/' /etc/default/nginx",
        path    => '/bin:/sbin:/usr/bin:/usr/sbin',
}
exec { 'restart nginx':
        command => 'sudo service nginx restart',
        path    => '/bin:/sbin:/usr/bin:/usr/sbin',
}
