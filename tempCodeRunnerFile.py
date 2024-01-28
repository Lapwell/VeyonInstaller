 # except:
    #     print("Veyon Install Failed...")
    # else:
    #     print("Veyon Install Finished...")

    # # if not os.path.exists("C:/ProgramData/Veyon/keys/private"):
    # #     print("Making Private Key Folder...\n")
    # #     os.makedirs("C:/ProgramData/Veyon/keys/private")
    # # else:
    # #     print("Private Key Folder Exists...\n")

    # # if not os.path.exists("C:/ProgramData/Veyon/keys/public"):
    # #     print("Making Public Key Folder...\n")
    # #     os.makedirs("C:/ProgramData/Veyon/keys/public")
    # # else:
    # #     print("Public Key Folder Exists...\n")

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