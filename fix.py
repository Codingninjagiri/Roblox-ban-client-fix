import os
import shutil
import requests
import subprocess

# Step 1: Define the Roblox Local directory path
roblox_local_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Roblox')

def delete_roblox_cache(path):
    """Deletes everything in the specified Roblox directory."""
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print("Roblox spoofed")
        except Exception as e:
            print(f"An error occurred while deleting the Roblox cache: {e}")
    else:
        print("Roblox cache directory does not exist. Skipping deletion.")

def download_and_run_installer(url, download_path):
    """Downloads the installer and runs it."""
    try:
        # Step 2: Download the installer
        response = requests.get(url, stream=True)
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Installer downloaded successfully.")

        # Step 3: Run the installer
        subprocess.run(download_path, shell=True)
        print("Installer launched successfully.")
    except Exception as e:
        print(f"An error occurred during download or installation: {e}")

# Define the URL for the Roblox installer and the download path
installer_url = "https://setup.rbxcdn.com/version-b7eebc919e96477a-RobloxPlayerInstaller.exe"
download_path = os.path.join(os.getenv('LOCALAPPDATA'), 'RobloxPlayerInstaller.exe')

# Run the functions
delete_roblox_cache(roblox_local_path)
download_and_run_installer(installer_url, download_path)
