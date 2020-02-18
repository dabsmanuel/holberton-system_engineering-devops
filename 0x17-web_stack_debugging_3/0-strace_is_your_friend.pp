#Replaces .phpp for .php in wp-settings.php file
exec { 'Replace':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php && service apache2 reload',
  provider => 'shell',
}
