# Create a file in /tmp

file { 'school':

  ensure  => 'present',

  PasswordAuthentication => 'no',

  private key => '~/.ssh/school',

  path    => '/etc/ssh/ssh_config',

}
