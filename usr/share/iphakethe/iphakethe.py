#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import configparser
import sys
sys.path.insert(0, '/usr/lib/iphakethe')
from Config import Config
from Check import Check
from Git import Git
from Debug import Debug
import functions

def main():
    config = Config()
    check = Check()
    debug = Debug()
    
    config.set_sections()
    sections = config.get_sections()

    for section in sections:
        config.set_temp_dir("/tmp/build")
        config.set_git_addr(section, 'git_addr')
        config.set_git_port(section, 'git_port')
        config.set_user_git(section, 'user_git')
        config.set_repo(section, 'repo')
        config.set_folder_package_linux_repo(section, 'folder_package_linux_repo')
        config.set_testing(section , 'testing')
        config.set_branch_dev_testing(section, 'branch_dev_testing')
        config.set_distro_repo(section, 'distro_repo')
        config.set_codename_repo(section, 'codename_repo')
        config.set_keep_old_packages(section, 'keep_old_packages')

        temp_dir = config.get_temp_dir()
        debug.debug(temp_dir)


        git_addr = config.get_git_addr()
        user_git = config.get_user_git()
        git_port = config.get_git_port()
        repo = config.get_repo()
        folder_package_linux_repo = config.get_folder_package_linux_repo()
        testing = config.get_testing()
        branch_dev_testing = config.get_branch_dev_testing()
        distro_repo = config.get_distro_repo()
        codename_repo = config.get_codename_repo()
        keep_old_packages = config.get_keep_old_packages()

        check.check_dir_and_create_and_go_to(temp_dir)
        git = Git(git_addr, git_port, user_git, repo)
        git.clone()

        if testing == "yes":
            os.chdir("{0}/{1}".format(temp_dir, repo))
            git.checkout(branch_dev_testing)

        folder = "{0}/{1}".format(temp_dir, repo)

        check.set_permission('0755', folder)

        package_file_control = open("{0}/{1}/DEBIAN/control".format(temp_dir, repo))
        temp_file_package_control = open("{0}/FILE_TEMP_PACKAGE".format(temp_dir), "w+")

        temp_file_package_control.write("[PACKAGE]\n")
        for line in package_file_control:
            temp_file_package_control.write(line)

        temp_file_package_control.close()
        package_file_control.close()

        files_to_delete_package_deb = [".git", "readme.md", "README.md",
                                       "Jenkinsfile", ".gitignore"]
        for file in files_to_delete_package_deb:
            os.system("rm -rf /tmp/build/{0}/{1}".format(repo, file))

        os.system("dpkg -b {0}/{1} {0}".format(temp_dir, repo))

        package = configparser.ConfigParser()
        package.read("{0}/FILE_TEMP_PACKAGE".format(temp_dir))

        version = package.get('PACKAGE', 'Version')
        architecture = package.get('PACKAGE', 'Architecture')

        if keep_old_packages == "yes":
            os.system("reprepro --keepunreferencedfiles -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb 2> /dev/null"
                      .format(folder_package_linux_repo, distro_repo, codename_repo, temp_dir,
                              repo, version, architecture))
        else:
            os.system("reprepro -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb 2> /dev/null"
                      .format(folder_package_linux_repo, distro_repo, codename_repo, temp_dir,
                              repo, version, architecture))

        os.system('rm -rf /tmp/build')


if __name__ == '__main__':
    main()
