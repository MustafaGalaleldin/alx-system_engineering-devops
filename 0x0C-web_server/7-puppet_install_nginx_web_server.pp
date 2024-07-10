# a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
exec { 'update':
    command => '/usr/bin/apt-get update'
}
package { 'nginx':
    ensure   => 'installed',
    require  => Exec['update'],
}
file { 'index.html':
    ensure  => 'present',
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    require => Package['nginx'],
}
exec {'redirect_me':
    command  => 'sed -i "/server_name _;/a \\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
    path     => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
    provider => 'shell',
    require  => Package['nginx'],
    notify   => Service['nginx'],
}
service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Package['nginx'],
    subscribe => Exec['redirect_me'],
}
