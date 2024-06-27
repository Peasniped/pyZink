import os
import subprocess

try:
    print("Executing as subprocess: 'python -m pip install -e .'")
    result = subprocess.run(["python", "-m", "pip", "install", "-e", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if len(result.stderr) != 0:
        raise Exception(result.stderr)
except Exception as e:
    print(f"Something went wrong while installing the package: {e}")  

# make .pth-file in user_site directory, so the package is found by python
try:
    cwd = os.getcwd()
    result = subprocess.run(["python", "-m", "site", "--user-site"], stdout=subprocess.PIPE, text=True)
    user_site_dir = result.stdout.strip()
    pth_file_path = os.path.join(user_site_dir, "pyZink.pth")

    with open(pth_file_path, "w") as pth_file:
        pth_file.write(cwd + "\n")
except Exception as e:
    print("\nsomething went wrong while making the .pth file:", e, end="\n\n")