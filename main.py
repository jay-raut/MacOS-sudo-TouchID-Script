#!/usr/bin/env python3
#script must run as sudo
import filecmp
import shutil
import subprocess

sudo_file_location = "/etc/pam.d/sudo"
sudo_backup_location = "/etc/pam.d/sudo-backup"
replacement_sudo = "replacement_sudo_file"


def check_tid(): #check if sudo file has sufficient auth tid.so string
    return filecmp.cmp(sudo_file_location, replacement_sudo)


def modify_sudo_file(): #modify sudo file with modified sudo file
    create_sudo_backup()
    shutil.copyfile(replacement_sudo, sudo_file_location)

def create_sudo_backup(): #makes a backup copy for sudo file
    open(sudo_backup_location, 'a').close()
    shutil.copyfile(sudo_file_location, sudo_backup_location)


if __name__ == '__main__':
    if not check_tid():
        modify_sudo_file()
