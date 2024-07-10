# a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
exec { 'update':
    command => '/usr/bin/apt-get update'
}
package { 'nginx':
    ensure  => 'installed',
    require => Exec['update'],
}
file { '/var/www/html/index.html':
    content => 'Hello World!',
}
exec {'redirect_me':
    command  => 'sed -i "/server_name _;/a \\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
    provider => 'shell',
}
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
