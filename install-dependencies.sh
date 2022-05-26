#!/usr/bin/env sh

req_sum=$(md5sum /tmp/requirements.txt | awk '{print $1}')
req_version_file="/tmp/${req_sum}"

test -f "$req_version_file" || { # run ideally only once
    # upgrade pip and install dependencies
    python3 -m pip install --upgrade pip
    python3 -m pip install -r /tmp/requirements.txt

    # don't re-install unless changes made
    # you may use a volume to persist /tmp dir to a local one
    touch "$req_version_file"
}
