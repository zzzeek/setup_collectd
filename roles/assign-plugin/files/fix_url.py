#!/usr/bin/env python

import sys
import re
import shutil

file_ = sys.argv[1]
undercloud_ip = sys.argv[2]

newfile = file_ + ".tmp"
savedfile = file_ + ".saved"
with open(newfile, 'w') as newfile_handle:
    with open(file_, 'r') as file_handle:
        for line in file_handle:
            reg = re.match(r'(connection=mysql\+pymysql://[^\?]*)\??(.*)$', line.rstrip())
            if not reg:
                newfile_handle.write(line)
                continue
            line = reg.group(1)
            tokens = [t for t in reg.group(2).split('&') if 'collectd' not in t]
            tokens += ["plugin=collectd", "collectd_host=%s" % undercloud_ip]
            line += '?' + '&'.join(tokens) + "\n"
            newfile_handle.write(line)
            print(line)
shutil.move(file_, savedfile)
shutil.move(newfile, file_)

