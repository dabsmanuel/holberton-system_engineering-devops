#Installs nginx package, writes contenct on index.html, writes redirection url on default and starts server
package { 'nginx':
  ensure  => installed,
}
file { 'index.nginx-debian.html':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Holberton School',
}
file_line { 'writes redirection site':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://findtheinvisiblecow.com permanent;',
}
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
