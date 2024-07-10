include stdlib

package { 'nginx':
    ensure   => installed
    provider => apt
}
file { 'index.html':
    path    => '/var/www/html/index.html',
    ensure  => 'present',
    content => 'Hello World!'
}
