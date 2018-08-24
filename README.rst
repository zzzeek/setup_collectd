To run:

/path/to/ansible-playbook -i stack1_hosts  playbooks/deploy-collectd.yml


# the undercloud_ip is currently fetched as the default route, which
# might not be the case.
# previously we hardcoded here like this:
#/path/to/ansible-playbook -i stack1_hosts -e undercloud_ip=10.0.0.1

