import subprocess
import socket
import os

if __name__ == "__main__":
    FNULL = open(os.devnull, 'w')
    defaultDir = os.getcwd()
    print(defaultDir)
    localIP = socket.gethostbyname(socket.gethostname())
    deviceNumber = input("Device Number?")
    print(f"\n", "Updating IP list: ", localIP)
    DeviceList = open("Device List.txt", "w")
    DeviceList.writelines((deviceNumber, "||", localIP))
    DeviceList.close()
    # try:
    #     print("Installing Veyon...")
    #     configPath = os.path.abspath("ClientConfig.json")
    #     veyonSetup = "veyon-4.8.2.0-win64-setup.exe"
    #     args = "/S /NoMaster /ApplyConfig=%cd%\ClientConfig.json"
    #     subprocess.run([veyonSetup, args], shell=True)
    # except:
    #     print("Veyon Install Failed...")
    # else:
    #     print("Veyon Install Finished...")

    # try:
    #     print("Imporing Auth Keys")
    #     os.chdir("C:/Program Files/Veyon")
    #     subprocess.run(["./veyon-wcli", f'authkeys import Dojo/public "{defaultDir}\DojoLaptops_public_key.pem"'])
    # except:
    #     print("Auth Key Import Failed...\n")
    # else:
    #     print("Auth Key Import Success...\n")

    # try:
    #     print("Setting Auth Key Group")
    #     subprocess.run(["./veyon-wcli", "authkeys setaccessgroup Dojo/public Users"])
    # except:
    #     print("Setting Key Group Failed...")
    # else:
    #     print("Setting Auth Key Group Success...")

    # input("\nPress Key to Finish...\n")
