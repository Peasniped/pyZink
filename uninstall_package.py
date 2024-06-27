import os
import subprocess

PACKAGE_NAME = "pyZink"

try:
    print(f"Executing as subprocess: 'python -m pip uninstall {PACKAGE_NAME} -y'")
    result = subprocess.run(["python", "-m", "pip", "uninstall", PACKAGE_NAME, "-y"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if len(result.stderr) != 0:
        raise Exception(result.stderr)
except Exception as e:
    print(f"Something went wrong while uninstalling the package: {e}")

try:
    result = subprocess.run(["python", "-m", "site", "--user-site"], stdout=subprocess.PIPE, text=True)
    user_site_dir = result.stdout.strip()
    pth_file_path = os.path.join(user_site_dir, f"{PACKAGE_NAME}.pth")
    
    if os.path.exists(pth_file_path):
        os.remove(pth_file_path)
        print(f"Successfully removed .pth-file at: '{pth_file_path}'")
    else:
        raise FileNotFoundError(f"The file '{pth_file_path}' does not exist")
except Exception as e:
    print(f"Something went wrong while removing the .pth file: {e}")