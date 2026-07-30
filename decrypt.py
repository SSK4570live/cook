import os
import subprocess
import sys
import pyzipper


def unzip_password_protected_zip(zip_file_path, output_path, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as z:
            z.extractall(output_path, pwd=password.encode("utf-8"))
        print("Extraction successful.")
        return True
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return False


def run_and_cleanup_script(script_name):
    """Runs a python script and ensures it gets deleted afterward."""
    if not os.path.exists(script_name):
        print(f"File not found: {script_name}")
        return

    try:
        print(f"Running {script_name}...")
        # sys.executable ensures we use the exact same Python interpreter running this script
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}: {e}")
    finally:
        # The finally block guarantees the file is deleted even if the script crashes
        if os.path.exists(script_name):
            os.remove(script_name)
            print(f"Cleaned up {script_name}.")


# Configuration
zip_file_path = "cook.zip"
output_path = "."
password = os.environ.get("password", "")

# Run workflow
if unzip_password_protected_zip(zip_file_path, output_path, password):
    run_and_cleanup_script("cookjtv.py")
    run_and_cleanup_script("cookson.py")