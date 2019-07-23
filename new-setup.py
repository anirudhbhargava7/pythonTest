# new_setup.py for linux mint systems
import os


#install aptitude
install_aptitude = "sudo apt-get install aptitude"
os.system(install_aptitude)
#install ssh utility
ssh_install_cmd = "sudo apt-get install ssh"
os.system(ssh_install_cmd);

#install git 
git_install_cmd = "sudo apt-get install git"
os.system(git_install_cmd)

#install java 1.8
add_openjdk_apt_repo = "sudo add-apt-repository ppa:openjdk-r/ppa";
os.system(add_openjdk_apt_repo)

update_apt_get = "sudo apt-get update"
os.system(update_apt_get)

install_openjdk8 = "sudo apt-get install openjdk-8-jdk"
os.system(install_openjdk8)

check_java_version = "java -version"
os.system(check_java_version)

bash_rc_file = "/etc/bash.bashrc"
#list of env variables
java_home = "export JAVA_HOME=\"/usr/lib/jvm/java-1.8.0-openjdk-amd64\""
java_path = "export PATH=$JAVA_HOME/bin:$PATH"
f = open(bash_rc_file, "a+")
f.write(java_home)
f.write(java_path)
f.close() 

#Download and Install Docker
#Docker for Tessa 19.1 == Bionic for Ubuntu 18.04
download_docker = "wget -O docker.deb https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/docker-ce_18.09.6~3-0~ubuntu-bionic_amd64.deb"
os.system(download_docker)
install_docker = "sudo dpkg -i docker.deb"
os.system(install_docker)
download_docker_cli = "wget -O docker-cli.deb https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/docker-ce-cli_18.09.6~3-0~ubuntu-bionic_amd64.deb"
os.system(download_docker_cli)
install_docker_cli = "sudo dpkg -i docker-cli.deb"
download_containerdio = "wget -O containerd-io.deb https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/containerd.io_1.2.5-1_amd64.deb"
install_containerdio = "sudo dpkg -i containerd-io.deb"
install_docker_compose = "sudo apt-get install docker-compose"
os.system(install_docker_compose)
os.system("sudo docker-compose version")
print("Adding the $USER to docker group")
os.system("sudo usermod -aG docker $USER")
#Notes after Installation
print("run \"sudo vim /etc/docker/daemon.json\"")
print("add lines [\"rdocker:6000\",\"nexus.eng.hitachivantara.com:6000\",\"10.76.48.134:6000\"], \"bip\":\"192.168.1.5/24\"}")


#setting ip addresses to access local resources in host file




