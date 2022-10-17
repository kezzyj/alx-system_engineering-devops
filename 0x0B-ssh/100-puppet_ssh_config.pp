# Create a file in /tmp

file { 'school':

  ensure  => 'present',

  PasswordAuthentication => 'no',

  private key => '~/.ssh/school',

  group   => 'www-data',

  mode    => '0744',

  owner   => 'www-data',

  path    => '/tmp/holberton',

}

