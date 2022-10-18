
#!/usr/bin/env python3

# Fabfile defining functions to pack, deploy, and clean the

# current directory to a remote server.

from fabric import task





@task

def pack(c):

    """Create a tar gzipped archive of the current directory."""

    c.run("touch schoolwebapp.tar.gz")

    c.run("tar --exclude='*.tar.gz' -cvzf schoolwebapp.tar.gz .")





@task

def deploy(c):

    """Upload the archive to the remote server in the /tmp/ directory."""

    c.user = "ubuntu"

    c.put("schoolwebapp.tar.gz", "/tmp")

    c.run("mkdir /tmp/schoolwebapp")

    c.run("tar -C /tmp/schoolwebapp -xzvf /tmp/schoolwebapp.tar.gz")





@task

def clean(c):

    """Deletes holbertonwebapp.tar.gz on the local machine."""

    c.run("rm schoolwebapp.tar.gz")
