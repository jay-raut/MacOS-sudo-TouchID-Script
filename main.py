#!/usr/bin/env python3
#script must run as sudo
import filecmp
import shutil
sudo_file_location = "/etc/pam.d/sudo"
replacement_sudo = "replacement_sudo_file"


def check_tid(): #check if sudo file has sufficient auth tid.so string
    return filecmp.cmp(sudo_file_location, replacement_sudo)


def modify_sudo_file(): #modify sudo file with modified sudo file
    shutil.copyfile(replacement_sudo, sudo_file_location)

if __name__ == '__main__':
    if not check_tid():
        modify_sudo_file()
