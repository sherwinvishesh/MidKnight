import os
import time
import subprocess
import shutil
import json
from pathlib import Path

# --- Configuration Management ---
# Use the home directory to store configuration, making it persistent
CONFIG_DIR = Path.home() / '.midknight'
CONFIG_FILE = CONFIG_DIR / 'config.json'

def load_config():
    """Loads user configuration from the config file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return None

def save_config(config_data):
    """Saves user configuration to the config file."""
    CONFIG_DIR.mkdir(exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f, indent=4)

def first_time_setup():
    """Guides the user through the initial setup process."""
    clear_screen()
    display_welcome()
    print("\nWelcome to MidKnight! Let's get you set up.")
    name = input("\nWhat should I call you? ").strip()
    api_key = input("Please enter your Gemini API Key: ").strip()

    config = {
        "name": name,
        "gemini_api_key": api_key
    }
    save_config(config)
    print("\nSetup complete! Configuration saved.")
    time.sleep(2)
    return config

def log_out():
    """Logs the user out by deleting the configuration file."""
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        print("\nYou have been logged out. MidKnight will run the setup on the next start.")
    else:
        print("\nNo active session found.")
    time.sleep(2)


# --- UI and Display Functions ---
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Displays the MidKnight welcome screen with ASCII art."""

    # ANSI escape code for a cool blue color
    blue_color = "\033[94m"
    # ANSI escape code to reset color
    reset_color = "\033[0m"

    logo = r"""
███╗   ███╗ ██╗ ██████╗  ██╗  ██╗ ███╗   ██╗ ██╗  ██████╗  ██╗  ██╗ ████████╗
████╗ ████║ ██║ ██╔══██╗ ██║ ██╔╝ ████╗  ██║ ██║ ██╔════╝  ██║  ██║ ╚══██╔══╝
██╔████╔██║ ██║ ██║  ██║ █████╔╝  ██╔██╗ ██║ ██║ ██║  ███╗ ███████║    ██║
██║╚██╔╝██║ ██║ ██║  ██║ ██╔═██╗  ██║╚██╗██║ ██║ ██║   ██║ ██╔══██║    ██║
██║ ╚═╝ ██║ ██║ ██████╔╝ ██║ ╚██╗ ██║ ╚████║ ██║ ╚██████╔╝ ██║  ██║    ██║
╚═╝     ╚═╝ ╚═╝ ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═════╝  ╚═╝  ╚═╝    ╚═╝
"""
    clear_screen()
    print(blue_color + logo + reset_color)


def display_intro_message(name):
    """Displays a personalized introductory text."""
    description = f"""
Hi {name}, I'm MidKnight, an AI assistant for the Midnight developer ecosystem.

I'm here to help you build secure, private, and robust applications on the
Midnight blockchain.
"""
    # Print description with a slight delay for effect
    for char in description:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print("\n")


def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*40)
    print(" " * 14 + "MAIN MENU")
    print("="*40)
    print("  1. Midnight Starter Kit")
    print("  2. Code Analyser")
    print("\n  s. Settings")
    print("  q. Quit")
    print("="*40)

# --- Feature Functions ---
def download_starter_kit():
    """Clones the Midnight Starter Kit from GitHub into a user-specified directory."""
    clear_screen()
    display_welcome()

    starter_kit_url = "https://github.com/luislucena16/midnight-quick-starter"

    project_name = input("\nEnter a name for your new project: ").strip()

    if not project_name:
        print("\n[ERROR] Project name cannot be empty.")
        input("\nPress Enter to return to the main menu...")
        return

    # Sanitize the name for use as a directory (e.g., replace spaces with hyphens)
    project_name = project_name.replace(" ", "-")

    print(f"\n[INFO] Preparing to download the Midnight Starter Kit into './{project_name}'")

    # 1. Check if git is installed
    if shutil.which("git") is None:
        print("\n[ERROR] Git is not installed or not found in your system's PATH.")
        print("Please install Git to download the starter kit automatically.")
        print("You can find it here: https://git-scm.com/downloads")
        input("\nPress Enter to return to the main menu...")
        return

    print("[INFO] Git is installed. Proceeding with download...")
    time.sleep(1)

    # 2. Check if the directory already exists
    if os.path.exists(project_name):
        print(f"\n[WARNING] A directory named '{project_name}' already exists in this location.")
        overwrite = input("Do you want to remove it and re-download? (y/n): ").lower().strip()
        if overwrite == 'y':
            try:
                shutil.rmtree(project_name)
                print(f"[INFO] Existing directory '{project_name}' removed.")
            except OSError as e:
                print(f"\n[ERROR] Failed to remove existing directory: {e}")
                input("\nPress Enter to return to the main menu...")
                return
        else:
            print("\n[INFO] Download cancelled.")
            input("\nPress Enter to return to the main menu...")
            return

    # 3. Clone the repository
    print(f"\n[INFO] Cloning repository into './{project_name}'...")
    try:
        # Using subprocess to run the git clone command
        subprocess.run(
            ['git', 'clone', starter_kit_url, project_name],
            check=True,
            capture_output=True, # Hides git's output unless there's an error
            text=True
        )
        print("\n" + "="*40)
        print("[SUCCESS] Starter Kit downloaded successfully!")
        print(f"You can find it in the '{project_name}' directory.")
        print("="*40)
    except subprocess.CalledProcessError as e:
        print("\n[ERROR] Failed to clone the repository.")
        print(f"Details:\n{e.stderr}")

    input("\nPress Enter to return to the main menu...")


