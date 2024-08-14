# a puppet manifest fix the error with phpp and make it php
exec { 'fixer':
    command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
    path    => '/bin:/sbin',
}
