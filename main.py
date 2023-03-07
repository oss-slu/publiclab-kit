import subprocess
import git 
import time
repoPath = "../FIRE/AutoBuilder"
#publicLab = "https://gitlab.com/publiclab/pi-builder/-/jobs/121890022/artifacts/download"
drive = "test"
iso = "test"

#load up a new directory for building git repo if needed in future
print(subprocess.run(["mkdir", "AutoBuilder"]))
print(subprocess.run(["cd", "AutoBuilder"]))
print(subprocess.run(["lsblk"]))


#ask for drive path and iso path, wait in betweeen
drive = input("Enter name of drive, and its path ")
print("Drive selected is: " + drive)
time.sleep(2)
iso = input("Enter name path of iso ")
print("Iso selected is: " + iso)
time.sleep(2)

#unmount and format disk to FAT32
print(subprocess.run(["umount", drive]))
print("formatting disk...")
print(subprocess.run(["sudo","mkfs","-t","vfat",drive]))

#load the given iso onto the given disk
print("loading Iso onto disk... This may take some time")
print(subprocess.run(["sudo","dd","bs=4M","if=" + iso,"of=" + drive, "conv=fdatasync", "status=progress"], capture_output=True))
#git.Git(repoPath).clone(publicLab)