def analyze_code():
    """Integrates with external Midnight AI analyser (Node wrapper + Python backend)."""
    clear_screen()
    display_welcome()
    print("\n[INFO] Code Analyser")
    print("[INFO] This will call the external analyser. Make sure you've set it up per its README.")

    target = input("\nPath to file or directory to review (default: .): ").strip() or "."

    # Load API key from our MidKnight config and pass it through to the analyser
    cfg = load_config() or {}
    env = os.environ.copy()
    if cfg.get("gemini_api_key"):
        env["GEMINI_API_KEY"] = cfg["gemini_api_key"]

    # Prefer globally installed CLI "midnight-ai"
    analyser_cmd = None
    if shutil.which("midnight-ai"):
        analyser_cmd = ["midnight-ai", "review", target]
    else:
        # Fallbacks: local node wrapper or python backend if present next to this script
        here = Path(__file__).resolve().parent
        index_js    = here / "index.js"
        analyser_py = here / "analyser.py"
        legacy_main = here / "main.py"  # backward-compat if the old name is present

        if index_js.exists():
            analyser_cmd = ["node", str(index_js), "review", target]
        elif analyser_py.exists():
            # Rely on system python3 if venv is not present
            py = shutil.which("python3") or "python3"
            analyser_cmd = [py, str(analyser_py), "review", target]
        elif legacy_main.exists():
            py = shutil.which("python3") or "python3"
            analyser_cmd = [py, str(legacy_main), "review", target]

    if not analyser_cmd:
        print("\n[ERROR] Could not find the analyser.")
        print("Tips:")
        print("  • If you have the Node wrapper, install it with: npm install -g .")
        print("  • Or place index.js/analyser.py (or main.py) next to this midknight.py.")
        input("\nPress Enter to return to the main menu...")
        return

    print(f"\n[INFO] Running: {' '.join(analyser_cmd)}")
    try:
        # Stream output directly so the user sees the analyser's UI/results
        result = subprocess.run(analyser_cmd, env=env)
        if result.returncode != 0:
            print(f"\n[ERROR] Analyser exited with code {result.returncode}.")
    except FileNotFoundError:
        print("\n[ERROR] Failed to start the analyser (command not found).")
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")

    input("\nPress Enter to return to the main menu...")




def settings_menu(config):
    """Displays and handles the settings menu."""
    while True:
        clear_screen()
        display_welcome()
        print("\n" + "="*40)
        print(" " * 15 + "SETTINGS")
        print("="*40)
        print(f"  Current User: {config['name']}")
        print(f"  Gemini API Key: {'*' * (len(config['gemini_api_key']) - 4) + config['gemini_api_key'][-4:]}")
        print("-" * 40)
        print("  1. Change Name")
        print("  2. Change Gemini API Key")
        print("  3. Log Out")
        print("\n  b. Back to Main Menu")
        print("="*40)
        choice = input("  Enter your choice: ").strip().lower()

        if choice == '1':
            new_name = input("\nEnter your new name: ").strip()
            if new_name:
                config['name'] = new_name
                save_config(config)
                print("\nName updated successfully!")
                time.sleep(1.5)
        elif choice == '2':
            new_key = input("\nEnter your new Gemini API Key: ").strip()
            if new_key:
                config['gemini_api_key'] = new_key
                save_config(config)
                print("\nAPI Key updated successfully!")
                time.sleep(1.5)
        elif choice == '3':
            confirm = input("\nAre you sure you want to log out? (y/n): ").lower().strip()
            if confirm == 'y':
                log_out()
                exit() # Exit the application after logging out
        elif choice == 'b':
            return
        else:
            print("\n[ERROR] Invalid choice. Please try again.")
            time.sleep(1.5)

def main():
    """Main function to run the MidKnight application."""
    config = load_config()
    if not config:
        config = first_time_setup()

    display_welcome()
    display_intro_message(config["name"])
    input("Press Enter to continue...")

    while True:
        clear_screen()
        display_welcome()
        display_menu()
        choice = input("  Enter your choice: ").strip().lower()

        if choice == '1':
            download_starter_kit()
        elif choice == '2':
            analyze_code()
        elif choice == '3':
            run_and_fix_code()
        elif choice == 's':
            settings_menu(config)
        elif choice == 'q':
            print("\nExiting MidKnight. Happy coding!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()

