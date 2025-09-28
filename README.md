# MidKnight 
```d
███╗   ███╗ ██╗ ██████╗  ██╗  ██╗ ███╗   ██╗ ██╗  ██████╗  ██╗  ██╗ ████████╗
████╗ ████║ ██║ ██╔══██╗ ██║ ██╔╝ ████╗  ██║ ██║ ██╔════╝  ██║  ██║ ╚══██╔══╝
██╔████╔██║ ██║ ██║  ██║ █████╔╝  ██╔██╗ ██║ ██║ ██║  ███╗ ███████║    ██║
██║╚██╔╝██║ ██║ ██║  ██║ ██╔═██╗  ██║╚██╗██║ ██║ ██║   ██║ ██╔══██║    ██║
██║ ╚═╝ ██║ ██║ ██████╔╝ ██║ ╚██╗ ██║ ╚████║ ██║ ╚██████╔╝ ██║  ██║    ██║
╚═╝     ╚═╝ ╚═╝ ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═════╝  ╚═╝  ╚═╝    ╚═╝
```
**MidKnight** is a command-line assistant designed to help you build **secure, private, and robust applications** on the **Midnight blockchain**

It combines the **power of AI (Google Gemini)** with a **Python analysis engine** and a **Node.js CLI wrapper**, giving developers an intuitive way to:

* Analyze smart contracts for **security, correctness, and best practices**.
* Bootstrap new projects with **sample contract templates**.
* Ask AI-powered **development questions** directly in the terminal.

This project was built for the **Midnight Hackathon (Midnight Hackathon 2025)**.

---

## ✨ Features

* 🔍 **Smart Contract Analysis** — Scan and review your Midnight contracts with AI suggestions.
* 🛠 **AI-Powered CLI** — A single binary (`midnight-ai`) that runs cross-platform.
* 🤖 **Google Gemini Integration** — Uses Gemini for contract insights, security advice, and Q&A.
* 🔐 **Security-First** — Keeps your API key private via `.env` support.
* 🧩 **Sample Contracts Included** — A TypeScript starter (`sample_contract.ts`) to help you get going.
* ⚡ **Cross-Language Design** — Node.js CLI orchestrates a Python backend for powerful analysis.

---

## 📂 Project Structure

```plaintext
.
├── index.js             # Node.js CLI entrypoint (bridges to Python backend)
├── analyser.py          # Python analyzer (handles AI contract analysis logic)
├── midknight.py         # Main Python CLI assistant logic
├── sample_contract.ts   # Example Midnight smart contract
├── requirements.txt     # Python dependencies (dotenv, Gemini SDK, rich UI)
├── package.json         # Node.js metadata and CLI registration
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sherwinvishesh/MidKnight.git
cd midknight
```

### 2. Install dependencies

#### Python (backend)

```bash
python3 -m venv .venv
source .venv/bin/activate   # (on Linux/macOS)
# OR .venv\Scripts\activate  # (on Windows)

pip install -r requirements.txt
```

#### Node.js (CLI wrapper)

```bash
npm install -g .
```

This will install the `midnight-ai` command globally on your system.


---

## 🕹 Usage

### Run the CLI

```bash
# from the project root
python3 midknight.py
```
or you can just
```bash
# from the project root
midknight 
```
in the terminal

On first launch you’ll see a welcome screen and be guided through a quick setup:

1. Enter the name you’d like MidKnight to call you
2. Paste your **Gemini API key**

These are saved to a persistent config at:

* **macOS/Linux:** `~/.midknight/config.json`
* **Windows (PowerShell):** `C:\Users\<you>\.midknight\config.json`

---

### Main Flow (interactive)

After setup:

1. **Welcome & Intro**
   You’ll see the MidKnight ASCII banner and a short intro. Press **Enter** to continue.

2. **Main Menu**

   ```
   ========================================
                MAIN MENU
   ========================================
     1. Midnight Starter Kit
     2. Code Analyser

     s. Settings
     q. Quit
   ========================================
   ```

#### 1) Midnight Starter Kit

Downloads a ready-to-build starter into a new folder.

* You’ll be prompted for a **project name** (e.g., `my-dapp`).
* MidKnight checks for **git**. If it’s missing, you’ll get install guidance.
* If the target folder already exists, you can choose to **overwrite** it.
* On success, the starter kit is cloned into `./<project-name>`.

> Tip: Choose a simple, hyphenated name (the CLI will replace spaces with `-`).

#### 2) Code Analyser

Runs the code review workflow on a file or directory.

* You’ll be prompted for a **path** (press **Enter** for current directory `.`).
* MidKnight loads your saved API key and runs the analyzer, streaming results to your terminal.
* Non-zero exit codes are reported so you can quickly spot failures.

#### s) Settings

Manage your local configuration.

* **Change Name** – update the friendly name MidKnight uses to greet you.
* **Change Gemini API Key** – securely update your key (stored in `~/.midknight/config.json`).
* **Log Out** – deletes your config; next launch will re-run first-time setup.
* **Back** – return to the main menu.

#### q) Quit

Exits the application gracefully.

---

### Non-interactive quick start

If you prefer to invoke directly without navigating menus (e.g., from a script), you can still run the CLI and follow the prompts inline:

```bash
# Start MidKnight; follow the prompts
python3 midknight.py
```

---

### Troubleshooting

* **Git not found** when downloading the starter kit → install from [https://git-scm.com/downloads](https://git-scm.com/downloads) and rerun.
* **Analyzer errors** → the CLI will show the exit code and any available message. Re-run after fixing the highlighted issue.
* **Reset everything** → run **Settings → Log Out**, then start MidKnight again to redo setup.

---

## 📦 Dependencies

### Python (`requirements.txt`)

* [`python-dotenv`](https://pypi.org/project/python-dotenv/) — load `.env` keys securely.
* [`google-generativeai`](https://pypi.org/project/google-generativeai/) — Gemini AI SDK.
* [`rich`](https://pypi.org/project/rich/) — pretty CLI output. 

### Node.js (`package.json`)

* Provides CLI metadata, binary mapping, and script hooks .
* Uses `child_process.spawn` to call into Python backend .

---

## 🛡 Security

* API keys are never hardcoded; always read from environment variables.
* Analysis is run locally with Python + Gemini, no unnecessary data leakage.
* Contract templates encourage **secure-by-default** coding practices.

---

## 🧑‍💻 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-idea`)
3. Commit your changes (`git commit -m "Add cool feature"`)
4. Push to the branch (`git push origin feature/my-idea`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **Apache License 2.0**.

---

## 🙌 Acknowledgements

* **Midnight Blockchain** for the platform.
* **Google Gemini AI** for powering smart analysis.
* **Midnight Hackathon** for inspiring this project.

---

