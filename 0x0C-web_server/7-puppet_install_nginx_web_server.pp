# a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
include stdlib

package { 'nginx':
    ensure   => installed
    provider => apt
}
file { 'index.html':
    ensure  => 'present',
    path    => '/var/www/html/index.html',
    content => 'Hello World!'
}
