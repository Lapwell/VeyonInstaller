import subprocess
import shutil

if __name__ == "__main__":
    FNULL = open(os.devnull, 'w')
    args = "veyon-4.8.2.0-win64-setup.exe", "/S /NoMaster /NoStartMenuFolder /ApplyConfig=%cd%\ClientConfig.json"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=false)
    mkdir("C:\ProgramData\Veyon\keys\private")
    mkdir("C:\ProgramData\Veyon\keys\public")
    shutil.copyfile("%cd%\DojoLaptops_public_key.pem", "C:\ProgramData\Veyon\keys\public")
