# Python 101 for Pharmacists
### A Practical Introduction to Programming for Healthcare Professionals

*No computer science background required.*

---

## Table of Contents

- [Introduction](#introduction)
  - [What is Programming?](#what-is-programming)
  - [Why Python for Pharmacists?](#why-python-for-pharmacists)
  - [How to Use This Handbook](#how-to-use-this-handbook)
- [Chapter 1: Setting Up Python](#chapter-1-setting-up-python)
- [Chapter 2: Variables and Data Types](#chapter-2-variables-and-data-types)
- [Chapter 3: Operators and Expressions](#chapter-3-operators-and-expressions)
- [Chapter 4: Strings and String Manipulation](#chapter-4-strings-and-string-manipulation)
- [Chapter 5: Lists and Tuples](#chapter-5-lists-and-tuples)
- [Chapter 6: Dictionaries and Sets](#chapter-6-dictionaries-and-sets)
- [Chapter 7: Control Flow — Conditionals](#chapter-7-control-flow--conditionals)
- [Chapter 8: Control Flow — Loops](#chapter-8-control-flow--loops)
- [Chapter 9: Functions](#chapter-9-functions)
- [Chapter 10: File Handling](#chapter-10-file-handling)
- [Chapter 11: Error Handling](#chapter-11-error-handling)
- [Mini-Project 1: Medication Tracker](#mini-project-1-medication-tracker)
- [Mini-Project 2: Prescription Label Generator](#mini-project-2-prescription-label-generator)
- [Mini-Project 3: Dose Safety Checker](#mini-project-3-dose-safety-checker)
- [Final Challenge: Pharmacy Management Script](#final-challenge-pharmacy-management-script)
- [What's Next](#whats-next)

---

## Introduction

Welcome to *Python 101 for Pharmacists*. This handbook is written specifically for pharmacists and pharmacy students who have never written a line of code. You don't need a computer science degree, a mathematics background, or any prior experience with software. What you do need is curiosity and a willingness to try things out.

By the time you finish this handbook, you will be able to write Python programs that automate dose calculations, manage patient medication lists, generate prescription labels, read and write patient data files, and flag potential safety issues — all using real pharmacy workflows as your guide.

---

### What is Programming?

Think about a prescription. When a prescriber writes a prescription, they are giving a precise, ordered set of instructions: the drug name, the dose, the route of administration, the frequency, and the duration. The pharmacist reads those instructions and carries them out exactly. There is no room for ambiguity — "take as needed" must be clarified before dispensing.

A computer program works the same way. A program is a precise, ordered set of instructions that tells a computer exactly what to do, step by step. The computer, like a diligent pharmacist, follows those instructions faithfully and without interpretation. If the instructions are clear and correct, the outcome is predictable. If there is an error — a wrong dose, a missing step — the program will either produce the wrong result or stop and report a problem.

Here is a simple analogy side by side:

| Prescription | Program |
|---|---|
| Drug name: Amoxicillin | Variable: `drug_name = "Amoxicillin"` |
| Dose: 500 mg | Variable: `dose_mg = 500` |
| Frequency: three times daily | Calculation: `daily_dose = dose_mg * 3` |
| Duration: 10 days | Loop: repeat for 10 days |
| Dispense 30 capsules | Output: `print(f"Dispense {30} capsules")` |

Just as a prescription is written in a specific language (Latin abbreviations, standard units, recognised drug names), a program is written in a programming language. This handbook teaches you **Python** — one of the most readable and widely used programming languages in the world.

Programming is not about memorising syntax. It is about learning to think in steps: break a problem down into small, clear instructions, and then express those instructions in a language the computer understands. You already do this every day when you verify a prescription, counsel a patient, or calculate a paediatric dose. Programming is just a new way to apply that same logical thinking.

---

### Why Python for Pharmacists?

There are dozens of programming languages. Python is the right choice for pharmacists for several reasons:

**Readable syntax.** Python code reads almost like plain English. Compare `if dose > max_dose:` to the equivalent in some other languages — Python wins on clarity every time. This matters when you are learning, and it matters when you come back to code you wrote six months ago.

**It is free and open source.** Python costs nothing to download, install, or use. There are no licences to manage, no subscription fees, and no vendor lock-in. You can install it on your work computer, your home laptop, and a Raspberry Pi in the dispensary.

**Widely used in healthcare and data analysis.** Python is the dominant language in data science, bioinformatics, clinical research, and health informatics. Libraries like `pandas` (data analysis), `matplotlib` (charts), and `numpy` (numerical computing) are used in hospitals, pharmaceutical companies, and research institutions worldwide. Learning Python opens doors to analysing prescription data, building clinical decision support tools, and contributing to healthcare software projects.

**Automate repetitive tasks.** Pharmacists spend significant time on tasks that follow predictable patterns: checking dose ranges, formatting labels, reconciling medication lists, generating reports. Python can automate all of these. A script that takes ten seconds to run can replace thirty minutes of manual work — and it will make the same decision every time, without fatigue.

**A large, supportive community.** Python has one of the largest programming communities in the world. Whatever problem you encounter, someone has almost certainly solved it and posted the solution online. The official Python documentation is thorough and beginner-friendly.

---

### How to Use This Handbook

This handbook is designed to be worked through **linearly**, from Chapter 1 to the Final Challenge. Each chapter builds on the concepts introduced in previous chapters. Skipping ahead is possible, but you may find later chapters harder to follow if you have not read the earlier ones.

**Try every code example.** Reading code is not the same as writing code. Every time you see a code block in this handbook, open your Python environment and type it out — or paste it in and then modify it. Change a variable name. Change a number. See what happens. This is how programming is learned: by doing, breaking things, and fixing them.

**Complete the quizzes.** Each chapter ends with a short quiz. Answer the questions before looking at the answer key. The quizzes are not graded — they are a tool for you to check your own understanding. If you get a question wrong, re-read the relevant section before moving on.

**Complete the challenges.** After each quiz there is a hands-on coding challenge. These are small programs you write yourself, based on a pharmacy scenario. They are the most important part of each chapter. The reference solution is provided, but try to write your own solution first. Your solution does not have to match the reference exactly — there are many correct ways to write a program.

**Use the mini-projects as milestones.** After Chapter 11 there are three mini-projects that combine everything you have learned. Treat these as your practical assessments. If you can complete all three mini-projects, you have genuinely learned to program in Python.

**Don't worry about memorising syntax.** Professional programmers look things up constantly. The goal is not to memorise every method name or operator — it is to understand the concepts well enough that you know what to search for when you need it.

You are ready to begin. Let's start by getting Python installed on your computer.

---

## Chapter 1: Setting Up Python

### Learning Objectives

By the end of this chapter you will be able to:

- Download and install Python 3 on your computer (Windows, macOS, or Linux)
- Understand what PATH is and why it matters
- Verify that Python is installed correctly by running a command in your terminal

---

### 1.1 Installing Python 3

Before you can write a single line of Python, you need to install it on your computer. This section walks you through the process step by step for each major operating system. Follow only the section that matches your computer.

> **Which version?** Always install **Python 3**. Python 2 is no longer supported and is not covered in this handbook. At the time of writing, the current stable release is Python 3.12, but any Python 3.x version will work for everything in this handbook.

---

#### Installing Python 3 on Windows

**Step 1 — Download the installer**

1. Open your web browser and go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. The website will detect that you are on Windows and show a large yellow button labelled **"Download Python 3.x.x"**. Click it.
3. A file named something like `python-3.12.x-amd64.exe` will download to your Downloads folder. Wait for it to finish.

**Step 2 — Run the installer**

1. Open your Downloads folder and double-click the file you just downloaded.
2. A setup window will appear. **Before you click anything else**, look at the bottom of the window. You will see a checkbox labelled **"Add Python 3.x to PATH"**.

   > **This checkbox is critical.** If you do not tick it, Windows will not know where to find Python when you type commands, and you will get errors like `'python' is not recognized as an internal or external command`. Tick it now.

3. Tick the **"Add Python 3.x to PATH"** checkbox.
4. Click **"Install Now"** (the top option). This installs Python with the recommended settings.
5. If Windows asks "Do you want to allow this app to make changes to your device?", click **Yes**.
6. Wait for the installation to complete. When you see "Setup was successful", click **Close**.

**Step 3 — What is PATH and why does it matter?**

When you type a command like `python` into the Command Prompt, Windows searches a list of folders on your computer to find a program with that name. This list of folders is called the **PATH**. Think of it like a list of filing cabinets Windows checks, in order, until it finds what it is looking for.

When you ticked "Add Python to PATH" during installation, the installer added Python's folder to that list. Without this step, Windows would not know where Python lives, and every time you tried to run Python you would get an error. With it ticked, you can type `python` from any folder on your computer and Windows will find it immediately.

If you forgot to tick the checkbox, the easiest fix is to run the installer again, choose "Modify", and tick the PATH option.

**Step 4 — Verify the installation**

1. Press the **Windows key**, type `cmd`, and press **Enter** to open the Command Prompt. A black window with a blinking cursor will appear.
2. Type the following command and press **Enter**:

```
python --version
```

3. You should see output like:

```
Python 3.12.3
```

If you see a version number starting with 3, Python is installed correctly. If you see an error, go back and check that you ticked the PATH checkbox during installation.

---

#### Installing Python 3 on macOS

macOS comes with an older version of Python pre-installed, but it is Python 2, which is outdated. You need to install Python 3 separately.

You have two options: download from python.org (simpler, recommended for beginners) or use Homebrew (preferred by developers who already use it).

**Option A — Download from python.org (recommended for beginners)**

**Step 1 — Download the installer**

1. Open Safari or your preferred browser and go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. The site will detect macOS and show a download button for the latest Python 3 release. Click it.
3. A `.pkg` file will download to your Downloads folder.

**Step 2 — Run the installer**

1. Open your Downloads folder and double-click the `.pkg` file.
2. A setup wizard will open. Click **Continue** through each screen, agree to the licence, and click **Install**.
3. macOS may ask for your password (the same one you use to log in to your Mac). Enter it and click **Install Software**.
4. When the installation finishes, click **Close**.

**Step 3 — Verify the installation**

1. Open the **Terminal** application. You can find it by pressing **Command + Space**, typing `Terminal`, and pressing **Enter**.
2. Type the following command and press **Enter**:

```
python3 --version
```

3. You should see output like:

```
Python 3.12.3
```

> **Note for macOS users:** On macOS, the command is `python3`, not `python`. This is because macOS reserves the `python` command for the old system Python 2. Always use `python3` on a Mac.

---

**Option B — Install using Homebrew**

If you already have Homebrew installed (a popular package manager for macOS), you can install Python 3 with a single command. Open Terminal and run:

```
brew install python3
```

Homebrew will download and install Python 3 automatically. Once it finishes, verify with:

```
python3 --version
```

If you do not have Homebrew and would like to install it, visit [https://brew.sh](https://brew.sh) for instructions. For most beginners, Option A (the python.org installer) is simpler.

---

#### Installing Python 3 on Linux (Ubuntu / Debian)

Most Linux distributions come with Python 3 already installed. The steps below are for Ubuntu and Debian-based systems (such as Linux Mint, Pop!_OS, and Raspberry Pi OS). If you are using a different distribution, the package manager commands will differ slightly, but the process is the same.

**Step 1 — Open a Terminal**

Press **Ctrl + Alt + T** to open a terminal window, or search for "Terminal" in your applications menu.

**Step 2 — Update your package list**

Before installing anything, it is good practice to update the list of available packages so you get the latest version. Run:

```
sudo apt update
```

You will be prompted for your password. Type it and press **Enter**. (You will not see the characters as you type — this is normal on Linux.)

**Step 3 — Install Python 3**

```
sudo apt install python3
```

The terminal will show a list of packages to be installed and ask you to confirm. Press **Y** and then **Enter** to proceed. The installation will complete in a minute or two.

**Step 4 — Verify the installation**

```
python3 --version
```

You should see output like:

```
Python 3.12.3
```

> **Note for Linux users:** Like macOS, Linux uses `python3` as the command name to distinguish it from the legacy Python 2. Always use `python3` in your terminal.

---

### Verification Summary

Once installation is complete, use the table below to confirm everything is working:

| Operating System | Command to run | Expected output |
|---|---|---|
| Windows | `python --version` | `Python 3.x.x` |
| macOS | `python3 --version` | `Python 3.x.x` |
| Linux (Ubuntu/Debian) | `python3 --version` | `Python 3.x.x` |

If you see a version number starting with 3, you are ready to move on. If you see an error, re-read the installation steps for your operating system and make sure you did not skip any steps.

---

### Chapter Summary

- Python 3 is free and available at [python.org](https://www.python.org/downloads/).
- On **Windows**, tick "Add Python to PATH" during installation — this is the most common source of beginner errors.
- On **macOS** and **Linux**, use the `python3` command (not `python`).
- Always verify your installation by running `python --version` (Windows) or `python3 --version` (macOS/Linux) in your terminal.
- PATH is the list of folders your operating system searches when you type a command — Python must be on this list to work from any location.

---

### 1.2 The Python Interactive Shell (REPL)

Now that Python is installed, the fastest way to start experimenting is the **interactive shell**, also called the **REPL**.

**REPL** stands for **Read-Evaluate-Print Loop**:

- **Read** — Python reads the line you type.
- **Evaluate** — Python runs it immediately.
- **Print** — Python prints the result.
- **Loop** — Python waits for your next line.

Think of the REPL as a conversation with Python. You type something, Python responds instantly. It is perfect for testing a quick calculation or trying out a new idea without creating a file.

---

#### Opening the REPL

**On Windows:**

1. Press the **Windows key**, type `cmd`, and press **Enter** to open the Command Prompt.
2. Type the following and press **Enter**:

```
python
```

**On macOS or Linux:**

1. Open the **Terminal** application.
2. Type the following and press **Enter**:

```
python3
```

In both cases, you will see a welcome message followed by the `>>>` prompt:

```
Python 3.12.3 (main, Apr  9 2024, 08:17:23)
[GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is Python's way of saying: *I am ready. What would you like me to do?*

---

#### Your First Pharmacy Example

At the `>>>` prompt, type the following and press **Enter**:

```python
>>> print("Hello, Pharmacist!")
Hello, Pharmacist!
```

Python read your instruction, evaluated it, and printed the result immediately. That is the REPL in action.

Now try a few more examples. Type each line and press **Enter** after each one:

```python
>>> drug_name = "Amoxicillin"
>>> dose_mg = 500
>>> print(drug_name)
Amoxicillin
>>> print(dose_mg * 3)
1500
```

Here is what happened step by step:

1. `drug_name = "Amoxicillin"` — you stored the text `"Amoxicillin"` in a variable called `drug_name`. Python remembered it.
2. `dose_mg = 500` — you stored the number `500` in a variable called `dose_mg`.
3. `print(drug_name)` — Python retrieved the value of `drug_name` and printed it.
4. `print(dose_mg * 3)` — Python multiplied 500 by 3 and printed `1500` — the total daily dose if taken three times a day.

You can also type an expression directly without `print()` and Python will display the result:

```python
>>> dose_mg * 3
1500
>>> drug_name
'Amoxicillin'
```

---

#### When to Use the REPL

The REPL is ideal for:

- **Quick experiments** — testing a calculation before putting it in a script.
- **Checking syntax** — not sure if a line of code is correct? Try it in the REPL first.
- **Exploring Python** — trying out a new function or method to see what it does.
- **Learning** — the instant feedback loop makes it the best environment for beginners.

The REPL is *not* ideal for writing programs you want to save and run again later. For that, you need a script file — which is covered in the next section.

---

#### Exiting the REPL

When you are done, you can exit the REPL in two ways:

- Type `exit()` and press **Enter**.
- Press **Ctrl + D** on macOS or Linux.
- Press **Ctrl + Z** and then **Enter** on Windows.

```python
>>> exit()
```

You will be returned to your normal terminal prompt.

---

### 1.3 Creating and Running a Python Script File

The REPL is great for quick experiments, but anything you want to save, share, or run again needs to live in a **script file** — a plain text file with a `.py` extension.

A `.py` file is simply a text file containing Python code. When you run it, Python reads the file from top to bottom and executes every line in order, just as if you had typed each line into the REPL yourself.

---

#### Step 1 — Create the file

Open any plain text editor:

- **Windows:** Notepad (search for it in the Start menu)
- **macOS:** TextEdit (make sure it is in plain text mode: Format → Make Plain Text)
- **Linux:** gedit, nano, or any text editor you prefer

Create a new file and type the following code exactly as shown:

```python
# My first pharmacy script
drug_name = "Amoxicillin"
dose_mg = 500
frequency = "three times daily"
print(f"Drug: {drug_name}")
print(f"Dose: {dose_mg} mg")
print(f"Frequency: {frequency}")
print(f"Total daily dose: {dose_mg * 3} mg")
```

> **What is the `#` symbol?** Lines that start with `#` are **comments**. Python ignores them completely — they are notes for the human reading the code. Use comments to explain what your code does.

> **What are the `f"..."` strings?** These are called **f-strings** (formatted strings). The `f` before the opening quote tells Python to look for `{variable_name}` placeholders inside the string and replace them with the actual values. You will learn more about f-strings in Chapter 4.

---

#### Step 2 — Save the file

Save the file with the name `first_script.py`.

- Make sure the file extension is `.py`, not `.py.txt` (a common mistake in Notepad on Windows).
- Save it somewhere easy to find, such as your Desktop or a folder called `python_scripts`.

> **Notepad tip (Windows):** When saving in Notepad, change "Save as type" from "Text Documents (*.txt)" to "All Files (*.*)", then type `first_script.py` as the filename. This prevents Notepad from adding `.txt` to the end.

---

#### Step 3 — Open your terminal in the right folder

Before you can run the script, your terminal needs to be in the same folder where you saved the file.

**On Windows:**

1. Open the Command Prompt.
2. Navigate to the folder where you saved the file. For example, if you saved it on the Desktop:

```
cd Desktop
```

Or if you saved it in a folder called `python_scripts` inside your Documents:

```
cd Documents\python_scripts
```

**On macOS or Linux:**

1. Open the Terminal.
2. Navigate to the folder. For example, if you saved it on the Desktop:

```
cd ~/Desktop
```

---

#### Step 4 — Run the script

**On Windows:**

```
python first_script.py
```

**On macOS or Linux:**

```
python3 first_script.py
```

---

#### Expected output

When you run the script, you should see the following printed in your terminal:

```
Drug: Amoxicillin
Dose: 500 mg
Frequency: three times daily
Total daily dose: 1500 mg
```

Congratulations — you have just written and run your first Python pharmacy script.

---

#### Script files vs. the REPL — a quick comparison

| | REPL | Script file |
|---|---|---|
| Best for | Quick experiments, learning | Programs you want to save and reuse |
| How to run | Type `python` or `python3` | `python filename.py` |
| Saves your work? | No — lost when you close the terminal | Yes — saved as a `.py` file |
| Runs line by line? | Yes, immediately | Yes, from top to bottom |

---

### 1.4 Setting Up VS Code

Notepad and TextEdit can open and save `.py` files, but they offer no help when you are writing code. A proper **code editor** makes programming significantly easier, especially as your scripts grow longer.

A good code editor gives you:

- **Syntax highlighting** — different parts of your code appear in different colours, making it much easier to read.
- **Auto-completion** — the editor suggests variable names and function names as you type, reducing typos.
- **Error highlighting** — the editor underlines mistakes before you even run the code.
- **An integrated terminal** — you can run your scripts without switching windows.

The editor recommended in this handbook is **Visual Studio Code** (VS Code). It is free, works on Windows, macOS, and Linux, and has excellent Python support.

---

#### Step 1 — Download and install VS Code

1. Open your browser and go to [https://code.visualstudio.com](https://code.visualstudio.com).
2. The website will detect your operating system and show a download button. Click **Download for [your OS]**.
3. Once the download finishes, run the installer:
   - **Windows:** Double-click the `.exe` file and follow the setup wizard. Accept the default options. On the "Select Additional Tasks" screen, it is helpful to tick **"Add to PATH"** and **"Open with Code"** context menu options.
   - **macOS:** Open the downloaded `.zip` file, drag the **Visual Studio Code** application to your **Applications** folder.
   - **Linux (Ubuntu/Debian):** Download the `.deb` package and install it with `sudo dpkg -i code_*.deb`, or follow the instructions on the VS Code website for your distribution.
4. Launch VS Code. You will see a welcome screen.

---

#### Step 2 — Install the Python extension

VS Code supports many programming languages, but Python support is provided by an extension that you need to install once.

1. In VS Code, look at the left-hand sidebar. You will see a column of icons. Click the **Extensions** icon — it looks like four squares, with one square slightly separated from the others. Alternatively, press **Ctrl + Shift + X** (Windows/Linux) or **Cmd + Shift + X** (macOS).
2. A search box will appear at the top of the Extensions panel. Type `Python` and press **Enter**.
3. The first result should be **"Python"** published by **Microsoft**. It will have millions of downloads and a blue verified badge.
4. Click the **Install** button next to it.
5. VS Code will download and install the extension. This takes about 30 seconds.

Once installed, VS Code will automatically detect your Python installation and use it to run your scripts.

---

#### Step 3 — Open a folder in VS Code

It is good practice to keep all your Python files for this handbook in one folder. VS Code works best when you open a whole folder rather than individual files.

1. Create a new folder on your computer called `pharmacy_python` (on your Desktop or Documents, wherever you prefer).
2. In VS Code, go to **File → Open Folder** (Windows/Linux) or **File → Open...** (macOS).
3. Navigate to the `pharmacy_python` folder you just created and click **Select Folder** (or **Open** on macOS).
4. VS Code will open the folder. You will see it listed in the **Explorer** panel on the left side.

---

#### Step 4 — Create a new Python file

1. In the Explorer panel on the left, you will see the name of your folder at the top. Hover over it and click the **New File** icon (a page with a plus sign).
2. Type `first_script.py` and press **Enter**.
3. A new empty file will open in the editor.
4. Type (or paste) the pharmacy script from Section 1.3:

```python
# My first pharmacy script
drug_name = "Amoxicillin"
dose_mg = 500
frequency = "three times daily"
print(f"Drug: {drug_name}")
print(f"Dose: {dose_mg} mg")
print(f"Frequency: {frequency}")
print(f"Total daily dose: {dose_mg * 3} mg")
```

5. Save the file with **Ctrl + S** (Windows/Linux) or **Cmd + S** (macOS).

---

#### Step 5 — Run the script from VS Code

You have two ways to run a Python file in VS Code:

**Option A — The Run button**

Look at the top-right corner of the editor window. You will see a **play button** (a triangle pointing to the right). Click it. VS Code will open an integrated terminal at the bottom of the screen and run your script automatically. You will see the output appear in that terminal.

**Option B — The integrated terminal**

1. Open the integrated terminal by going to **Terminal → New Terminal** in the menu bar, or press **Ctrl + `` ` ``** (the backtick key, usually top-left on your keyboard).
2. A terminal panel will appear at the bottom of VS Code. It will already be in your `pharmacy_python` folder.
3. Type the run command for your operating system and press **Enter**:

   - **Windows:** `python first_script.py`
   - **macOS / Linux:** `python3 first_script.py`

Either way, you should see the same output as before:

```
Drug: Amoxicillin
Dose: 500 mg
Frequency: three times daily
Total daily dose: 1500 mg
```

From this point on, this handbook assumes you are using VS Code to write and run your Python scripts. All code examples can be typed directly into `.py` files and run using either method above.

---

### Chapter Summary

- The **REPL** (Read-Evaluate-Print Loop) is Python's interactive shell. Open it with `python` (Windows) or `python3` (macOS/Linux). Use it for quick experiments and testing small snippets.
- The `>>>` prompt means Python is ready for your input.
- A **script file** is a `.py` text file containing Python code. Run it with `python filename.py` (Windows) or `python3 filename.py` (macOS/Linux).
- **VS Code** is a free code editor that makes writing Python much easier with syntax highlighting, auto-completion, and an integrated terminal.
- Install the **Microsoft Python extension** in VS Code to enable full Python support.
- Exit the REPL with `exit()`, **Ctrl + D** (macOS/Linux), or **Ctrl + Z then Enter** (Windows).

---

### 1.5 Common Installation and Setup Errors

Even when you follow the installation steps carefully, things can go wrong. This section covers the four most common errors beginners encounter when setting up Python for the first time. For each error you will find the exact message you will see, what causes it, and the steps to fix it.

---

#### Error 1 — Python not in PATH (Windows)

**The error message:**

```
'python' is not recognized as an internal or external command,
operable program or batch file.
```

**What causes it:**

During installation, the Windows installer shows a checkbox at the bottom of the first screen labelled **"Add Python 3.x to PATH"**. If this checkbox was not ticked, Windows does not know where Python is installed. When you type `python` in the Command Prompt, Windows searches its list of known folders (the PATH) and cannot find Python anywhere on that list.

**How to fix it:**

You have two options:

*Option A — Re-run the installer (recommended for beginners):*

1. Open your Downloads folder and double-click the Python installer again (or download it again from [python.org](https://www.python.org/downloads/) if you deleted it).
2. This time, instead of "Install Now", click **"Modify"**.
3. On the next screen, make sure **"Add Python to environment variables"** is ticked.
4. Click **Next**, then **Install**.
5. Once complete, close and reopen the Command Prompt and try `python --version` again.

*Option B — Add Python to PATH manually:*

1. Press the **Windows key**, search for **"Environment Variables"**, and click **"Edit the system environment variables"**.
2. In the System Properties window, click **"Environment Variables..."**.
3. Under "System variables", find the variable named **Path** and double-click it.
4. Click **New** and add the path to your Python installation. This is usually something like:
   ```
   C:\Users\YourName\AppData\Local\Programs\Python\Python312\
   C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts\
   ```
5. Click **OK** on all windows to save.
6. Close and reopen the Command Prompt, then run `python --version` to confirm.

---

#### Error 2 — FileNotFoundError when running a script

**The error message:**

```
python: can't open file 'first_script.py': [Errno 2] No such file or directory
```

**What causes it:**

Your terminal is not in the same folder as the script file. When you type `python first_script.py`, Python looks for that file in the folder your terminal is currently in — not on your entire computer. If you saved the file on your Desktop but your terminal is pointing at a different folder (such as your home directory), Python cannot find the file.

**How to fix it:**

Use the `cd` command (short for "change directory") to navigate to the folder where your script is saved before running it.

If you saved your script on the Desktop:

```
cd Desktop
```

On macOS or Linux, use:

```
cd ~/Desktop
```

If you saved it in a folder called `pharmacy_python` inside your Documents:

```
cd Documents/pharmacy_python
```

On Windows:

```
cd Documents\pharmacy_python
```

Once you are in the correct folder, run the script again:

```
python first_script.py
```

> **Tip:** You can always check which folder your terminal is currently in by typing `pwd` (macOS/Linux) or `cd` with no arguments (Windows). The terminal will print the current folder path.

---

#### Error 3 — SyntaxError in the REPL

**The error message:**

```
SyntaxError: invalid syntax
```

or

```
SyntaxError: expected ':'
```

**What causes it:**

A `SyntaxError` means Python could not understand the line you wrote because it does not follow the rules of the Python language — similar to a grammatical error in a sentence. Python cannot even begin to run the code; it stops as soon as it spots the problem.

The most common causes are:

- **Missing colon** after `if`, `for`, `while`, or `def` statements
- **Wrong indentation** — Python uses indentation to define blocks of code, and inconsistent spacing causes errors
- **Mismatched quotes** — opening a string with `"` but closing it with `'`, or forgetting to close a quote at all
- **Typos in keywords** — writing `pritn` instead of `print`, or `iff` instead of `if`

**A pharmacy example — the error:**

Suppose you are writing a simple dose check in the REPL and you forget the colon after `if`:

```python
>>> dose_mg = 600
>>> max_dose = 500
>>> if dose_mg > max_dose
  File "<stdin>", line 1
    if dose_mg > max_dose
                         ^
SyntaxError: expected ':'
```

Python is pointing at the end of the line and telling you it expected a `:` there.

**The corrected version:**

```python
>>> dose_mg = 600
>>> max_dose = 500
>>> if dose_mg > max_dose:
...     print("Warning: dose exceeds maximum")
...
Warning: dose exceeds maximum
```

The fix is simply to add the colon at the end of the `if` line. Notice that after you type the `if` line correctly, the REPL shows `...` instead of `>>>` — this means Python is waiting for the indented block that follows the `if` statement. Press **Enter** on a blank line to finish the block.

> **Remember:** A `SyntaxError` is not a sign that you are bad at programming. Every programmer encounters them constantly. Read the error message carefully — Python usually points directly at the problem with a `^` symbol.

---

#### Error 4 — ModuleNotFoundError

**The error message:**

```
ModuleNotFoundError: No module named 'csv'
```

or, for a third-party module:

```
ModuleNotFoundError: No module named 'pandas'
```

**What causes it:**

Python comes with a large collection of built-in modules (like `csv`, `os`, `math`, and `datetime`) that are available immediately without any installation. It also has a vast ecosystem of third-party modules (like `pandas`, `numpy`, and `requests`) that must be installed separately before you can use them.

A `ModuleNotFoundError` usually means one of two things:

1. **The module is third-party and has not been installed yet.** You need to install it using `pip`, Python's package installer.
2. **You are using the wrong Python environment.** If you have multiple Python versions installed, you might be running a version that does not have the module installed.

> **Special note about `csv`:** The `csv` module is built into Python — you should never need to install it. If you see `ModuleNotFoundError: No module named 'csv'`, this almost always means you are accidentally running Python 2 instead of Python 3, or there is a file in your folder named `csv.py` that is conflicting with the built-in module.

**How to fix it:**

*For third-party modules (e.g., `pandas`, `numpy`, `requests`):*

Open your terminal and run:

```
pip install module_name
```

For example, to install `pandas`:

```
pip install pandas
```

On macOS or Linux, you may need to use `pip3` instead:

```
pip3 install pandas
```

After installation completes, try importing the module again.

*For built-in modules like `csv`:*

If you see this error for a built-in module, check which Python version is running:

```
python --version
```

or

```
python3 --version
```

Make sure you are running Python 3. If you see `Python 2.x.x`, use `python3` instead of `python` to run your scripts.

Also check that you do not have a file in your current folder named `csv.py` — if you do, rename it to something else, as it will shadow the built-in `csv` module.

---

### Chapter 1 Summary

Here is a recap of everything covered in Chapter 1:

- **Installing Python 3:** Download the installer from [python.org](https://www.python.org/downloads/). On Windows, always tick **"Add Python to PATH"** during installation. On macOS and Linux, use the `python3` command.
- **Verifying installation:** Run `python --version` (Windows) or `python3 --version` (macOS/Linux) in your terminal. A version number starting with 3 confirms success.
- **PATH:** The list of folders your operating system searches when you type a command. Python must be on this list to work from any location. Forgetting to add Python to PATH is the most common Windows setup error.
- **The REPL:** Python's interactive shell. Open it with `python` (Windows) or `python3` (macOS/Linux). The `>>>` prompt means Python is ready. Use it for quick experiments and testing. Exit with `exit()`.
- **Script files:** Plain text files with a `.py` extension. Write your code in a text editor, save the file, navigate to its folder in the terminal using `cd`, and run it with `python filename.py` or `python3 filename.py`.
- **VS Code:** A free code editor with syntax highlighting, auto-completion, error highlighting, and an integrated terminal. Install the Microsoft Python extension to enable full Python support.
- **Common errors:**
  - `'python' is not recognized` — Python is not in PATH. Re-run the installer and tick the PATH option.
  - `No such file or directory` — your terminal is not in the same folder as your script. Use `cd` to navigate there.
  - `SyntaxError` — a typo or missing punctuation in your code (often a missing `:`). Read the error message and look at the line Python points to.
  - `ModuleNotFoundError` — a third-party module needs to be installed with `pip install module_name`, or you are running the wrong Python version.

---

## Chapter 2: Variables and Data Types

### Learning Objectives

By the end of this chapter you will be able to:

- Explain what a variable is and why variables are useful in programs
- Assign values to variables using pharmacy-relevant examples
- Identify and use the four primitive data types: `int`, `float`, `str`, and `bool`
- Use the `type()` function to inspect the type of any value
- Explain Python's dynamic typing and demonstrate reassigning a variable to a different type
- Convert between data types using `int()`, `float()`, and `str()`
- Recognise what happens when a type conversion fails

---

### 2.1 What is a Variable?

A **variable** is a named container that stores a value in your program's memory. Think of it like a labelled drawer in a dispensary cabinet. The label is the variable name; whatever is inside the drawer is the value. You can open the drawer, read what is inside, replace the contents, or use the contents in a calculation — all by referring to the label.

In Python, you create a variable and give it a value using the **assignment operator** `=`. The name goes on the left, the value goes on the right:

```python
# --- Pharmacy Example: storing drug information ---
# Context: recording the name and dose of a prescribed antibiotic

drug_name = "Amoxicillin"
dose_mg = 500
```

After these two lines run, Python has reserved two labelled spaces in memory:

- `drug_name` holds the text `"Amoxicillin"`
- `dose_mg` holds the number `500`

You can then use those names anywhere in your program:

```python
# --- Pharmacy Example: using stored variables ---
# Context: printing a prescription summary

drug_name = "Amoxicillin"
dose_mg = 500
frequency = "three times daily"
duration_days = 10

print(drug_name)
print(dose_mg)
print(f"Take {dose_mg} mg {frequency} for {duration_days} days.")
```

Output:

```
Amoxicillin
500
Take 500 mg three times daily for 10 days.
```

#### The assignment operator `=`

The `=` in Python does **not** mean "is equal to" — it means "store this value in this variable". Reading `dose_mg = 500` aloud as *"dose_mg gets 500"* or *"dose_mg is assigned 500"* is more accurate than reading it as *"dose_mg equals 500"*.

This distinction matters because you will later see `==` (two equals signs), which *does* mean "is equal to" and is used for comparisons. For now, remember: one `=` assigns, two `==` compares.

#### Variable naming rules

Python variable names must follow a few rules:

- They can contain letters, digits, and underscores (`_`)
- They **cannot** start with a digit (`2dose` is invalid; `dose2` is fine)
- They are **case-sensitive** (`dose_mg` and `Dose_mg` are two different variables)
- They cannot be Python reserved words like `if`, `for`, `while`, `True`, `False`

By convention, Python programmers use **snake_case** for variable names: all lowercase letters with underscores between words. This is the style used throughout this handbook.

```python
# Good variable names — clear and pharmacy-themed
drug_name = "Metformin"
patient_age = 62
dose_per_kg = 2.5
requires_refrigeration = False

# Avoid — unclear or not following convention
x = "Metformin"       # What is x?
DrugName = "Metformin" # PascalCase is for classes, not variables
dn = "Metformin"       # Too abbreviated
```

#### More pharmacy variable examples

```python
# --- Pharmacy Example: a complete prescription record as variables ---
# Context: storing all the key fields of a prescription

rx_number = "RX-20240115-001"
patient_name = "Sarah Johnson"
prescriber = "Dr. Emily Chen"
drug = "Amoxicillin"
dose_mg = 500
route = "oral"
frequency = "three times daily"
duration_days = 10
quantity = 30

print(f"Rx: {rx_number}")
print(f"Patient: {patient_name}")
print(f"Drug: {drug} {dose_mg} mg — {route} — {frequency} for {duration_days} days")
print(f"Qty: {quantity} capsules")
```

Output:

```
Rx: RX-20240115-001
Patient: Sarah Johnson
Drug: Amoxicillin 500 mg — oral — three times daily for 10 days
Qty: 30 capsules
```

---

### 2.2 The Four Primitive Data Types

Every value in Python has a **type** — a classification that tells Python what kind of data it is and what operations are valid on it. Python has four fundamental (primitive) data types that you will use constantly: `int`, `float`, `str`, and `bool`.

---

#### `int` — Integers

An **integer** is a whole number with no decimal point. It can be positive, negative, or zero.

```python
# --- Pharmacy Example: integer values ---
# Context: whole-number quantities in pharmacy practice

dose_mg = 500          # dose in milligrams
patient_age = 45       # patient age in years
quantity = 30          # number of tablets to dispense
refills_remaining = 2  # number of refills left on the prescription
days_supply = 90       # days of medication supply

print(dose_mg)         # 500
print(patient_age)     # 45
print(quantity)        # 30
```

Integers support all the arithmetic you would expect: addition, subtraction, multiplication, division, and more. You will explore these in Chapter 3.

---

#### `float` — Floating-Point Numbers

A **float** is a number that includes a decimal point. Use floats whenever precision beyond whole numbers is needed — body weight, concentration, dose per kilogram.

```python
# --- Pharmacy Example: float values ---
# Context: measurements that require decimal precision

weight_kg = 68.5          # patient weight in kilograms
dose_per_kg = 2.5         # dose in mg per kg of body weight
creatinine_clearance = 72.3  # mL/min — used for renal dose adjustment
bmi = 24.8                # body mass index

# Calculate weight-based dose
total_dose = weight_kg * dose_per_kg
print(f"Weight-based dose: {total_dose} mg")  # 171.25 mg
```

Output:

```
Weight-based dose: 171.25 mg
```

> **int vs. float:** Use `int` for things you count (tablets, days, refills) and `float` for things you measure (weight, concentration, volume). When in doubt, `float` is the safer choice for any numeric value that might ever need a decimal.

---

#### `str` — Strings

A **string** is a sequence of characters enclosed in single quotes `'...'` or double quotes `"..."`. Strings hold text: drug names, patient names, instructions, route of administration — anything that is not a number.

```python
# --- Pharmacy Example: string values ---
# Context: text data in a prescription

drug_name = "Metformin"
route = "oral"
frequency = "twice daily"
patient_name = "Sarah Johnson"
allergy_note = "NKDA"  # No Known Drug Allergies

print(drug_name)    # Metformin
print(route)        # oral
print(frequency)    # twice daily
```

Both single and double quotes work — choose one and be consistent. Double quotes are slightly more common in Python code and are used throughout this handbook.

```python
# Both of these are valid strings
drug_a = "Lisinopril"
drug_b = 'Atorvastatin'
```

> **Important:** `500` (no quotes) is an integer. `"500"` (with quotes) is a string. They look similar but behave very differently. You cannot do arithmetic on `"500"` without converting it first — more on this in Section 2.4.

---

#### `bool` — Booleans

A **boolean** holds one of exactly two values: `True` or `False`. Booleans are the result of yes/no questions and are used to control the flow of a program (covered in Chapter 7).

```python
# --- Pharmacy Example: boolean values ---
# Context: yes/no flags in a patient record

is_allergic = True           # patient has a known drug allergy
requires_refrigeration = False  # medication does not need cold storage
is_controlled_substance = True  # medication is a controlled drug
is_generic_available = False    # no generic equivalent on formulary
patient_consented = True        # patient has given informed consent

print(is_allergic)              # True
print(requires_refrigeration)   # False
```

Notice that `True` and `False` are capitalised — this is required in Python. `true` and `false` (lowercase) will cause a `NameError`.

```python
# This will cause a NameError — do NOT run as-is
flag = true   # NameError: name 'true' is not defined

# Correct
flag = True   # Capital T required
```

---

### 2.3 Dynamic Typing and the `type()` Function

Python is a **dynamically typed** language. This means you do not have to declare the type of a variable before using it — Python figures out the type automatically based on the value you assign. It also means a variable can be reassigned to a completely different type later in the program.

Compare this to some other languages (like Java or C++) where you must declare `int dose_mg = 500;` and the variable can only ever hold an integer. In Python, you simply write `dose_mg = 500` and Python handles the rest.

#### The `type()` function

The built-in `type()` function tells you the type of any value or variable:

```python
# --- Pharmacy Example: inspecting data types ---
# Context: checking the type of various pharmacy values

dose_mg = 500
weight_kg = 68.5
drug_name = "Metformin"
is_allergic = True

print(type(dose_mg))    # <class 'int'>
print(type(weight_kg))  # <class 'float'>
print(type(drug_name))  # <class 'str'>
print(type(is_allergic))  # <class 'bool'>
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

The output `<class 'int'>` is Python's way of saying "this value belongs to the `int` class". You will learn more about classes much later — for now, just read it as "this is an int".

#### Dynamic typing in action

Because Python is dynamically typed, you can reassign a variable to a different type. This is flexible but can also be a source of bugs if you are not careful:

```python
# --- Pharmacy Example: dynamic typing ---
# Context: a variable changing type during a program

# Start with a numeric dose
dose = 500
print(type(dose))   # <class 'int'>
print(dose)         # 500

# Reassign to a string (perhaps reading from user input)
dose = "500 mg"
print(type(dose))   # <class 'str'>
print(dose)         # 500 mg

# Reassign to a float for a calculation
dose = 500.0
print(type(dose))   # <class 'float'>
print(dose)         # 500.0
```

> **Practical advice:** While Python allows this, it is generally better practice to keep a variable holding the same type throughout its life. Changing types mid-program makes code harder to read and debug. If you need a different representation of the same data, use a new variable name — for example, `dose_mg = 500` and `dose_label = "500 mg"`.

#### Checking types in pharmacy code

The `type()` function is especially useful when debugging — for example, when you are not sure whether a value read from user input is a number or a string:

```python
# --- Pharmacy Example: debugging a type issue ---
# Context: investigating why a calculation is failing

user_input = "250"   # input() always returns a string
print(type(user_input))   # <class 'str'>

# This would fail — can't multiply a string by a number
# total = user_input * 3   # TypeError!

# Check the type first, then convert
print(f"Input type: {type(user_input)}")
numeric_dose = int(user_input)
print(f"After conversion: {type(numeric_dose)}")  # <class 'int'>
total_daily_dose = numeric_dose * 3
print(f"Total daily dose: {total_daily_dose} mg")  # 750 mg
```

---

### 2.4 Type Conversion

Sometimes you have a value of one type but need it in another type. Python provides built-in functions to convert between types:

| Function | Converts to | Example |
|---|---|---|
| `int()` | Integer | `int("500")` → `500` |
| `float()` | Float | `float("68.5")` → `68.5` |
| `str()` | String | `str(500)` → `"500"` |
| `bool()` | Boolean | `bool(0)` → `False` |

---

#### Converting strings to numbers

The most common conversion in pharmacy programs is turning a string (from user input or a file) into a number so you can do arithmetic:

```python
# --- Pharmacy Example: converting string input to a numeric dose ---
# Context: a pharmacist enters a dose as text; we need to calculate with it

dose_input = "500"       # this is a string — imagine it came from input()
dose_mg = int(dose_input)  # convert to integer

# Now we can do arithmetic
total_daily_dose = dose_mg * 3
print(f"Single dose: {dose_mg} mg")
print(f"Total daily dose: {total_daily_dose} mg")
```

Output:

```
Single dose: 500 mg
Total daily dose: 1500 mg
```

For decimal values, use `float()` instead:

```python
# --- Pharmacy Example: converting string to float for weight-based dosing ---
# Context: patient weight entered as text, needed for dose calculation

weight_input = "68.5"          # string from user input
weight_kg = float(weight_input)  # convert to float
dose_per_kg = 2.5

total_dose = weight_kg * dose_per_kg
print(f"Patient weight: {weight_kg} kg")
print(f"Dose per kg: {dose_per_kg} mg/kg")
print(f"Total dose: {total_dose} mg")
```

Output:

```
Patient weight: 68.5 kg
Dose per kg: 2.5 mg/kg
Total dose: 171.25 mg
```

---

#### Converting integers to floats

When mixing integers and floats in a calculation, Python automatically promotes the result to a float. But sometimes you want to be explicit:

```python
# --- Pharmacy Example: int to float for precise calculations ---
# Context: ensuring a dose calculation returns a float, not an integer

dose_mg = 500          # int
doses_per_day = 3      # int

# Integer division — result is a float in Python 3
dose_per_dose = dose_mg / doses_per_day
print(dose_per_dose)          # 166.66666666666666
print(type(dose_per_dose))    # <class 'float'>

# Explicit conversion
dose_float = float(dose_mg)
print(dose_float)             # 500.0
print(type(dose_float))       # <class 'float'>
```

---

#### Converting numbers to strings

You need to convert numbers to strings when building text output or combining numbers with text using concatenation (the `+` operator on strings):

```python
# --- Pharmacy Example: converting numbers to strings for display ---
# Context: building a label string by combining text and numbers

drug_name = "Metformin"
dose_mg = 500
quantity = 60

# Using str() to combine number with text via concatenation
label = drug_name + " " + str(dose_mg) + " mg — Qty: " + str(quantity)
print(label)
```

Output:

```
Metformin 500 mg — Qty: 60
```

> **Tip:** f-strings (introduced in Section 1.3) handle this conversion automatically and are usually cleaner than manual `str()` calls. The above example is equivalent to `f"{drug_name} {dose_mg} mg — Qty: {quantity}"`. Both approaches are valid.

---

#### What happens when conversion fails

Not every conversion is possible. If you try to convert a value that cannot be interpreted as the target type, Python raises a `ValueError`:

```python
# --- Pharmacy Example: failed type conversion ---
# Context: a user enters an invalid dose value

# This will cause a ValueError — do NOT run as-is
bad_input = "five hundred"
dose = int(bad_input)   # ValueError: invalid literal for int() with base 10: 'five hundred'
```

```python
# Another example — a dose with units attached
dose_with_units = "500mg"
dose = int(dose_with_units)  # ValueError: invalid literal for int() with base 10: '500mg'
```

You will learn how to handle these errors gracefully using `try`/`except` in Chapter 11. For now, the key lesson is: `int()` and `float()` only work on strings that contain a valid number — no letters, no units, no spaces.

```python
# These conversions work
int("500")       # 500
float("68.5")    # 68.5
int("  42  ")    # 42  — leading/trailing spaces are stripped automatically

# These conversions fail with ValueError
int("500mg")     # invalid — contains letters
float("68,5")    # invalid — comma instead of decimal point
int("five")      # invalid — spelled out
```

---

### Introducing the Patient Record Data Model

Throughout this handbook, you will work with a consistent set of data structures that represent real pharmacy objects. This makes it easier to follow examples across chapters — you will recognise the same patient, the same medications, and the same structure each time.

The first and most important of these is the **Patient Record**. Here it is in full:

```python
# --- Recurring Data Model: Patient Record ---
# Context: a dictionary representing a complete patient profile
# This structure will be used throughout the handbook

patient = {
    "name": "Sarah Johnson",
    "age": 45,
    "weight_kg": 68.0,
    "medications": ["Metformin", "Lisinopril", "Atorvastatin"],
    "allergies": ["Penicillin"]
}
```

You do not need to understand everything about this structure yet — dictionaries and lists are covered in Chapters 5 and 6. For now, notice the data types at work:

- `"name"` holds a **string** (`"Sarah Johnson"`)
- `"age"` holds an **integer** (`45`)
- `"weight_kg"` holds a **float** (`68.0`)
- `"medications"` holds a **list** of strings (a collection of drug names)
- `"allergies"` holds a **list** of strings (a collection of allergen names)

This patient — Sarah Johnson — will appear in examples throughout the handbook. As you learn new concepts, you will add to her record, query it, update it, and eventually read it from and write it to a file.

---

### Chapter Summary

- A **variable** is a named container for storing a value. Create one with `variable_name = value`.
- The `=` operator **assigns** a value to a variable. It does not mean "is equal to" — that is `==`.
- Python has four primitive data types:
  - `int` — whole numbers (e.g., `dose_mg = 500`, `patient_age = 45`)
  - `float` — decimal numbers (e.g., `weight_kg = 68.5`, `dose_per_kg = 2.5`)
  - `str` — text enclosed in quotes (e.g., `drug_name = "Metformin"`, `route = "oral"`)
  - `bool` — `True` or `False` (e.g., `is_allergic = True`, `requires_refrigeration = False`)
- Python is **dynamically typed**: you do not declare types, and variables can be reassigned to different types.
- The `type()` function returns the type of any value: `type(500)` → `<class 'int'>`.
- Type conversion functions: `int()`, `float()`, `str()` convert values between types.
- If a conversion is impossible (e.g., `int("five hundred")`), Python raises a `ValueError`.
- The **Patient Record** data model (`patient = {...}`) is introduced here and will be reused throughout the handbook.

---

---

## Chapter 3: Operators and Expressions

In the previous chapter you learned how to store values in variables. Now you will learn how to *do things* with those values — calculate doses, compare numbers, and combine conditions. This is where Python starts to feel like a real tool for pharmacy practice.

An **expression** is any combination of values, variables, and operators that Python can evaluate to produce a result. `500 + 250` is an expression. `dose > max_safe_dose` is an expression. `is_adult and not is_pregnant` is an expression.

An **operator** is a symbol that tells Python what operation to perform. Python has several categories of operators. This chapter covers the three most important ones for pharmacy work: arithmetic, comparison, and logical.

---

### Learning Objectives

By the end of this chapter you will be able to:

- Use all seven arithmetic operators to perform dose calculations and tablet counts
- Use all six comparison operators to check whether a value meets a threshold or condition
- Use the three logical operators (`and`, `or`, `not`) to combine multiple conditions
- Explain operator precedence and use parentheses to control the order of evaluation
- Write a multi-step dosage calculation expression that mirrors real pharmacy practice

---

### Section 3.1: Arithmetic Operators

Python supports seven arithmetic operators. You will use these constantly in pharmacy calculations — computing total doses, dividing by body weight, working out how many tablets to dispense, and more.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `500 + 250` | `750` |
| `-` | Subtraction | `1000 - 400` | `600` |
| `*` | Multiplication | `500 * 3` | `1500` |
| `/` | Division (float) | `1500 / 3` | `500.0` |
| `//` | Floor division | `29 // 7` | `4` |
| `%` | Modulo (remainder) | `29 % 7` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

Let's walk through each one with a pharmacy example.

---

#### `+` Addition — Calculating Total Daily Dose

When a patient takes a drug in split doses throughout the day, you add them together to find the total daily dose.

```python
# --- Pharmacy Example: Total daily dose from split doses ---
# Context: a patient takes Metformin 500 mg in the morning and 1000 mg in the evening

morning_dose = 500    # mg
evening_dose = 1000   # mg

total_daily_dose = morning_dose + evening_dose
print(total_daily_dose)   # 1500
```

---

#### `-` Subtraction — Tracking Remaining Tablets

After a patient collects a partial supply, you subtract what they have taken to find what remains.

```python
# --- Pharmacy Example: Remaining tablets in a blister pack ---
# Context: a pack of 28 tablets; patient has taken 10

dispensed = 28
taken = 10

remaining_tablets = dispensed - taken
print(remaining_tablets)   # 18
```

---

#### `*` Multiplication — Total Dose from Dose Strength and Frequency

Multiply the dose per administration by the number of doses per day to get the total daily dose.

```python
# --- Pharmacy Example: Total daily dose from dose strength and frequency ---
# Context: Amoxicillin 500 mg taken three times daily

dose_mg = 500          # mg per dose
doses_per_day = 3

total_daily_dose = dose_mg * doses_per_day
print(total_daily_dose)   # 1500
```

---

#### `/` Division — Weight-Based Dosing

Many drugs are dosed by body weight (mg/kg). Divide the total dose by the patient's weight to find the dose per kilogram — or divide the total dose by the dose per kg to find the correct total for a given patient.

```python
# --- Pharmacy Example: Weight-based dose calculation ---
# Context: a patient weighing 68 kg is prescribed a total dose of 340 mg
# We want to verify the dose per kg

total_dose = 340.0    # mg
weight_kg = 68.0      # kg

dose_per_kg = total_dose / weight_kg
print(dose_per_kg)    # 5.0

# Note: / always returns a float, even when the result is a whole number
print(type(dose_per_kg))   # <class 'float'>
```

> **Important:** The `/` operator always returns a `float` in Python 3. Even `10 / 2` gives `5.0`, not `5`. This matters when you need an integer result — use `//` instead (see below).

---

#### `//` Floor Division — Counting Complete Weeks of Supply

Floor division divides and then rounds *down* to the nearest whole number. This is useful when you need to count complete units — full weeks in a supply, full tablets in a dose, and so on.

```python
# --- Pharmacy Example: Complete weeks in a days supply ---
# Context: a prescription is written for a 29-day supply; how many full weeks is that?

days_supply = 29

full_weeks = days_supply // 7
print(full_weeks)   # 4  (4 complete weeks, with 1 day left over)
```

---

#### `%` Modulo — Finding the Leftover Days

The modulo operator returns the *remainder* after division. Paired with `//`, it tells you what is left over after counting complete units.

```python
# --- Pharmacy Example: Leftover days after counting full weeks ---
# Context: continuing the 29-day supply example above

days_supply = 29

extra_days = days_supply % 7
print(extra_days)   # 1  (1 day left over after 4 full weeks)

# Together, // and % give you the full picture:
print(f"{full_weeks} full weeks and {extra_days} extra day(s)")
# 4 full weeks and 1 extra day(s)
```

---

#### `**` Exponentiation — Pharmacokinetic Decay

The `**` operator raises a number to a power. In pharmacokinetics, drug concentration in the body often follows an exponential decay — the concentration at time *t* is the initial concentration multiplied by a decay factor raised to the power of *t*.

```python
# --- Pharmacy Example: First-order drug concentration decay ---
# Context: a drug has an initial plasma concentration of 100 mg/L
# and a half-life of 6 hours. After each half-life, concentration halves.
# Concentration at time t (in half-lives) = C0 * (0.5 ** t)

initial_concentration = 100.0   # mg/L
half_life_hours = 6

# Concentration after 3 half-lives (18 hours)
t = 3
concentration_at_t = initial_concentration * (0.5 ** t)
print(concentration_at_t)   # 12.5 mg/L

# Concentration after 4 half-lives (24 hours)
t = 4
concentration_at_t = initial_concentration * (0.5 ** t)
print(concentration_at_t)   # 6.25 mg/L
```

> **Pharmacy note:** This is a simplified model. Real pharmacokinetic calculations also account for volume of distribution, clearance, and route of administration. But the mathematical pattern — exponential decay — is exactly what `**` models.

---

### Section 3.2: Comparison Operators

Comparison operators compare two values and return a **boolean** result: either `True` or `False`. You will use these constantly to check whether a dose is within range, whether a patient meets eligibility criteria, and whether a drug is on the formulary.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `dose == 500` | `True` or `False` |
| `!=` | Not equal to | `drug != "Penicillin"` | `True` or `False` |
| `<` | Less than | `dose < min_dose` | `True` or `False` |
| `>` | Greater than | `dose > max_dose` | `True` or `False` |
| `<=` | Less than or equal to | `age <= 18` | `True` or `False` |
| `>=` | Greater than or equal to | `crcl >= 60` | `True` or `False` |

---

#### `==` Equals — Checking Against a Standard Dose

```python
# --- Pharmacy Example: Verify prescribed dose matches standard dose ---
# Context: the standard dose for Amoxicillin is 500 mg; check if the prescription matches

prescribed_dose = 500
standard_dose = 500

dose_is_standard = prescribed_dose == standard_dose
print(dose_is_standard)   # True

# A different prescription
prescribed_dose_2 = 750
print(prescribed_dose_2 == standard_dose)   # False
```

> **Common mistake:** Do not confuse `=` (assignment) with `==` (comparison). Writing `dose = 500` stores the value. Writing `dose == 500` checks whether the value is 500.

---

#### `!=` Not Equals — Checking Formulary Status

```python
# --- Pharmacy Example: Check if a drug is not on the formulary ---
# Context: the formulary drug for this indication is Metformin

prescribed_drug = "Glipizide"
formulary_drug = "Metformin"

is_non_formulary = prescribed_drug != formulary_drug
print(is_non_formulary)   # True  — Glipizide is not the formulary choice
```

---

#### `<` Less Than — Sub-Therapeutic Dose Check

```python
# --- Pharmacy Example: Check if dose is below the minimum therapeutic dose ---
# Context: minimum therapeutic dose for this antibiotic is 250 mg

prescribed_dose = 125
min_therapeutic_dose = 250

is_sub_therapeutic = prescribed_dose < min_therapeutic_dose
print(is_sub_therapeutic)   # True  — dose is too low
```

---

#### `>` Greater Than — Toxic Dose Alert

```python
# --- Pharmacy Example: Check if dose exceeds the maximum safe dose ---
# Context: maximum safe daily dose of Paracetamol (Acetaminophen) is 4000 mg

prescribed_daily_dose = 5000
max_safe_dose = 4000

is_toxic = prescribed_daily_dose > max_safe_dose
print(is_toxic)   # True  — dose exceeds safe limit, alert required
```

---

#### `<=` Less Than or Equal To — Pediatric Patient Check

```python
# --- Pharmacy Example: Identify pediatric patients for dose adjustment ---
# Context: patients aged 18 or under require pediatric dosing protocols

patient_age = 16

is_pediatric = patient_age <= 18
print(is_pediatric)   # True  — patient is 16, pediatric dosing applies

patient_age_2 = 18
print(patient_age_2 <= 18)   # True  — 18 is included (≤, not <)

patient_age_3 = 19
print(patient_age_3 <= 18)   # False — adult dosing applies
```

---

#### `>=` Greater Than or Equal To — Renal Function Check

Creatinine clearance (CrCl) is used to assess kidney function. Many drugs require dose adjustment when CrCl falls below a threshold.

```python
# --- Pharmacy Example: Check if renal function is adequate for standard dosing ---
# Context: standard dosing of this drug requires CrCl >= 60 mL/min

creatinine_clearance = 72.0   # mL/min

adequate_renal_function = creatinine_clearance >= 60
print(adequate_renal_function)   # True  — no dose adjustment needed

creatinine_clearance_2 = 45.0
print(creatinine_clearance_2 >= 60)   # False — dose adjustment required
```

---

### Section 3.3: Logical Operators

Logical operators combine multiple boolean expressions into a single `True` or `False` result. In pharmacy, you often need to check several conditions at once — a patient must meet *all* criteria, or *at least one* condition must be true, or a condition must *not* be true.

| Operator | Meaning | Result is `True` when... |
|---|---|---|
| `and` | Both conditions must be true | Both left AND right are `True` |
| `or` | At least one condition must be true | Left OR right (or both) are `True` |
| `not` | Reverses the boolean value | The operand is `False` |

---

#### `and` — Adult Dosing Eligibility

Use `and` when a patient must meet *all* criteria simultaneously.

```python
# --- Pharmacy Example: Check eligibility for adult dosing protocol ---
# Context: adult dosing requires patient age >= 18 AND weight >= 50 kg

patient_age = 22
weight_kg = 55.0

is_eligible_adult_dosing = patient_age >= 18 and weight_kg >= 50
print(is_eligible_adult_dosing)   # True  — both conditions met

# A patient who is old enough but underweight
patient_age_2 = 20
weight_kg_2 = 45.0
print(patient_age_2 >= 18 and weight_kg_2 >= 50)   # False — weight condition fails
```

---

#### `or` — Allergy Screening

Use `or` when *any one* of several conditions being true is enough to trigger an action.

```python
# --- Pharmacy Example: Cross-allergy screening for beta-lactam antibiotics ---
# Context: patients allergic to Penicillin OR Cephalosporin need an alternative antibiotic

is_allergic_penicillin = True
is_allergic_cephalosporin = False

needs_alternative = is_allergic_penicillin or is_allergic_cephalosporin
print(needs_alternative)   # True  — Penicillin allergy alone is sufficient

# A patient with no beta-lactam allergies
is_allergic_penicillin_2 = False
is_allergic_cephalosporin_2 = False
print(is_allergic_penicillin_2 or is_allergic_cephalosporin_2)   # False
```

---

#### `not` — Contraindication Check

Use `not` to reverse a boolean value. This is useful when your variable stores a positive condition but you need to check the negative.

```python
# --- Pharmacy Example: Check that a drug is not contraindicated in pregnancy ---
# Context: this drug is contraindicated during pregnancy; only prescribe if patient is NOT pregnant

is_pregnant = False

safe_to_prescribe = not is_pregnant
print(safe_to_prescribe)   # True  — patient is not pregnant, drug can be prescribed

is_pregnant_2 = True
print(not is_pregnant_2)   # False — drug is contraindicated, do not prescribe
```

---

#### Combining Logical Operators

You can chain `and`, `or`, and `not` together to express complex clinical rules.

```python
# --- Pharmacy Example: Full eligibility check for a drug ---
# Context: prescribe this drug only if:
#   - patient is an adult (age >= 18)
#   - patient is not pregnant
#   - patient has adequate renal function (CrCl >= 60) OR is on a reduced dose protocol

patient_age = 35
is_pregnant = False
creatinine_clearance = 55.0
on_reduced_dose_protocol = True

eligible = (
    patient_age >= 18
    and not is_pregnant
    and (creatinine_clearance >= 60 or on_reduced_dose_protocol)
)
print(eligible)   # True
```

---

### Section 3.4: Operator Precedence

When an expression contains multiple operators, Python follows a specific order of evaluation — just like the PEMDAS/BODMAS rule you may remember from school mathematics.

**PEMDAS / BODMAS order in Python:**

| Priority | Category | Operators |
|---|---|---|
| 1 (highest) | Parentheses | `( )` |
| 2 | Exponentiation | `**` |
| 3 | Unary operators | `-x`, `+x`, `not x` |
| 4 | Multiplication / Division | `*`, `/`, `//`, `%` |
| 5 | Addition / Subtraction | `+`, `-` |
| 6 | Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| 7 | Logical NOT | `not` |
| 8 | Logical AND | `and` |
| 9 (lowest) | Logical OR | `or` |

Higher priority operators are evaluated first. When operators have the same priority, Python evaluates left to right.

---

#### Multi-Step Dosage Calculation — Precedence in Action

Consider this real-world scenario: you need to calculate the number of tablets to dispense for a course of treatment, then check whether the total dose is within a safe limit.

```python
# --- Pharmacy Example: Multi-step dosage calculation with precedence ---
# Context: Amoxicillin 500 mg capsules, 3 times daily for 7 days
# Step 1: total daily dose = dose_mg * doses_per_day
# Step 2: total course dose = total_daily_dose * days
# Step 3: number of tablets = total course dose / dose_mg  (should equal doses_per_day * days)

dose_mg = 500
doses_per_day = 3
days = 7
max_safe_daily_dose = 3000

# Without parentheses — let's trace the precedence:
# Python evaluates * before + and before ==
total_course_dose = dose_mg * doses_per_day * days
print(total_course_dose)   # 10500 mg over the full course

# Check if daily dose is within safe limits
# dose_mg * doses_per_day is evaluated first (multiplication before comparison)
daily_dose_safe = dose_mg * doses_per_day <= max_safe_daily_dose
print(daily_dose_safe)   # True  (1500 <= 3000)
```

---

#### Parentheses Override Precedence

Parentheses always take the highest priority. Use them to make your intent explicit and to override the default order.

```python
# --- Pharmacy Example: Parentheses controlling calculation order ---
# Context: calculating adjusted dose using a loading dose formula
# Adjusted dose = (loading_dose + maintenance_dose) / 2

loading_dose = 1000    # mg
maintenance_dose = 500  # mg

# WITHOUT parentheses — wrong result
# Python evaluates / before +, so this computes: 1000 + (500 / 2) = 1250
wrong_result = loading_dose + maintenance_dose / 2
print(wrong_result)   # 1250.0  — NOT what we intended

# WITH parentheses — correct result
# Python evaluates the parenthesised expression first: (1000 + 500) / 2 = 750
correct_result = (loading_dose + maintenance_dose) / 2
print(correct_result)   # 750.0  — correct average dose

# Practical rule: when in doubt, add parentheses.
# They make your code clearer AND ensure the right calculation order.
```

> **Best practice:** In pharmacy calculations, always use parentheses to make the order of operations explicit. A misplaced operator precedence in a dose calculation could produce a clinically significant error. Parentheses cost nothing and prevent mistakes.

---

### Chapter Summary

- **Arithmetic operators** perform mathematical calculations: `+` (add), `-` (subtract), `*` (multiply), `/` (divide, returns float), `//` (floor divide, returns int), `%` (remainder), `**` (power).
- `/` always returns a `float`; use `//` when you need a whole-number result.
- `//` and `%` work together: `days // 7` gives full weeks, `days % 7` gives leftover days.
- `**` models exponential relationships such as pharmacokinetic decay.
- **Comparison operators** return `True` or `False`: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Do not confuse `=` (assignment) with `==` (comparison).
- **Logical operators** combine boolean expressions: `and` (both true), `or` (at least one true), `not` (reverse).
- **Operator precedence** follows PEMDAS/BODMAS: parentheses first, then exponentiation, then multiplication/division, then addition/subtraction, then comparisons, then logical operators.
- Use **parentheses** to make calculation order explicit — especially important in clinical dose calculations.

---

### Quiz

**Question 1**
A patient is prescribed Metformin 500 mg twice daily and 1000 mg at bedtime. Which Python expression correctly calculates the total daily dose?

A) `500 * 2 + 1000`
B) `500 + 2 + 1000`
C) `500 * 1000 + 2`
D) `(500 + 1000) * 2`

---

**Question 2**
A 28-day blister pack of Atorvastatin has been partially used. The patient has taken 11 tablets. Write a Python expression to calculate the number of remaining tablets.

A) `28 * 11`
B) `28 + 11`
C) `28 - 11`
D) `28 / 11`

---

**Question 3**
A prescription is written for a 30-day supply of a medication taken once daily. You want to know how many complete weeks that is, and how many days are left over. Which pair of expressions gives you both values?

A) `30 / 7` and `30 * 7`
B) `30 // 7` and `30 % 7`
C) `30 % 7` and `30 // 7` (same as B, just reversed labels)
D) `30 ** 7` and `30 - 7`

---

**Question 4**
The maximum safe daily dose of Paracetamol is 4000 mg. A patient has been prescribed 4500 mg/day. Which expression evaluates to `True` to flag this as an overdose?

A) `4500 == 4000`
B) `4500 < 4000`
C) `4500 > 4000`
D) `4500 != 4500`

---

**Question 5**
A drug can only be prescribed if the patient is aged 18 or over AND has a creatinine clearance of at least 30 mL/min. A patient is 22 years old with a CrCl of 25 mL/min. What does the following expression return?

```python
patient_age = 22
crcl = 25
patient_age >= 18 and crcl >= 30
```

A) `True`
B) `False`
C) `22`
D) `25`

---

**Question 6**
A pharmacist needs to check whether a patient is allergic to either Penicillin or Sulfonamides before dispensing a drug. The patient has a Sulfonamide allergy but not a Penicillin allergy. What does this expression return?

```python
is_allergic_penicillin = False
is_allergic_sulfonamide = True
is_allergic_penicillin or is_allergic_sulfonamide
```

A) `False`
B) `True`
C) `None`
D) `0`

---

**Question 7**
What is the result of the following expression, and why?

```python
loading_dose = 800
maintenance_dose = 400
loading_dose + maintenance_dose / 2
```

A) `600.0` — because `(800 + 400) / 2 = 600`
B) `1000.0` — because `800 + (400 / 2) = 1000`
C) `800` — because division is ignored
D) `400.0` — because only the division is evaluated

---

#### Answer Key

**Q1 — Answer: A** `500 * 2 + 1000`
Multiplication is evaluated before addition (PEMDAS). `500 * 2 = 1000`, then `1000 + 1000 = 2000`. This correctly gives the total daily dose of 2000 mg.

**Q2 — Answer: C** `28 - 11`
Subtraction gives the remaining count: `28 - 11 = 17` tablets remaining.

**Q3 — Answer: B** `30 // 7` gives `4` (complete weeks); `30 % 7` gives `2` (leftover days).
Floor division discards the remainder; modulo returns only the remainder.

**Q4 — Answer: C** `4500 > 4000` evaluates to `True`.
The prescribed dose (4500 mg) is greater than the maximum safe dose (4000 mg), so the comparison returns `True`, correctly flagging the overdose.

**Q5 — Answer: B** `False`
Both conditions must be true for `and` to return `True`. The age condition (`22 >= 18`) is `True`, but the CrCl condition (`25 >= 30`) is `False`. `True and False` evaluates to `False`.

**Q6 — Answer: B** `True`
`or` returns `True` if at least one operand is `True`. The Sulfonamide allergy is `True`, so the whole expression is `True` — the patient needs an alternative drug.

**Q7 — Answer: B** `1000.0`
Division has higher precedence than addition. Python evaluates `400 / 2 = 200.0` first, then `800 + 200.0 = 1000.0`. To get the average of the two doses, you would need parentheses: `(loading_dose + maintenance_dose) / 2 = 600.0`.

---

### Challenge

#### Problem: Dosage Calculator

Write a Python program that performs the following steps:

1. Store a prescribed total daily dose (e.g., 1500 mg/day)
2. Store the dose strength per tablet (e.g., 500 mg per tablet)
3. Calculate the number of tablets needed per day
4. Calculate the total number of tablets needed for a 10-day course
5. Check whether the total daily dose exceeds a maximum safe daily dose (e.g., 3000 mg/day)
6. Print all results clearly

#### Expected Output

```
Tablets per day: 3
Tablets for 10-day course: 30
Daily dose (1500 mg) exceeds max safe dose (3000 mg): False
```

#### Reference Solution

```python
# --- Challenge: Dosage Calculator ---
# Context: calculate tablet counts and safety check for a prescribed course

# Step 1 & 2: Store the prescribed values
total_daily_dose_mg = 1500    # mg/day (prescribed)
dose_per_tablet_mg = 500      # mg per tablet
course_days = 10
max_safe_daily_dose_mg = 3000  # mg/day (safety threshold)

# Step 3: Tablets per day
# Use // (floor division) because you can't dispense a fraction of a tablet
tablets_per_day = total_daily_dose_mg // dose_per_tablet_mg
print(f"Tablets per day: {tablets_per_day}")

# Step 4: Total tablets for the full course
total_tablets = tablets_per_day * course_days
print(f"Tablets for {course_days}-day course: {total_tablets}")

# Step 5: Safety check — does the daily dose exceed the maximum?
exceeds_max = total_daily_dose_mg > max_safe_daily_dose_mg
print(
    f"Daily dose ({total_daily_dose_mg} mg) exceeds "
    f"max safe dose ({max_safe_daily_dose_mg} mg): {exceeds_max}"
)
```

**Try it yourself:** Change `total_daily_dose_mg` to `3500` and observe how the safety check output changes. Then try a dose that doesn't divide evenly into the tablet strength (e.g., `total_daily_dose_mg = 1250`, `dose_per_tablet_mg = 500`) and see what `//` does with the remainder.

---

## Chapter 4: Strings and String Manipulation

### Learning Objectives

By the end of this chapter you will be able to:

- Create strings using single quotes, double quotes, and triple quotes
- Access individual characters and slices of a string using indexing
- Apply common string methods to clean, transform, and search text
- Build formatted prescription label strings using f-strings and `.format()`

---

### Section 4.1: Creating Strings

A **string** is a sequence of characters — letters, digits, spaces, punctuation — enclosed in quotes. In pharmacy, strings appear everywhere: drug names, patient names, dosing instructions, prescription numbers, and file names.

#### Single vs Double Quotes

Python accepts both single quotes (`'`) and double quotes (`"`) to define a string. They are interchangeable, but you must open and close with the same type.

```python
# --- Pharmacy Example: drug name strings ---
# Context: storing a drug name using both quote styles

drug_name_single = 'Amoxicillin'
drug_name_double = "Amoxicillin"

print(drug_name_single)   # Amoxicillin
print(drug_name_double)   # Amoxicillin
print(drug_name_single == drug_name_double)  # True — identical strings
```

Use double quotes when the string itself contains an apostrophe, and single quotes when it contains a double-quote character:

```python
# --- Pharmacy Example: quotes inside strings ---
instruction_single = "Patient's medication must be refrigerated."
instruction_double = 'Dispense with "Medication Guide" attached.'

print(instruction_single)
print(instruction_double)
```

#### Multi-line Strings with Triple Quotes

Triple quotes (`"""` or `'''`) let you write a string that spans multiple lines. This is perfect for drug labels or dosing instructions that naturally occupy several lines.

```python
# --- Pharmacy Example: multi-line drug label ---
# Context: storing a complete drug label as a single string

drug_label = """
AMOXICILLIN CAPSULES 500 mg
Rx Only

Dosage: Take 1 capsule by mouth three times daily.
Duration: 10 days
Storage: Store below 25°C. Keep out of reach of children.
Manufacturer: PharmaCo Ltd.
"""

print(drug_label)
```

The string preserves every newline and space exactly as written — useful when you need to print a label that looks like the real thing.

#### Escape Characters

Sometimes you need to include special characters inside a string. Python uses a backslash (`\`) as an **escape character** to signal that the next character has a special meaning.

| Escape | Meaning | Pharmacy use |
|--------|---------|--------------|
| `\n`   | Newline | Separate lines on a printed label |
| `\t`   | Tab     | Indent columns in a dispensing report |
| `\\`   | Literal backslash | File paths on Windows |
| `\'`   | Literal single quote | Inside a single-quoted string |
| `\"`   | Literal double quote | Inside a double-quoted string |

```python
# --- Pharmacy Example: escape characters in a label ---
# Context: building a compact label string with newlines and tabs

label = "METFORMIN 500 mg\nTake 1 tablet twice daily with meals.\n\tRefrigerate after opening."
print(label)
# Output:
# METFORMIN 500 mg
# Take 1 tablet twice daily with meals.
#     Refrigerate after opening.

# Tab-separated dispensing report row
report_row = "Sarah Johnson\t500 mg\tTwice daily\t10 days"
print(report_row)
# Sarah Johnson   500 mg  Twice daily     10 days
```

---

### Section 4.2: String Indexing and Slicing

A string is an ordered sequence of characters. Python assigns each character a **position number** called an **index**, starting at **0** for the first character. This is called **zero-based indexing**.

```
drug_code = "AMX-500"
Index:       0 1 2 3 4 5 6
```

#### Accessing Individual Characters

Use square brackets `[]` with an index to retrieve a single character:

```python
# --- Pharmacy Example: indexing a drug code ---
# Context: extracting characters from a standardised drug code

drug_code = "AMX-500"

print(drug_code[0])   # "A"  — first character (drug family prefix)
print(drug_code[1])   # "M"
print(drug_code[2])   # "X"
print(drug_code[3])   # "-"  — separator
print(drug_code[4])   # "5"  — start of dose number
```

#### Negative Indexing

Python also supports **negative indices**, which count backwards from the end of the string. `-1` is the last character, `-2` is the second-to-last, and so on.

```python
# --- Pharmacy Example: negative indexing ---
drug_code = "AMX-500"

print(drug_code[-1])   # "0"  — last character
print(drug_code[-3])   # "5"  — third from the end
print(drug_code[-4])   # "-"  — the separator
```

Negative indexing is handy when you want the last few characters of a string without knowing its exact length.

#### Slicing

**Slicing** extracts a portion of a string using the syntax `string[start:stop]`. The slice includes the character at `start` and goes up to — but **not including** — the character at `stop`.

```python
# --- Pharmacy Example: slicing a drug code ---
# Context: extracting the drug prefix and dose number from a code

drug_code = "AMX-500"

drug_prefix = drug_code[0:3]   # "AMX"  — characters at index 0, 1, 2
dose_part   = drug_code[4:7]   # "500"  — characters at index 4, 5, 6

print(drug_prefix)   # AMX
print(dose_part)     # 500
```

You can omit `start` (defaults to 0) or `stop` (defaults to end of string):

```python
drug_code = "AMX-500"

print(drug_code[:3])    # "AMX"  — from beginning to index 2
print(drug_code[4:])    # "500"  — from index 4 to end
print(drug_code[:])     # "AMX-500"  — full copy of the string
```

A third value, the **step**, controls how many characters to skip:

```python
# Every other character
print(drug_code[::2])   # "A-0"
```

---

### Section 4.3: Common String Methods

Python strings come with a rich set of built-in **methods** — functions that belong to the string and are called with dot notation: `string.method()`. None of these methods modify the original string; they always return a new one.

#### `upper()` — Convert to Uppercase

Used to standardise drug names on printed labels, where convention requires uppercase.

```python
# --- Pharmacy Example: upper() for drug labels ---
drug_name = "amoxicillin"
label_name = drug_name.upper()
print(label_name)   # AMOXICILLIN
```

#### `lower()` — Convert to Lowercase

Used to normalise user input before comparison, so "METFORMIN", "Metformin", and "metformin" all match.

```python
# --- Pharmacy Example: lower() for input normalisation ---
user_input = "METFORMIN"
normalised = user_input.lower()
print(normalised)   # metformin

# Safe comparison regardless of how the user typed it
if user_input.lower() == "metformin":
    print("Metformin found in database.")
```

#### `strip()` — Remove Leading and Trailing Whitespace

When reading drug names from a form or file, extra spaces often sneak in. `strip()` removes them.

```python
# --- Pharmacy Example: strip() for cleaning user input ---
raw_input = "   Lisinopril   "
clean_input = raw_input.strip()
print(f"'{raw_input}'")    # '   Lisinopril   '
print(f"'{clean_input}'")  # 'Lisinopril'
```

`lstrip()` removes only leading whitespace; `rstrip()` removes only trailing whitespace.

#### `replace()` — Replace a Substring

Useful for expanding abbreviations in dosing instructions before printing a label.

```python
# --- Pharmacy Example: replace() for expanding abbreviations ---
instruction = "Take 1 tab PO TID for 10 days."
expanded = instruction.replace("tab", "tablet").replace("PO", "by mouth").replace("TID", "three times daily")
print(expanded)
# Take 1 tablet by mouth three times daily for 10 days.
```

#### `split()` — Split a String into a List

Splits a string at every occurrence of a separator and returns a list of substrings. Ideal for parsing CSV-like medication data.

```python
# --- Pharmacy Example: split() for parsing a medication string ---
med_string = "Metformin,Lisinopril,Atorvastatin,Aspirin"
medications = med_string.split(",")
print(medications)
# ['Metformin', 'Lisinopril', 'Atorvastatin', 'Aspirin']

# Iterate over the parsed list
for med in medications:
    print(f"  - {med}")
```

Calling `split()` with no argument splits on any whitespace (spaces, tabs, newlines):

```python
instruction = "Take  1  tablet  daily"
words = instruction.split()
print(words)   # ['Take', '1', 'tablet', 'daily']
```

#### `join()` — Join a List into a String

The inverse of `split()`. Joins a list of strings into one string, inserting a separator between each item.

```python
# --- Pharmacy Example: join() for building a medication summary ---
medications = ["Metformin", "Lisinopril", "Atorvastatin"]

# Comma-separated for a label
summary = ", ".join(medications)
print(summary)   # Metformin, Lisinopril, Atorvastatin

# Bullet-point list for a report
bullet_list = "\n  - ".join(medications)
print("Current medications:\n  - " + bullet_list)
# Current medications:
#   - Metformin
#   - Lisinopril
#   - Atorvastatin
```

#### `find()` — Find the Position of a Substring

Returns the index of the **first** occurrence of a substring, or `-1` if not found. Useful for locating a keyword in a drug label.

```python
# --- Pharmacy Example: find() in a drug label ---
label = "AMOXICILLIN CAPSULES 500 mg — Store below 25°C"

pos = label.find("500")
print(pos)   # 21  — index where "500" starts

pos_missing = label.find("Penicillin")
print(pos_missing)   # -1  — not found

# Practical use: check if a storage instruction is present
if label.find("Store") != -1:
    print("Storage instruction found.")
```

#### `startswith()` — Check if a String Starts with a Prefix

Returns `True` if the string begins with the given prefix. Useful for validating drug code formats.

```python
# --- Pharmacy Example: startswith() for drug code validation ---
drug_code = "AMX-500"

if drug_code.startswith("AMX"):
    print("Amoxicillin family drug detected.")

# Check multiple prefixes using a tuple
antibiotic_prefixes = ("AMX", "PEN", "ERY", "AZI")
if drug_code.startswith(antibiotic_prefixes):
    print("Antibiotic detected — check allergy record.")
```

#### `endswith()` — Check if a String Ends with a Suffix

Returns `True` if the string ends with the given suffix. Commonly used to validate file extensions before processing.

```python
# --- Pharmacy Example: endswith() for file validation ---
filename = "patient_records_2024.csv"

if filename.endswith(".csv"):
    print(f"'{filename}' is a valid CSV file — safe to import.")
else:
    print("Unexpected file format. Please provide a .csv file.")

# Also works with a tuple of suffixes
report_file = "dose_report.pdf"
if report_file.endswith((".pdf", ".txt", ".csv")):
    print("Recognised report format.")
```

---

### Section 4.4: f-strings and `.format()`

Hard-coding values directly into strings is fine for simple output, but real pharmacy applications need to insert variable values — patient names, drug names, doses — into a template. Python provides two clean ways to do this.

#### f-strings (Formatted String Literals)

An **f-string** is a string prefixed with `f` (or `F`). Inside the string, any expression wrapped in curly braces `{}` is evaluated and its value is inserted into the string at that position.

```python
# --- Pharmacy Example: f-string for a prescription summary ---
patient_name = "Sarah Johnson"
drug         = "Amoxicillin"
dose_mg      = 500
frequency    = "three times daily"

summary = f"{patient_name} is prescribed {drug} {dose_mg} mg {frequency}."
print(summary)
# Sarah Johnson is prescribed Amoxicillin 500 mg three times daily.
```

You can include any valid Python expression inside the braces:

```python
dose_mg      = 500
num_tablets  = 3
total_daily  = dose_mg * num_tablets

print(f"Total daily dose: {dose_mg} mg × {num_tablets} tablets = {total_daily} mg")
# Total daily dose: 500 mg × 3 tablets = 1500 mg
```

#### `.format()` as an Alternative

Before f-strings were introduced in Python 3.6, `.format()` was the standard approach. You may encounter it in older code, so it is worth knowing.

```python
# --- Pharmacy Example: .format() for a prescription summary ---
patient_name = "Sarah Johnson"
drug         = "Amoxicillin"
dose_mg      = 500

summary = "{} is prescribed {} {} mg.".format(patient_name, drug, dose_mg)
print(summary)
# Sarah Johnson is prescribed Amoxicillin 500 mg.

# Named placeholders (more readable)
summary_named = "{patient} is prescribed {drug} {dose} mg.".format(
    patient=patient_name,
    drug=drug,
    dose=dose_mg
)
print(summary_named)
```

#### Multi-line f-string for a Full Prescription Label

Combine triple quotes with an f-string prefix to build a complete, multi-line prescription label:

```python
# --- Pharmacy Example: multi-line f-string prescription label ---
rx_number    = "RX-20240115-001"
patient_name = "Sarah Johnson"
drug         = "Amoxicillin 500 mg Capsules"
directions   = "Take 1 capsule by mouth three times daily for 10 days."
prescriber   = "Dr. Emily Chen"
date         = "2024-01-15"

label = f"""
╔══════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#: {rx_number}
  Date: {date}
──────────────────────────────────────────
  Patient:    {patient_name}
  Drug:       {drug}
  Directions: {directions}
  Prescriber: {prescriber}
╚══════════════════════════════════════════╝
"""

print(label)
```

---

### Chapter Summary

- Strings store text data and can be created with single quotes, double quotes, or triple quotes for multi-line content.
- Escape characters like `\n` (newline) and `\t` (tab) let you control formatting within a string.
- Python uses **zero-based indexing** — the first character is at index `0`.
- **Negative indices** count from the end: `-1` is the last character.
- **Slicing** (`string[start:stop]`) extracts a substring without modifying the original.
- String methods (`upper`, `lower`, `strip`, `replace`, `split`, `join`, `find`, `startswith`, `endswith`) return new strings and are essential for cleaning and transforming pharmacy text data.
- **f-strings** (prefix `f"..."`) are the modern, readable way to embed variable values in strings.
- `.format()` is an older alternative you will encounter in existing code.

---

### Quiz

**1.** What is the output of the following code?

```python
drug_code = "PEN-250"
print(drug_code[0])
```

a) `"P"`
b) `"PEN"`
c) `"PEN-250"`
d) `0`

**2.** A pharmacist stores the following string:

```python
instruction = "   Take with food   "
```

Which method call produces `"Take with food"` (no surrounding spaces)?

a) `instruction.remove(" ")`
b) `instruction.strip()`
c) `instruction.replace(" ", "")`
d) `instruction.split()`

**3.** What does `"AMX-500"[0:3]` evaluate to?

a) `"AMX-"`
b) `"AMX"`
c) `"500"`
d) `"A"`

**4.** A pharmacist has a list of medications:

```python
meds = ["Metformin", "Lisinopril", "Aspirin"]
```

Which line of code produces the string `"Metformin | Lisinopril | Aspirin"`?

a) `meds.join(" | ")`
b) `" | ".join(meds)`
c) `str(meds)`
d) `meds.split(" | ")`

**5.** What is the output of the following code?

```python
filename = "patient_data.csv"
print(filename.endswith(".csv"))
```

a) `"csv"`
b) `True`
c) `False`
d) `".csv"`

**6.** Which f-string correctly builds the string `"Dose: 500 mg"`?

a) `f"Dose: {dose_mg mg}"`
b) `f"Dose: " + dose_mg + " mg"`
c) `f"Dose: {dose_mg} mg"`
d) `"Dose: {dose_mg} mg"`

**7.** What does `"Amoxicillin".find("cillin")` return?

a) `True`
b) `5`
c) `6`
d) `-1`

#### Answer Key

1. **a)** `drug_code[0]` retrieves the character at index 0, which is `"P"`.
2. **b)** `strip()` removes leading and trailing whitespace. `replace(" ", "")` would remove *all* spaces, giving `"Takewithfood"`.
3. **b)** `[0:3]` includes indices 0, 1, 2 — the characters `"A"`, `"M"`, `"X"` — giving `"AMX"`.
4. **b)** `join()` is called on the separator string, not the list: `separator.join(list)`.
5. **b)** `endswith()` returns a boolean. `"patient_data.csv"` ends with `".csv"`, so the result is `True`.
6. **c)** f-strings use `{variable}` inside the string. Option d) is a regular string — the braces are literal characters, not placeholders.
7. **b)** `"Amoxicillin".find("cillin")` — counting from 0: A(0) m(1) o(2) x(3) i(4) c(5) i(6) l(7) l(8) i(9) n(10). The substring `"cillin"` starts at index 5.

---

### Challenge

**Problem:** A pharmacy system needs to generate a formatted prescription label from raw patient and drug data. Your task is to write a Python program that takes the variables below and produces a neatly formatted multi-line label.

**Given variables:**

```python
patient_name  = "Sarah Johnson"
drug          = "Amoxicillin 500 mg Capsules"
dose_mg       = 500
route         = "by mouth"
frequency     = "three times daily"
duration_days = 10
prescriber    = "Dr. Emily Chen"
rx_number     = "RX-20240115-001"
```

**Expected output:**

```
╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        RX-20240115-001
──────────────────────────────────────────────────
  Patient:    Sarah Johnson
  Drug:       Amoxicillin 500 mg Capsules
  Dose:       500 mg
  Route:      by mouth
  Frequency:  three times daily
  Duration:   10 days
  Prescriber: Dr. Emily Chen
╚══════════════════════════════════════════════════╝
```

**Reference solution:**

```python
# --- Challenge: Prescription Label Generator ---
# Context: build a formatted label from patient and drug data using f-strings

patient_name  = "Sarah Johnson"
drug          = "Amoxicillin 500 mg Capsules"
dose_mg       = 500
route         = "by mouth"
frequency     = "three times daily"
duration_days = 10
prescriber    = "Dr. Emily Chen"
rx_number     = "RX-20240115-001"

label = f"""╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        {rx_number}
──────────────────────────────────────────────────
  Patient:    {patient_name}
  Drug:       {drug}
  Dose:       {dose_mg} mg
  Route:      {route}
  Frequency:  {frequency}
  Duration:   {duration_days} days
  Prescriber: {prescriber}
╚══════════════════════════════════════════════════╝"""

print(label)
```

**Try it yourself:** Extend the label to include a `date` variable (today's date as a string) and add a `"Date: {date}"` line below the Rx number. Then try using `.upper()` on `drug` so the drug name always prints in uppercase on the label.

---


---

## Chapter 5: Lists and Tuples

### Learning Objectives

- Understand what lists are and how to create and manipulate them
- Use list methods to add, remove, sort, and modify medication lists
- Apply list slicing and iteration techniques to process collections
- Understand tuples and when to use them instead of lists
- Write list comprehensions to filter and transform data efficiently

---

### Section 5.1: Lists

A **list** is an ordered, mutable collection of items. In Python, lists can hold any type of data — strings, numbers, or even other lists. Lists are perfect for storing collections like a patient's medication list, where you might need to add or remove items over time.

**Creating a List**

You create a list by placing items inside square brackets `[]`, separated by commas:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
print(medications)
# Output: ['Metformin', 'Lisinopril', 'Atorvastatin']
```

**List Indexing**

Just like strings, lists use zero-based indexing. You can access individual items by their position:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
print(medications[0])  # Output: Metformin
print(medications[1])  # Output: Lisinopril
print(medications[-1]) # Output: Atorvastatin (last item)
```

**Lists Can Hold Mixed Types**

While it's common to store items of the same type, Python lists can hold mixed data types:

```python
patient_info = ["John Doe", 45, 180.5, True]  # name, age, weight_lbs, is_active
print(patient_info)
# Output: ['John Doe', 45, 180.5, True]
```

---

### Section 5.2: List Methods

Python provides many built-in methods to manipulate lists. Let's explore each one with pharmacy examples.

**`append()` — Add a New Medication**

The `append()` method adds an item to the end of the list:

```python
medications = ["Metformin", "Lisinopril"]
medications.append("Atorvastatin")
print(medications)
# Output: ['Metformin', 'Lisinopril', 'Atorvastatin']
```

**`remove()` — Remove a Discontinued Medication**

The `remove()` method removes the first occurrence of a specified item:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
medications.remove("Lisinopril")
print(medications)
# Output: ['Metformin', 'Atorvastatin']
```

**`pop()` — Remove and Return the Last Item**

The `pop()` method removes and returns the last item (or an item at a specific index):

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
last_med = medications.pop()
print(last_med)        # Output: Atorvastatin
print(medications)     # Output: ['Metformin', 'Lisinopril']

# You can also pop by index
first_med = medications.pop(0)
print(first_med)       # Output: Metformin
print(medications)     # Output: ['Lisinopril']
```

**`insert()` — Insert a Medication at a Specific Position**

The `insert()` method inserts an item at a specified index:

```python
medications = ["Metformin", "Atorvastatin"]
medications.insert(1, "Lisinopril")
print(medications)
# Output: ['Metformin', 'Lisinopril', 'Atorvastatin']
```

**`sort()` — Sort Medications Alphabetically**

The `sort()` method sorts the list in place (modifies the original list):

```python
medications = ["Atorvastatin", "Metformin", "Lisinopril"]
medications.sort()
print(medications)
# Output: ['Atorvastatin', 'Lisinopril', 'Metformin']
```

**`reverse()` — Reverse the Order**

The `reverse()` method reverses the list in place:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
medications.reverse()
print(medications)
# Output: ['Atorvastatin', 'Lisinopril', 'Metformin']
```

**`len()` — Count Medications in the List**

The `len()` function returns the number of items in a list:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
count = len(medications)
print(f"Patient is taking {count} medications.")
# Output: Patient is taking 3 medications.
```

---

### Section 5.3: List Slicing and Iteration

**List Slicing**

Just like strings, you can slice lists to extract a portion:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin", "Amlodipine", "Omeprazole"]
first_three = medications[0:3]
print(first_three)
# Output: ['Metformin', 'Lisinopril', 'Atorvastatin']

last_two = medications[-2:]
print(last_two)
# Output: ['Amlodipine', 'Omeprazole']
```

**Iterating Over a List with a `for` Loop**

You can loop through each item in a list:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
for med in medications:
    print(f"Dispensing: {med}")

# Output:
# Dispensing: Metformin
# Dispensing: Lisinopril
# Dispensing: Atorvastatin
```

**Using `enumerate()` for Index and Value**

The `enumerate()` function gives you both the index and the value:

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
for index, med in enumerate(medications):
    print(f"{index + 1}. {med}")

# Output:
# 1. Metformin
# 2. Lisinopril
# 3. Atorvastatin
```

---

### Section 5.4: Tuples

A **tuple** is an ordered, immutable collection. Once you create a tuple, you cannot change its contents. Tuples are useful for data that should not be modified, such as a fixed drug administration schedule.

**Creating a Tuple**

You create a tuple using parentheses `()`:

```python
drug_schedule = ("08:00", "14:00", "20:00")
print(drug_schedule)
# Output: ('08:00', '14:00', '20:00')
```

**Immutability**

You cannot change, add, or remove items from a tuple after creation:

```python
drug_schedule = ("08:00", "14:00", "20:00")
# drug_schedule[0] = "09:00"  # This would raise a TypeError
```

**When to Use Tuples vs. Lists**

- Use **lists** when your data might change (e.g., a patient's medication list).
- Use **tuples** when your data is fixed (e.g., a standard dosing schedule, coordinates, or configuration settings).

**Tuple Unpacking**

You can unpack a tuple into separate variables:

```python
drug_schedule = ("08:00", "14:00", "20:00")
morning, afternoon, evening = drug_schedule
print(f"Morning dose: {morning}")
print(f"Afternoon dose: {afternoon}")
print(f"Evening dose: {evening}")

# Output:
# Morning dose: 08:00
# Afternoon dose: 14:00
# Evening dose: 20:00
```

---

### Section 5.5: List Comprehensions

A **list comprehension** is a concise way to create a new list by applying an expression to each item in an existing list. It's a powerful tool for filtering and transforming data.

**Basic Syntax**

```python
new_list = [expression for item in iterable]
```

**Filtering Medications Above a Dose Threshold**

Suppose you have a list of doses and want to filter only those above 100 mg:

```python
doses_mg = [50, 150, 200, 75, 300]
high_doses = [dose for dose in doses_mg if dose > 100]
print(high_doses)
# Output: [150, 200, 300]
```

**Transforming a List**

You can transform each item in a list. For example, converting all drug names to uppercase:

```python
medications = ["metformin", "lisinopril", "atorvastatin"]
medications_upper = [med.upper() for med in medications]
print(medications_upper)
# Output: ['METFORMIN', 'LISINOPRIL', 'ATORVASTATIN']
```

**Combining Filter and Transform**

You can filter and transform in one step:

```python
doses_mg = [50, 150, 200, 75, 300]
high_doses_doubled = [dose * 2 for dose in doses_mg if dose > 100]
print(high_doses_doubled)
# Output: [300, 400, 600]
```

---

### Chapter Summary

- **Lists** are ordered, mutable collections perfect for storing items like medication lists.
- **List methods** (`append()`, `remove()`, `pop()`, `insert()`, `sort()`, `reverse()`, `len()`) let you manipulate lists easily.
- **List slicing** and **iteration** allow you to work with portions of a list and process each item.
- **Tuples** are ordered, immutable collections used for fixed data like dosing schedules.
- **List comprehensions** provide a concise way to filter and transform lists.

---

### Quiz

**1. What is the output of the following code?**

```python
medications = ["Aspirin", "Ibuprofen", "Acetaminophen"]
print(medications[1])
```

a) Aspirin  
b) Ibuprofen  
c) Acetaminophen  
d) Error

**2. Which method would you use to add a new medication to the end of a list?**

a) `insert()`  
b) `append()`  
c) `add()`  
d) `push()`

**3. What happens when you call `medications.pop()` on a list?**

a) Removes the first item  
b) Removes and returns the last item  
c) Removes all items  
d) Raises an error

**4. True or False: You can change the value of an item in a tuple after it is created.**

a) True  
b) False

**5. What is the output of the following code?**

```python
doses = [100, 200, 50, 300]
high_doses = [d for d in doses if d > 150]
print(high_doses)
```

a) `[100, 200, 50, 300]`  
b) `[200, 300]`  
c) `[100, 50]`  
d) `[150]`

**6. Which of the following creates a tuple?**

a) `medications = ["Aspirin", "Ibuprofen"]`  
b) `medications = ("Aspirin", "Ibuprofen")`  
c) `medications = {"Aspirin", "Ibuprofen"}`  
d) `medications = {Aspirin: 1, Ibuprofen: 2}`

**7. What does `len(medications)` return if `medications = ["A", "B", "C"]`?**

a) 2  
b) 3  
c) 4  
d) Error

---

### Answer Key

1. **b) Ibuprofen** — Lists use zero-based indexing, so `medications[1]` is the second item.
2. **b) `append()`** — The `append()` method adds an item to the end of a list.
3. **b) Removes and returns the last item** — `pop()` removes and returns the last item by default.
4. **b) False** — Tuples are immutable; you cannot change their contents after creation.
5. **b) `[200, 300]`** — The list comprehension filters doses greater than 150.
6. **b) `medications = ("Aspirin", "Ibuprofen")`** — Tuples are created with parentheses.
7. **b) 3** — `len()` returns the number of items in the list.

---

### Challenge

**Problem: Manage a Patient's Medication List**

Write a Python program that:

1. Starts with an initial list of 3 medications.
2. Adds a new medication to the list.
3. Removes a discontinued medication.
4. Sorts the list alphabetically.
5. Prints the final list with numbered items.

**Expected Output:**

```
Initial medications: ['Metformin', 'Lisinopril', 'Atorvastatin']
After adding Amlodipine: ['Metformin', 'Lisinopril', 'Atorvastatin', 'Amlodipine']
After removing Lisinopril: ['Metformin', 'Atorvastatin', 'Amlodipine']
After sorting: ['Amlodipine', 'Atorvastatin', 'Metformin']
Final medication list:
1. Amlodipine
2. Atorvastatin
3. Metformin
```

---

### Reference Solution

```python
# Step 1: Start with an initial list of 3 medications
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
print(f"Initial medications: {medications}")

# Step 2: Add a new medication
medications.append("Amlodipine")
print(f"After adding Amlodipine: {medications}")

# Step 3: Remove a discontinued medication
medications.remove("Lisinopril")
print(f"After removing Lisinopril: {medications}")

# Step 4: Sort the list alphabetically
medications.sort()
print(f"After sorting: {medications}")

# Step 5: Print the final list with numbered items
print("Final medication list:")
for index, med in enumerate(medications, start=1):
    print(f"{index}. {med}")
```

**Output:**

```
Initial medications: ['Metformin', 'Lisinopril', 'Atorvastatin']
After adding Amlodipine: ['Metformin', 'Lisinopril', 'Atorvastatin', 'Amlodipine']
After removing Lisinopril: ['Metformin', 'Atorvastatin', 'Amlodipine']
After sorting: ['Amlodipine', 'Atorvastatin', 'Metformin']
Final medication list:
1. Amlodipine
2. Atorvastatin
3. Metformin
```

---

## Chapter 6: Dictionaries and Sets

### Learning Objectives

By the end of this chapter, you will be able to:

- Explain what a dictionary is and how key-value pairs work
- Create and manipulate patient record dictionaries
- Use dictionary methods: `get()`, `keys()`, `values()`, `items()`, `update()`
- Explain what a set is and why it enforces uniqueness
- Perform set operations: union, intersection, and difference
- Apply dictionaries and sets to real pharmacy scenarios like patient records and drug databases

---

### Section 6.1: Dictionaries

A **dictionary** is a collection of **key-value pairs**. Think of it like a patient chart: each field (key) maps to a specific piece of information (value). Dictionaries are:

- **Unordered** — items don't have a fixed position (though Python 3.7+ preserves insertion order)
- **Mutable** — you can add, update, or remove entries after creation
- **Indexed by keys** — you look up values by their key, not by a number

#### Creating a Patient Record Dictionary

```python
# --- Pharmacy Example: Patient Record ---
# Context: Store a patient's complete profile in a single dictionary

patient = {
    "name": "Sarah Johnson",
    "age": 45,
    "weight_kg": 68.0,
    "medications": ["Metformin", "Lisinopril", "Atorvastatin"],
    "allergies": ["Penicillin"]
}

print(patient)
```

**Output:**
```
{'name': 'Sarah Johnson', 'age': 45, 'weight_kg': 68.0, 'medications': ['Metformin', 'Lisinopril', 'Atorvastatin'], 'allergies': ['Penicillin']}
```

#### Keys and Values

- **Keys** are the labels: `"name"`, `"age"`, `"weight_kg"`, etc. Keys must be unique and are usually strings.
- **Values** are the data stored under each key. Values can be any type — strings, numbers, lists, even other dictionaries.

#### Accessing Values

Use square bracket notation with the key name:

```python
# --- Pharmacy Example: Accessing patient data ---
# Context: Retrieve specific fields from a patient record

print(patient["name"])       # Sarah Johnson
print(patient["age"])        # 45
print(patient["medications"])  # ['Metformin', 'Lisinopril', 'Atorvastatin']
```

**Output:**
```
Sarah Johnson
45
['Metformin', 'Lisinopril', 'Atorvastatin']
```

---

### Section 6.2: Dictionary Operations

#### Accessing Values — Bracket Notation vs `.get()`

Bracket notation raises a `KeyError` if the key doesn't exist. The `.get()` method returns `None` (or a default you specify) instead of crashing:

```python
# --- Pharmacy Example: Safe vs. direct access ---
# Context: Retrieve a field that may or may not exist in the record

# Direct access — works fine when key exists
print(patient["name"])          # Sarah Johnson

# .get() — safe access with a default fallback
print(patient.get("phone", "No phone on file"))  # No phone on file
```

#### Adding New Entries

```python
# --- Pharmacy Example: Adding a prescriber to the record ---
# Context: Update the patient record with the prescribing physician

patient["prescriber"] = "Dr. Emily Chen"
print(patient["prescriber"])    # Dr. Emily Chen
```

#### Updating Existing Entries

```python
# --- Pharmacy Example: Updating patient age at annual review ---
# Context: Patient's age changes; update the record

patient["age"] = 46
print(patient["age"])           # 46
```

#### Deleting Entries

```python
# --- Pharmacy Example: Removing allergy field after review ---
# Context: Allergy information moved to a separate system

del patient["allergies"]
print("allergies" in patient)   # False
```

#### Iterating Over Keys

```python
# --- Pharmacy Example: List all fields in a patient record ---
# Context: Print every field name in the dictionary

for key in patient:
    print(key)
```

**Output:**
```
name
age
weight_kg
medications
prescriber
```

#### Iterating Over Values

```python
# --- Pharmacy Example: Print all values in a patient record ---
# Context: Display every stored value

for value in patient.values():
    print(value)
```

#### Iterating Over Key-Value Pairs

```python
# --- Pharmacy Example: Print a full patient summary ---
# Context: Display each field and its value side by side

for key, value in patient.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Sarah Johnson
age: 46
weight_kg: 68.0
medications: ['Metformin', 'Lisinopril', 'Atorvastatin']
prescriber: Dr. Emily Chen
```

---

### Section 6.3: Dictionary Methods

#### `get()` — Safe Access with a Default

```python
# --- Pharmacy Example: Retrieve notes field safely ---
# Context: Not all patients have clinical notes on file

notes = patient.get("notes", "No notes available")
print(notes)    # No notes available
```

#### `keys()` — List All Fields

```python
# --- Pharmacy Example: Inspect all fields in a patient record ---
# Context: Confirm which fields are stored before processing

fields = list(patient.keys())
print(fields)
# ['name', 'age', 'weight_kg', 'medications', 'prescriber']
```

#### `values()` — List All Values

```python
# --- Pharmacy Example: Collect all values for export ---
# Context: Prepare patient data for a report

values = list(patient.values())
print(values)
```

#### `items()` — Iterate Over Key-Value Pairs

```python
# --- Pharmacy Example: Build a formatted patient summary ---
# Context: Generate a readable report from the patient dictionary

print("=== Patient Summary ===")
for field, data in patient.items():
    print(f"  {field.capitalize()}: {data}")
```

#### `update()` — Merge Two Dictionaries

```python
# --- Pharmacy Example: Merge updated patient data ---
# Context: A new intake form provides updated information; merge it in

updated_info = {
    "age": 47,
    "weight_kg": 70.5,
    "phone": "555-0192"
}

patient.update(updated_info)
print(patient["age"])        # 47
print(patient["weight_kg"])  # 70.5
print(patient["phone"])      # 555-0192
```

#### Introducing the Drug Database Entry

Dictionaries can hold other dictionaries as values — this is called a **nested dictionary**. Here's the Drug Database model used throughout the rest of the handbook:

```python
# --- Pharmacy Example: Drug database with nested entries ---
# Context: Each drug maps to a sub-dictionary of clinical properties

drug_db = {
    "Amoxicillin": {"class": "Antibiotic",    "max_dose_mg": 3000, "unit": "mg"},
    "Metformin":   {"class": "Antidiabetic",  "max_dose_mg": 2550, "unit": "mg"},
    "Lisinopril":  {"class": "ACE Inhibitor", "max_dose_mg": 40,   "unit": "mg"},
}

# Look up a specific drug
drug = "Metformin"
print(f"{drug} max dose: {drug_db[drug]['max_dose_mg']} {drug_db[drug]['unit']}")
# Metformin max dose: 2550 mg
```

To access a nested value, chain two sets of square brackets: `drug_db["Metformin"]["max_dose_mg"]`.

---

### Section 6.4: Sets

A **set** is an unordered collection of **unique** elements. Sets automatically remove duplicates, which makes them perfect for tracking which drugs a patient is taking — no double-counting.

Key properties of sets:
- **Unordered** — no index, no guaranteed order
- **Unique elements** — duplicates are silently ignored
- **Mutable** — you can add and remove items

#### Creating Sets of Drug Names

```python
# --- Pharmacy Example: Drug sets for two patients ---
# Context: Track which medications each patient is currently taking

patient_a_meds = {"Metformin", "Lisinopril", "Atorvastatin", "Aspirin"}
patient_b_meds = {"Lisinopril", "Atorvastatin", "Amlodipine", "Aspirin"}

print(patient_a_meds)
# {'Metformin', 'Lisinopril', 'Atorvastatin', 'Aspirin'}  (order may vary)
```

#### Set Operations

**Union (`|`) — All drugs across both patients**

```python
# --- Pharmacy Example: Combined drug list ---
# Context: Find every drug prescribed to either patient

all_meds = patient_a_meds | patient_b_meds
print("All medications:", all_meds)
# {'Metformin', 'Lisinopril', 'Atorvastatin', 'Aspirin', 'Amlodipine'}
```

**Intersection (`&`) — Drugs both patients are taking**

```python
# --- Pharmacy Example: Shared medications ---
# Context: Identify drugs common to both patients (useful for bulk ordering)

shared_meds = patient_a_meds & patient_b_meds
print("Shared medications:", shared_meds)
# {'Lisinopril', 'Atorvastatin', 'Aspirin'}
```

**Difference (`-`) — Drugs patient A takes that patient B doesn't**

```python
# --- Pharmacy Example: Unique medications for patient A ---
# Context: Find drugs exclusive to patient A's regimen

only_patient_a = patient_a_meds - patient_b_meds
print("Only patient A:", only_patient_a)
# {'Metformin'}
```

#### Set Methods

```python
# --- Pharmacy Example: Modifying a medication set ---
# Context: Update patient A's drug set as their regimen changes

# add() — add a new drug
patient_a_meds.add("Omeprazole")
print("After add:", patient_a_meds)

# remove() — remove a drug (raises KeyError if not found)
patient_a_meds.remove("Aspirin")
print("After remove:", patient_a_meds)

# discard() — remove a drug safely (no error if not found)
patient_a_meds.discard("Warfarin")   # Warfarin wasn't there — no crash
print("After discard:", patient_a_meds)
```

**Output:**
```
After add: {'Metformin', 'Lisinopril', 'Atorvastatin', 'Omeprazole', 'Aspirin'}
After remove: {'Metformin', 'Lisinopril', 'Atorvastatin', 'Omeprazole'}
After discard: {'Metformin', 'Lisinopril', 'Atorvastatin', 'Omeprazole'}
```

> **Tip:** Use `remove()` when you're certain the item exists. Use `discard()` when you're not sure — it won't raise an error if the item is missing.

---

### Chapter Summary

- A **dictionary** stores data as key-value pairs. Keys are unique labels; values can be any type.
- Access values with `dict["key"]` or safely with `dict.get("key", default)`.
- Add entries with `dict["new_key"] = value`, update with assignment or `.update()`, delete with `del`.
- Iterate over keys with `for k in dict:`, values with `.values()`, and pairs with `.items()`.
- **Nested dictionaries** (like the drug database) let you store structured records inside a dictionary.
- A **set** stores unique, unordered elements — perfect for tracking drug lists without duplicates.
- Set operations: `|` (union), `&` (intersection), `-` (difference).
- Set methods: `add()`, `remove()` (raises error if missing), `discard()` (safe removal).

---

### Quiz

**1.** What is the output of the following code?

```python
patient = {"name": "Sarah Johnson", "age": 45}
print(patient["age"])
```

a) `"age"`
b) `45`
c) `"45"`
d) `KeyError`

**2.** Which method retrieves a value from a dictionary without raising an error if the key is missing?

a) `dict["key"]`
b) `dict.fetch("key")`
c) `dict.get("key")`
d) `dict.find("key")`

**3.** A pharmacist runs this code:

```python
drug_db = {"Metformin": {"max_dose_mg": 2550}, "Lisinopril": {"max_dose_mg": 40}}
drug_db["Aspirin"] = {"max_dose_mg": 4000}
print(len(drug_db))
```

What is printed?

a) `2`
b) `3`
c) `4`
d) `TypeError`

**4.** What does the following set operation return?

```python
meds_a = {"Metformin", "Lisinopril", "Aspirin"}
meds_b = {"Lisinopril", "Atorvastatin", "Aspirin"}
print(meds_a & meds_b)
```

a) `{'Metformin', 'Lisinopril', 'Atorvastatin', 'Aspirin'}`
b) `{'Lisinopril', 'Aspirin'}`
c) `{'Metformin'}`
d) `{'Atorvastatin'}`

**5.** What is the difference between `set.remove("Warfarin")` and `set.discard("Warfarin")` when `"Warfarin"` is not in the set?

a) Both raise a `KeyError`
b) `remove()` raises a `KeyError`; `discard()` does nothing
c) `discard()` raises a `KeyError`; `remove()` does nothing
d) Both do nothing

**6.** A pharmacist wants to print every drug name and its maximum dose from this dictionary:

```python
drug_db = {
    "Amoxicillin": {"max_dose_mg": 3000},
    "Metformin":   {"max_dose_mg": 2550},
}
```

Which loop correctly does this?

a) `for drug in drug_db.values(): print(drug, drug_db[drug]["max_dose_mg"])`
b) `for drug, info in drug_db.items(): print(drug, info["max_dose_mg"])`
c) `for drug in drug_db.keys(): print(drug_db["max_dose_mg"])`
d) `for drug in drug_db: print(drug_db.values())`

**7.** What is the output?

```python
meds = {"Metformin", "Lisinopril", "Metformin", "Aspirin"}
print(len(meds))
```

a) `4`
b) `3`
c) `2`
d) `TypeError`

---

#### Answer Key

1. **b) `45`** — `patient["age"]` retrieves the value stored under the key `"age"`.
2. **c) `dict.get("key")`** — `.get()` returns `None` (or a specified default) instead of raising a `KeyError`.
3. **b) `3`** — Adding `"Aspirin"` brings the total to 3 entries.
4. **b) `{'Lisinopril', 'Aspirin'}`** — `&` (intersection) returns only elements present in both sets.
5. **b) `remove()` raises a `KeyError`; `discard()` does nothing** — Use `discard()` for safe removal.
6. **b) `for drug, info in drug_db.items(): print(drug, info["max_dose_mg"])`** — `.items()` unpacks each key-value pair.
7. **b) `3`** — Sets automatically remove duplicates; `"Metformin"` appears only once.

---

### Challenge

**Problem: Build a Drug Database Dictionary**

You are building a simple drug reference tool for a pharmacy. Your task is to create and manage a drug database using a dictionary.

**Steps:**

1. Create a `drug_db` dictionary with at least 4 drugs. Each drug entry must include:
   - `"class"` — the drug class (e.g., `"Antibiotic"`)
   - `"max_dose_mg"` — the maximum daily dose in milligrams
   - `"unit"` — the dose unit (e.g., `"mg"`)

2. Write a `lookup_drug(name)` function that takes a drug name and returns its details, or a friendly message if the drug is not found.

3. Add a new drug to the database.

4. Update the `max_dose_mg` for an existing drug.

5. Print all drugs and their maximum doses.

**Expected Output:**

```
=== Drug Database ===
Amoxicillin  | Class: Antibiotic    | Max dose: 3000 mg
Metformin    | Class: Antidiabetic  | Max dose: 2550 mg
Lisinopril   | Class: ACE Inhibitor | Max dose: 40 mg
Atorvastatin | Class: Statin        | Max dose: 80 mg

Looking up Metformin...
{'class': 'Antidiabetic', 'max_dose_mg': 2550, 'unit': 'mg'}

Looking up Warfarin...
Warfarin not found in database.

After adding Omeprazole:
Amoxicillin  | Class: Antibiotic    | Max dose: 3000 mg
Metformin    | Class: Antidiabetic  | Max dose: 2550 mg
Lisinopril   | Class: ACE Inhibitor | Max dose: 40 mg
Atorvastatin | Class: Statin        | Max dose: 80 mg
Omeprazole   | Class: PPI           | Max dose: 40 mg

After updating Lisinopril max dose to 80 mg:
Lisinopril max dose is now 80 mg
```

---

### Reference Solution

```python
# Step 1: Create the drug database with 4 drugs
drug_db = {
    "Amoxicillin":  {"class": "Antibiotic",    "max_dose_mg": 3000, "unit": "mg"},
    "Metformin":    {"class": "Antidiabetic",  "max_dose_mg": 2550, "unit": "mg"},
    "Lisinopril":   {"class": "ACE Inhibitor", "max_dose_mg": 40,   "unit": "mg"},
    "Atorvastatin": {"class": "Statin",        "max_dose_mg": 80,   "unit": "mg"},
}

def print_database(db):
    """Print all drugs and their maximum doses."""
    for drug, info in db.items():
        print(f"{drug:<12} | Class: {info['class']:<14} | Max dose: {info['max_dose_mg']} {info['unit']}")

# Step 2: Lookup function
def lookup_drug(name):
    """Return drug details or a not-found message."""
    return drug_db.get(name, f"{name} not found in database.")

# Print initial database
print("=== Drug Database ===")
print_database(drug_db)

# Test the lookup function
print("\nLooking up Metformin...")
print(lookup_drug("Metformin"))

print("\nLooking up Warfarin...")
print(lookup_drug("Warfarin"))

# Step 3: Add a new drug
drug_db["Omeprazole"] = {"class": "PPI", "max_dose_mg": 40, "unit": "mg"}
print("\nAfter adding Omeprazole:")
print_database(drug_db)

# Step 4: Update max dose for an existing drug
drug_db["Lisinopril"]["max_dose_mg"] = 80
print(f"\nAfter updating Lisinopril max dose to 80 mg:")
print(f"Lisinopril max dose is now {drug_db['Lisinopril']['max_dose_mg']} mg")
```

---

## Chapter 7: Control Flow — Conditionals

### Learning Objectives

By the end of this chapter, you will be able to:

- Explain what control flow is and why it matters in pharmacy programs
- Write `if`, `elif`, and `else` statements to make decisions in code
- Use nested conditionals to check multiple conditions together
- Write ternary (conditional) expressions for concise one-line decisions
- Apply conditional logic to real pharmacy scenarios such as dose range checking and pediatric dosing

---

### Section 7.1: if, elif, else

#### What is Control Flow?

So far, every program you have written runs from top to bottom, executing every line in order. **Control flow** lets your program make decisions — it can choose which lines to run based on conditions. This is exactly what a pharmacist does when checking a prescription: *"If the dose is above the safe limit, warn the prescriber. Otherwise, dispense as written."*

Python uses `if`, `elif`, and `else` to implement this decision-making logic.

---

#### The `if` Statement

The simplest form checks a single condition. If the condition is `True`, the indented block runs. If it is `False`, Python skips it.

**Syntax:**

```python
if condition:
    # code to run when condition is True
```

Two things to notice:
1. The line ends with a **colon** (`:`).
2. The code inside the block is **indented** (4 spaces or 1 tab). Python uses indentation — not curly braces — to define blocks.

**Pharmacy example — dose range checking:**

```python
# --- Pharmacy Example: Maximum dose check ---
# Context: Alert the pharmacist if a prescribed dose exceeds the safe maximum.

dose_mg = 750
max_safe_dose = 1000

if dose_mg > max_safe_dose:
    print("WARNING: Dose exceeds maximum safe limit!")
```

Because `750 > 1000` is `False`, nothing is printed. Change `dose_mg` to `1200` and the warning appears.

---

#### The `if / else` Statement

Add an `else` block to handle the case when the condition is `False`:

```python
# --- Pharmacy Example: Formulary check ---
# Context: Check whether a drug is on the hospital formulary before dispensing.

drug_name = "Warfarin"
formulary = ["Metformin", "Lisinopril", "Atorvastatin", "Warfarin", "Amoxicillin"]

if drug_name in formulary:
    print(f"{drug_name} is on the formulary. Proceed with dispensing.")
else:
    print(f"{drug_name} is NOT on the formulary. Contact the prescriber for an alternative.")
```

Output:
```
Warfarin is on the formulary. Proceed with dispensing.
```

---

#### The `if / elif / else` Statement

Use `elif` (short for "else if") when you have more than two possible outcomes. Python checks each condition in order and runs the first block whose condition is `True`. The `else` block is a catch-all for anything that doesn't match.

**Pharmacy example — dose categorisation:**

```python
# --- Pharmacy Example: Dose category classification ---
# Context: Classify a prescribed dose as sub-therapeutic, therapeutic, or toxic.

dose_mg = 450
min_therapeutic = 250
max_therapeutic = 1000

if dose_mg < min_therapeutic:
    category = "Sub-therapeutic"
    recommendation = "Dose is too low. Consider increasing to therapeutic range."
elif dose_mg <= max_therapeutic:
    category = "Therapeutic"
    recommendation = "Dose is within the therapeutic range. Safe to dispense."
else:
    category = "Toxic"
    recommendation = "Dose exceeds safe limit. Do NOT dispense. Contact prescriber immediately."

print(f"Dose: {dose_mg} mg")
print(f"Category: {category}")
print(f"Recommendation: {recommendation}")
```

Output:
```
Dose: 450 mg
Category: Therapeutic
Recommendation: Dose is within the therapeutic range. Safe to dispense.
```

You can chain as many `elif` blocks as you need. Python evaluates them top to bottom and stops at the first match.

---

### Section 7.2: Nested Conditionals

Sometimes a decision depends on more than one condition that must be checked in sequence. You can place an `if` statement **inside** another `if` statement — this is called a **nested conditional**.

Think of it like a triage protocol: first check whether the patient is a child, then — only if they are — check their weight to determine the correct dosing protocol.

**Pharmacy example — pediatric dosing:**

```python
# --- Pharmacy Example: Pediatric dosing protocol ---
# Context: Select the correct dosing protocol based on patient age and weight.

patient_age = 10      # years
weight_kg = 32.0      # kilograms

if patient_age <= 18:
    if weight_kg < 40:
        print("Use pediatric low-weight dosing protocol")
    else:
        print("Use standard pediatric dosing protocol")
else:
    print("Use adult dosing protocol")
```

Output:
```
Use pediatric low-weight dosing protocol
```

**How it works:**
1. The outer `if` checks whether the patient is 18 or younger.
2. Only if that is `True` does Python enter the inner block and check the weight.
3. If the patient is older than 18, the inner block is never reached.

**Tip:** Deeply nested conditionals can become hard to read. If you find yourself nesting three or more levels deep, consider restructuring with `and` (covered in Chapter 3) or breaking the logic into a function (covered in Chapter 9).

---

### Section 7.3: Ternary (Conditional) Expression

Python provides a compact one-line form for simple `if/else` decisions called the **ternary expression** (also called a conditional expression):

```python
value = value_if_true if condition else value_if_false
```

This is useful when you want to assign one of two values based on a condition, without writing a full four-line `if/else` block.

**Pharmacy example:**

```python
# --- Pharmacy Example: Dose label assignment ---
# Context: Assign a short label to a dose for display on a dispensing screen.

dose_mg = 750

dose_label = "HIGH" if dose_mg > 500 else "STANDARD"

print(f"Dose: {dose_mg} mg — Label: {dose_label}")
```

Output:
```
Dose: 750 mg — Label: HIGH
```

The ternary expression reads almost like plain English: *"The label is HIGH if the dose is above 500, otherwise it is STANDARD."*

Use ternary expressions for simple, readable one-liners. For anything more complex — multiple conditions, side effects, or nested logic — stick with a full `if/elif/else` block.

---

### Chapter Summary

- **Control flow** lets a program make decisions instead of running every line unconditionally.
- An `if` statement runs a block only when its condition is `True`.
- `else` provides a fallback block that runs when the `if` condition is `False`.
- `elif` lets you chain multiple conditions; Python runs the first matching block.
- **Nested conditionals** place one `if` inside another to check conditions in sequence (e.g., age then weight for pediatric dosing).
- The **ternary expression** (`x if condition else y`) is a concise one-line alternative for simple two-way decisions.
- Always end `if`, `elif`, and `else` lines with a colon, and indent the body consistently.

---

### Quiz

**Question 1**
A pharmacist's program contains the following code:

```python
dose_mg = 1200
max_safe_dose = 1000

if dose_mg > max_safe_dose:
    print("WARNING: Dose exceeds maximum safe limit!")
else:
    print("Dose is within safe limits.")
```

What is printed?

A) `Dose is within safe limits.`
B) `WARNING: Dose exceeds maximum safe limit!`
C) Nothing is printed
D) A `SyntaxError` is raised

---

**Question 2**
Which of the following correctly classifies a dose of `200 mg` given `min_dose = 250` and `max_dose = 1000`?

```python
if dose_mg < min_dose:
    print("Sub-therapeutic")
elif dose_mg <= max_dose:
    print("Therapeutic")
else:
    print("Toxic")
```

A) `Therapeutic`
B) `Toxic`
C) `Sub-therapeutic`
D) Nothing is printed

---

**Question 3**
What is wrong with the following code?

```python
dose_mg = 500
if dose_mg > 250
    print("Dose is above minimum threshold.")
```

A) `dose_mg` should be a string
B) The `if` line is missing a colon at the end
C) The `print` statement is not indented
D) `>` should be `>=`

---

**Question 4**
A pharmacist wants to check whether a patient qualifies for a high-dose protocol. The patient must be over 18 **and** weigh more than 70 kg. Which code correctly implements this using nested conditionals?

A)
```python
if patient_age > 18:
    if weight_kg > 70:
        print("Qualifies for high-dose protocol")
```

B)
```python
if patient_age > 18 or weight_kg > 70:
    print("Qualifies for high-dose protocol")
```

C)
```python
if patient_age > 18:
print("Qualifies for high-dose protocol")
```

D)
```python
elif patient_age > 18:
    if weight_kg > 70:
        print("Qualifies for high-dose protocol")
```

---

**Question 5**
What does the following ternary expression evaluate to when `dose_mg = 300`?

```python
dose_label = "HIGH" if dose_mg > 500 else "STANDARD"
```

A) `"HIGH"`
B) `"STANDARD"`
C) `True`
D) `None`

---

**Question 6**
A program checks whether a drug is a controlled substance and whether the prescriber has the correct DEA registration. Which structure is most appropriate?

A) A single `if` statement
B) A ternary expression
C) Nested `if` statements
D) An `else` block without an `if`

---

**Question 7**
How many `elif` blocks can a single `if` statement have in Python?

A) Exactly one
B) Exactly two
C) As many as needed
D) None — `elif` is not valid Python

---

#### Answer Key

1. **B** — `1200 > 1000` is `True`, so the `if` block runs and prints the warning.
2. **C** — `200 < 250` is `True`, so the first branch (`Sub-therapeutic`) is printed.
3. **B** — The `if` line is missing the required colon (`:`) at the end. Python will raise a `SyntaxError`.
4. **A** — Nested `if` statements correctly enforce both conditions in sequence. Option B uses `or` (only one condition needs to be true). Option C has a missing colon and incorrect indentation. Option D starts with `elif`, which is invalid without a preceding `if`.
5. **B** — `300 > 500` is `False`, so the expression evaluates to `"STANDARD"`.
6. **C** — Nested `if` statements are ideal when the second check only makes sense after the first check passes.
7. **C** — Python allows any number of `elif` blocks in a single `if/elif/else` chain.

---

### Challenge

#### Problem: Dose Validation Program

Write a Python program that:

1. Takes a prescribed dose (e.g., `250 mg`)
2. Takes the therapeutic range (`min_dose = 250`, `max_dose = 1000`)
3. Categorises the dose as:
   - **"Sub-therapeutic"** — below `min_dose`
   - **"Therapeutic"** — within the range (inclusive)
   - **"Toxic"** — above `max_dose`
4. Prints the category and a recommendation for the pharmacist

#### Expected Output

For a dose of `250 mg` with `min_dose = 250` and `max_dose = 1000`:

```
Dose entered: 250 mg
Therapeutic range: 250 mg – 1000 mg

Category: Therapeutic
Recommendation: Dose is within the therapeutic range. Safe to dispense.
```

For a dose of `150 mg`:

```
Dose entered: 150 mg
Therapeutic range: 250 mg – 1000 mg

Category: Sub-therapeutic
Recommendation: Dose is below the minimum therapeutic threshold. Consider increasing the dose or consulting the prescriber.
```

For a dose of `1200 mg`:

```
Dose entered: 1200 mg
Therapeutic range: 250 mg – 1000 mg

Category: Toxic
Recommendation: Dose exceeds the maximum safe limit. Do NOT dispense. Contact the prescriber immediately.
```

#### Reference Solution

```python
# --- Challenge: Dose Validation Program ---
# Categorises a prescribed dose as sub-therapeutic, therapeutic, or toxic.

# Input values (in a real program these could come from input())
prescribed_dose_mg = 250
min_dose = 250
max_dose = 1000

# Display the inputs
print(f"Dose entered: {prescribed_dose_mg} mg")
print(f"Therapeutic range: {min_dose} mg – {max_dose} mg")
print()

# Categorise the dose
if prescribed_dose_mg < min_dose:
    category = "Sub-therapeutic"
    recommendation = (
        "Dose is below the minimum therapeutic threshold. "
        "Consider increasing the dose or consulting the prescriber."
    )
elif prescribed_dose_mg <= max_dose:
    category = "Therapeutic"
    recommendation = "Dose is within the therapeutic range. Safe to dispense."
else:
    category = "Toxic"
    recommendation = (
        "Dose exceeds the maximum safe limit. "
        "Do NOT dispense. Contact the prescriber immediately."
    )

# Display the result
print(f"Category: {category}")
print(f"Recommendation: {recommendation}")
```

**Try it yourself:** Change `prescribed_dose_mg` to `150` and then to `1200` to see all three categories in action.

---

## Chapter 8: Control Flow — Loops

**Learning Objectives**

By the end of this chapter, you will be able to:

- Use `for` loops to iterate over lists of medications and patient records
- Use `while` loops to repeat actions until a valid condition is met
- Control loop execution with `break`, `continue`, and `pass`
- Generate numeric sequences with the `range()` function
- Write nested loops to process multi-level data structures like patients and their medications

---

### Section 8.1: for Loops

A `for` loop lets you repeat a block of code once for each item in a sequence — a list, tuple, string, or any iterable. Think of it like going through a prescription queue: you process each prescription one by one until there are none left.

**Basic syntax:**

```python
for variable in sequence:
    # code to run for each item
```

**Iterating over a medication list:**

```python
medications = ["Metformin", "Lisinopril", "Atorvastatin"]
for drug in medications:
    print(f"Dispensing: {drug}")
```

Output:
```
Dispensing: Metformin
Dispensing: Lisinopril
Dispensing: Atorvastatin
```

Each time through the loop, `drug` takes the value of the next item in the list. The loop runs three times — once per medication.

**Iterating over a list of dictionaries:**

Real pharmacy data often comes as a list of records. Here's how to loop over medication entries that each have a name and a dose:

```python
medication_entries = [
    {"name": "Metformin", "dose_mg": 500},
    {"name": "Lisinopril", "dose_mg": 10},
    {"name": "Atorvastatin", "dose_mg": 20},
]

for entry in medication_entries:
    print(f"{entry['name']}: {entry['dose_mg']} mg")
```

Output:
```
Metformin: 500 mg
Lisinopril: 10 mg
Atorvastatin: 20 mg
```

Each `entry` is a dictionary, so you access its values with `entry['key']`.

---

### Section 8.2: while Loops

A `while` loop keeps running as long as a condition is `True`. It's useful when you don't know in advance how many times you need to repeat something — for example, prompting a user until they enter a valid value.

**Basic syntax:**

```python
while condition:
    # code to run while condition is True
```

**Valid-dose-input prompt example:**

```python
dose_mg = -1
while dose_mg <= 0:
    dose_mg = int(input("Enter dose in mg (must be positive): "))
print(f"Dose accepted: {dose_mg} mg")
```

The loop keeps asking for input as long as the entered dose is zero or negative. Once the pharmacist enters a positive number, the condition becomes `False` and the loop exits.

**⚠️ Warning: Infinite Loops**

If the condition in a `while` loop never becomes `False`, the loop runs forever — this is called an **infinite loop**. Your program will freeze and you'll need to force-quit it (usually `Ctrl+C`).

```python
# DANGER: this loop never ends!
while True:
    print("Processing...")  # no way to exit
```

Always make sure something inside the loop will eventually make the condition `False`, or use a `break` statement (covered next) to exit.

---

### Section 8.3: break, continue, pass

These three keywords give you fine-grained control over what happens inside a loop.

#### `break` — Exit the loop early

`break` immediately stops the loop, even if there are items left to process. Use it when you've found what you're looking for and don't need to keep searching.

```python
medications = ["Metformin", "Lisinopril", "Warfarin", "Atorvastatin"]
target = "Warfarin"

for drug in medications:
    if drug == target:
        print(f"Found high-risk medication: {drug}. Stopping search.")
        break
    print(f"Checked: {drug}")
```

Output:
```
Checked: Metformin
Checked: Lisinopril
Found high-risk medication: Warfarin. Stopping search.
```

Once Warfarin is found, the loop stops — Atorvastatin is never checked.

#### `continue` — Skip the current iteration

`continue` skips the rest of the current loop body and jumps to the next iteration. Use it to skip items that don't meet a condition.

```python
medication_entries = [
    {"name": "Metformin", "dose_mg": 500},
    {"name": "Aspirin", "dose_mg": None},
    {"name": "Lisinopril", "dose_mg": 10},
]

for entry in medication_entries:
    if entry["dose_mg"] is None:
        print(f"Skipping {entry['name']}: no dose information available.")
        continue
    print(f"Dispensing {entry['name']}: {entry['dose_mg']} mg")
```

Output:
```
Dispensing Metformin: 500 mg
Skipping Aspirin: no dose information available.
Dispensing Lisinopril: 10 mg
```

#### `pass` — Do nothing (placeholder)

`pass` is a no-op — it does nothing. It's useful as a placeholder when you need a syntactically valid block but haven't written the logic yet.

```python
medications = ["Metformin", "Lisinopril", "Warfarin"]

for drug in medications:
    if drug == "Warfarin":
        pass  # TODO: add interaction check later
    else:
        print(f"Dispensing: {drug}")
```

Output:
```
Dispensing: Metformin
Dispensing: Lisinopril
```

Warfarin is silently skipped — no error, no output. `pass` is a signal to yourself (and other developers) that this case will be handled later.

---

### Section 8.4: The range() Function

`range()` generates a sequence of integers. It's commonly used with `for` loops when you need to repeat something a specific number of times or work with numeric sequences.

**Three forms:**

| Form | Description | Example |
|------|-------------|---------|
| `range(stop)` | 0 up to (not including) stop | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, stop)` | start up to (not including) stop | `range(1, 6)` → 1, 2, 3, 4, 5 |
| `range(start, stop, step)` | start to stop, incrementing by step | `range(0, 50, 10)` → 0, 10, 20, 30, 40 |

**Generating dose increments:**

```python
# Print dose levels from 100 mg to 500 mg in 100 mg steps
print("Available dose levels:")
for dose in range(100, 600, 100):
    print(f"  {dose} mg")
```

Output:
```
Available dose levels:
  100 mg
  200 mg
  300 mg
  400 mg
  500 mg
```

**Counting refills:**

```python
patient_name = "Sarah Johnson"
total_refills = 5

print(f"Refill schedule for {patient_name}:")
for refill_number in range(1, total_refills + 1):
    print(f"  Refill {refill_number} of {total_refills}")
```

Output:
```
Refill schedule for Sarah Johnson:
  Refill 1 of 5
  Refill 2 of 5
  Refill 3 of 5
  Refill 4 of 5
  Refill 5 of 5
```

**Tip:** `range()` doesn't create a list in memory — it generates numbers on demand, which is efficient for large sequences.

---

### Section 8.5: Nested Loops

A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop. This is useful when your data has multiple levels — for example, a list of patients where each patient has their own list of medications.

```python
patients = [
    {"name": "Sarah Johnson", "medications": ["Metformin", "Lisinopril"]},
    {"name": "James Brown", "medications": ["Atorvastatin", "Aspirin", "Warfarin"]},
]

for patient in patients:
    print(f"Patient: {patient['name']}")
    for drug in patient['medications']:
        print(f"  - {drug}")
```

Output:
```
Patient: Sarah Johnson
  - Metformin
  - Lisinopril
Patient: James Brown
  - Atorvastatin
  - Aspirin
  - Warfarin
```

The outer loop runs twice (once per patient). For each patient, the inner loop runs once per medication. The indentation makes it clear which code belongs to which loop.

**Practical example — checking for high-risk drugs across all patients:**

```python
high_risk_drugs = {"Warfarin", "Methotrexate", "Lithium"}

patients = [
    {"name": "Sarah Johnson", "medications": ["Metformin", "Lisinopril"]},
    {"name": "James Brown", "medications": ["Atorvastatin", "Warfarin"]},
    {"name": "Emily Davis", "medications": ["Methotrexate", "Folic Acid"]},
]

print("High-risk medication alerts:")
for patient in patients:
    for drug in patient["medications"]:
        if drug in high_risk_drugs:
            print(f"  ⚠ {patient['name']} is prescribed {drug} — requires monitoring.")
```

Output:
```
High-risk medication alerts:
  ⚠ James Brown is prescribed Warfarin — requires monitoring.
  ⚠ Emily Davis is prescribed Methotrexate — requires monitoring.
```

---

### Chapter Summary

- A `for` loop iterates over each item in a sequence (list, tuple, string, range, etc.)
- A `while` loop repeats as long as a condition is `True` — always ensure the condition can become `False` to avoid infinite loops
- `break` exits a loop immediately; `continue` skips to the next iteration; `pass` does nothing and acts as a placeholder
- `range(stop)`, `range(start, stop)`, and `range(start, stop, step)` generate integer sequences for use in loops
- Nested loops let you process multi-level data structures, such as iterating over patients and their individual medication lists

---

### Quiz

**1.** What does the following code print?

```python
drugs = ["Aspirin", "Ibuprofen", "Paracetamol"]
for drug in drugs:
    print(drug)
```

a) Prints all three drug names, one per line  
b) Prints only the first drug  
c) Prints the list as a single line  
d) Raises an error  

**2.** A pharmacist wants to keep asking for a dose until the user enters a value greater than 0. Which loop type is most appropriate?

a) `for` loop  
b) `while` loop  
c) Nested loop  
d) `range()` loop  

**3.** What does `break` do inside a loop?

a) Skips the current iteration and moves to the next  
b) Does nothing — it's a placeholder  
c) Exits the loop immediately  
d) Restarts the loop from the beginning  

**4.** What is the output of `list(range(0, 30, 10))`?

a) `[0, 10, 20, 30]`  
b) `[10, 20, 30]`  
c) `[0, 10, 20]`  
d) `[0, 30, 10]`  

**5.** A loop is checking a list of medications for a specific drug. When the drug is found, the pharmacist wants to stop checking the rest of the list. Which keyword should be used?

a) `continue`  
b) `pass`  
c) `return`  
d) `break`  

**6.** What does `continue` do inside a loop?

a) Exits the loop entirely  
b) Skips the rest of the current iteration and moves to the next one  
c) Pauses the loop  
d) Repeats the current iteration  

**7.** How many times does the inner loop body run in total?

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

a) 3  
b) 2  
c) 5  
d) 6  

---

**Answer Key**

1. **a** — The `for` loop iterates over each item in the list and prints it on a new line.
2. **b** — A `while` loop is ideal when you don't know in advance how many attempts are needed.
3. **c** — `break` immediately exits the loop, regardless of remaining items.
4. **c** — `range(0, 30, 10)` generates 0, 10, 20 (stops before 30).
5. **d** — `break` stops the loop as soon as the target is found.
6. **b** — `continue` skips the remaining code in the current iteration and jumps to the next one.
7. **d** — The outer loop runs 3 times; for each, the inner loop runs 2 times: 3 × 2 = 6.

---

### Challenge: Dose Safety Flag Report

**Problem:**

Write a program that:

1. Has a list of patients, each with a name, a prescribed dose (in mg), and a maximum safe dose (in mg)
2. Iterates over all patients
3. Flags any patient whose prescribed dose exceeds their maximum safe dose
4. Prints a summary at the end showing how many patients were flagged

**Expected output** (for the sample data below):

```
Dose Safety Report
==================
✓ Sarah Johnson — 500 mg (max: 1000 mg) — OK
⚠ James Brown — 850 mg (max: 800 mg) — EXCEEDS SAFE DOSE
✓ Emily Davis — 200 mg (max: 400 mg) — OK
⚠ Robert Wilson — 1200 mg (max: 1000 mg) — EXCEEDS SAFE DOSE
✓ Linda Martinez — 75 mg (max: 100 mg) — OK

Summary: 2 patient(s) flagged for dose review.
```

**Reference Solution:**

```python
patients = [
    {"name": "Sarah Johnson",  "dose_mg": 500,  "max_safe_mg": 1000},
    {"name": "James Brown",    "dose_mg": 850,  "max_safe_mg": 800},
    {"name": "Emily Davis",    "dose_mg": 200,  "max_safe_mg": 400},
    {"name": "Robert Wilson",  "dose_mg": 1200, "max_safe_mg": 1000},
    {"name": "Linda Martinez", "dose_mg": 75,   "max_safe_mg": 100},
]

flagged_count = 0

print("Dose Safety Report")
print("==================")

for patient in patients:
    name = patient["name"]
    dose = patient["dose_mg"]
    max_dose = patient["max_safe_mg"]

    if dose > max_dose:
        print(f"⚠ {name} — {dose} mg (max: {max_dose} mg) — EXCEEDS SAFE DOSE")
        flagged_count += 1
    else:
        print(f"✓ {name} — {dose} mg (max: {max_dose} mg) — OK")

print(f"\nSummary: {flagged_count} patient(s) flagged for dose review.")
```

**How it works:**

- The `patients` list holds one dictionary per patient with three keys: `name`, `dose_mg`, and `max_safe_mg`
- The `for` loop iterates over every patient
- Inside the loop, an `if` statement compares the prescribed dose to the maximum safe dose
- If the dose exceeds the limit, the patient is flagged and `flagged_count` is incremented
- After the loop, the summary line reports the total number of flagged patients

**Try extending it:**

- Add a `continue` to skip patients with a `None` dose (missing data)
- Use `break` to stop processing after finding the first flagged patient
- Sort the output so flagged patients appear first


---

## Chapter 9: Functions

### Learning Objectives

By the end of this chapter, you will be able to:

- Define and call your own functions using the `def` keyword
- Use parameters and return values to make functions flexible and reusable
- Set default parameter values and use keyword arguments
- Understand the difference between local and global variable scope
- Write docstrings to document your functions
- Distinguish between pure functions and functions with side effects

---

### Section 9.1: Defining and Calling Functions

A **function** is a reusable block of code that performs a specific task. Instead of writing the same calculation over and over, you define it once and call it whenever you need it. Think of a function like a standard operating procedure (SOP) in a pharmacy — you write the steps once, and any staff member can follow them repeatedly.

#### The `def` Keyword

You define a function with the `def` keyword, followed by the function name, parentheses (which may contain **parameters**), and a colon. The indented block below is the function body.

```python
def function_name(parameter1, parameter2):
    # function body
    return result
```

#### Your First Pharmacy Function

```python
# --- Pharmacy Example: dose calculation function ---
# Context: Calculate the total dose for a patient based on weight.

def calculate_dose(weight_kg, dose_per_kg):
    """Calculate total dose based on patient weight."""
    return weight_kg * dose_per_kg

total = calculate_dose(68.0, 2.5)
print(f"Total dose: {total} mg")
# Output: Total dose: 170.0 mg
```

**Breaking it down:**

- `def calculate_dose(weight_kg, dose_per_kg):` — defines the function with two parameters
- `return weight_kg * dose_per_kg` — computes the result and sends it back to the caller
- `calculate_dose(68.0, 2.5)` — **calls** the function, passing `68.0` and `2.5` as **arguments**

#### Parameters vs. Arguments

These two words are often confused:

| Term | Where it appears | Example |
|---|---|---|
| **Parameter** | In the function *definition* | `def calculate_dose(weight_kg, dose_per_kg):` |
| **Argument** | In the function *call* | `calculate_dose(68.0, 2.5)` |

Parameters are the placeholders; arguments are the actual values you pass in.

#### Functions Without a Return Value

A function doesn't have to return anything. It can simply perform an action:

```python
# --- Pharmacy Example: print a medication label ---
# Context: Display a formatted label for a dispensed medication.

def print_label(patient_name, drug_name, dose_mg):
    """Print a simple medication label."""
    print(f"Patient : {patient_name}")
    print(f"Drug    : {drug_name}")
    print(f"Dose    : {dose_mg} mg")
    print("-" * 30)

print_label("Sarah Johnson", "Metformin", 500)
# Output:
# Patient : Sarah Johnson
# Drug    : Metformin
# Dose    : 500 mg
# ------------------------------
```

When a function has no `return` statement, Python returns `None` automatically.

---

### Section 9.2: Default Parameters and Keyword Arguments

#### Default Parameter Values

You can give a parameter a **default value**. If the caller doesn't supply that argument, the default is used. This is handy for common pharmacy scenarios where one value rarely changes.

```python
# --- Pharmacy Example: dose calculation with defaults ---
# Context: Most oral doses use 2.5 mg/kg; IV doses are specified explicitly.

def calculate_dose(weight_kg, dose_per_kg=2.5, route="oral"):
    """Calculate total dose; defaults to 2.5 mg/kg oral route."""
    total = weight_kg * dose_per_kg
    return f"{total} mg ({route})"

# Using defaults
print(calculate_dose(68.0))
# Output: 170.0 mg (oral)

# Overriding the default route
print(calculate_dose(68.0, 3.0, "IV"))
# Output: 204.0 mg (IV)
```

**Rule:** Parameters with defaults must come *after* parameters without defaults in the function signature.

#### Keyword Arguments

When calling a function, you can name the arguments explicitly. This makes the call self-documenting and lets you supply arguments in any order.

```python
# --- Pharmacy Example: keyword arguments ---
# Context: Clearly specify which value is weight and which is dose rate.

print(calculate_dose(weight_kg=68.0, route="IV", dose_per_kg=3.0))
# Output: 204.0 mg (IV)
```

Mixing positional and keyword arguments is allowed, but positional arguments must come first:

```python
print(calculate_dose(68.0, route="IV"))   # OK — weight positional, route keyword
# Output: 170.0 mg (IV)
```

---

### Section 9.3: Variable Scope

**Scope** determines where in your program a variable can be seen and used.

#### Local Scope

A variable created *inside* a function is **local** — it only exists while the function is running and cannot be accessed from outside.

```python
# --- Pharmacy Example: local variable scope ---
# Context: The calculated dose is a local variable inside the function.

def calculate_dose(weight_kg, dose_per_kg):
    total_dose = weight_kg * dose_per_kg   # local variable
    return total_dose

result = calculate_dose(68.0, 2.5)
print(result)          # 170.0  — works fine
# print(total_dose)    # NameError: name 'total_dose' is not defined
```

`total_dose` lives only inside `calculate_dose`. Once the function returns, it's gone.

#### Global Scope

A variable created *outside* all functions is **global** — it can be read from anywhere in the file.

```python
# --- Pharmacy Example: global variable ---
# Context: The pharmacy's maximum safe dose is a constant used across functions.

MAX_DAILY_DOSE_MG = 3000   # global constant

def is_dose_safe(prescribed_mg):
    """Return True if the prescribed dose is within the safe limit."""
    return prescribed_mg <= MAX_DAILY_DOSE_MG

print(is_dose_safe(2500))   # True
print(is_dose_safe(3500))   # False
```

#### Why Avoid Modifying Global Variables

Reading a global is fine. *Modifying* a global from inside a function is risky — it creates hidden dependencies that make code hard to test and debug. Prefer passing values as arguments and returning results.

```python
# Risky pattern — avoid this
dispensed_count = 0

def dispense_medication():
    global dispensed_count          # explicitly declares intent to modify global
    dispensed_count += 1            # modifies global state — hard to track

# Better pattern — return the new value instead
def dispense_medication(current_count):
    return current_count + 1

dispensed_count = dispense_medication(dispensed_count)
```

In a pharmacy system, hidden state changes can lead to incorrect counts or audit failures. Keep functions self-contained.

---

### Section 9.4: Docstrings

A **docstring** is a triple-quoted string placed at the very start of a function body. It describes what the function does, its parameters, and what it returns. Python stores it in the function's `__doc__` attribute, and tools like `help()` display it automatically.

```python
# --- Pharmacy Example: well-documented function ---
# Context: A creatinine clearance estimator with full documentation.

def calculate_creatinine_clearance(age, weight_kg, serum_creatinine, is_female):
    """
    Estimate creatinine clearance using the Cockcroft-Gault formula.

    Parameters
    ----------
    age : int
        Patient age in years.
    weight_kg : float
        Patient weight in kilograms.
    serum_creatinine : float
        Serum creatinine level in mg/dL.
    is_female : bool
        True if the patient is female (applies 0.85 correction factor).

    Returns
    -------
    float
        Estimated creatinine clearance in mL/min.
    """
    clearance = ((140 - age) * weight_kg) / (72 * serum_creatinine)
    if is_female:
        clearance *= 0.85
    return round(clearance, 2)

# Access the docstring
help(calculate_creatinine_clearance)
```

#### Why Docstrings Matter in Pharmacy

In a clinical or regulatory context, undocumented code is a liability:

- **Safety**: A colleague reading your dose calculator needs to know the expected units (mg/kg? mcg/kg?).
- **Auditability**: Regulatory bodies (FDA, ASHP) may review software used in clinical decisions. Documentation is evidence of intent.
- **Maintenance**: Pharmacy workflows change. A clear docstring tells the next developer what the function was designed to do.

Write docstrings as if the reader is a pharmacist who has never seen Python before.

---

### Section 9.5: Pure Functions and Side Effects

#### Pure Functions

A **pure function** always produces the same output for the same input and does not change anything outside itself. It has no **side effects**.

```python
# --- Pharmacy Example: pure function ---
# Context: Calculating a dose is deterministic — same inputs, same result, every time.

def calculate_dose(weight_kg, dose_per_kg):
    """Pure function: no side effects, deterministic output."""
    return weight_kg * dose_per_kg

# Always returns 170.0 for these inputs — no matter when or how many times called
print(calculate_dose(68.0, 2.5))   # 170.0
print(calculate_dose(68.0, 2.5))   # 170.0
```

#### Side Effects

A **side effect** is anything a function does beyond computing a return value — printing to the screen, writing to a file, modifying a global variable, or changing a list passed in.

```python
# --- Pharmacy Example: function with side effects ---
# Context: Logging a dispensing event writes to an external log — a side effect.

dispensing_log = []   # global list

def dispense_and_log(drug_name, dose_mg):
    """Dispenses a drug and logs the event — has a side effect."""
    dispensing_log.append(f"Dispensed {dose_mg} mg of {drug_name}")   # side effect
    return dose_mg

dispense_and_log("Amoxicillin", 500)
print(dispensing_log)
# Output: ['Dispensed 500 mg of Amoxicillin']
```

#### The Pharmacy Analogy

Think of a **pure function** like a dose calculation written on a prescription pad:

- You give it a weight and a dose rate.
- It gives you a number.
- It doesn't call the patient, update the chart, or change the stock level.
- Run the same calculation a hundred times — you always get the same answer.

A function with **side effects** is like the act of dispensing the medication — it changes the real world (stock decreases, a label is printed, a log entry is created). Both types of functions are necessary, but keeping them separate makes your code easier to test and reason about.

**Best practice:** Write your *calculations* as pure functions and isolate your *actions* (logging, file writes, UI updates) in separate functions.

---

### Chapter Summary

- A **function** is defined with `def`, accepts **parameters**, and can `return` a value.
- **Parameters** appear in the definition; **arguments** are the values passed at the call site.
- **Default parameters** let callers omit arguments that rarely change; **keyword arguments** make calls self-documenting.
- **Local variables** exist only inside the function; **global variables** are visible everywhere but should not be modified inside functions.
- **Docstrings** (triple-quoted strings at the top of a function) document purpose, parameters, and return values — essential in a clinical context.
- **Pure functions** are deterministic and side-effect-free, like a dose calculation; functions with **side effects** change external state, like dispensing a medication.

---

### Quiz

**1.** What keyword is used to define a function in Python?

a) `function`
b) `def`
c) `define`
d) `func`

**2.** What is the difference between a *parameter* and an *argument*?

a) They are the same thing — the terms are interchangeable.
b) A parameter is the value passed at the call site; an argument is the placeholder in the definition.
c) A parameter is the placeholder in the function definition; an argument is the actual value passed when calling the function.
d) Parameters are only used with default values.

**3.** Given the function below, what does it print?

```python
def calculate_dose(weight_kg, dose_per_kg=2.0):
    return weight_kg * dose_per_kg

print(calculate_dose(70.0))
```

a) `0.0`
b) `140.0`
c) `72.0`
d) `TypeError`

**4.** A pharmacist writes the following code. What is the value of `total_dose` after the function call?

```python
def compute(weight, rate):
    result = weight * rate
    return result

total_dose = compute(60.0, 3.0)
```

a) `None`
b) `63.0`
c) `180.0`
d) `NameError`

**5.** Which of the following is a **side effect**?

a) Returning a calculated dose from a function.
b) Appending a dispensing event to a global log list inside a function.
c) Multiplying two numbers inside a function.
d) Accepting a parameter named `weight_kg`.

**6.** Why should global variables be modified sparingly inside functions?

a) Python does not allow it.
b) It makes the function run slower.
c) It creates hidden dependencies that make code hard to test and debug.
d) Global variables are automatically deleted when a function runs.

**7.** What does the following docstring describe?

```python
def flag_high_dose(dose_mg, threshold_mg=1000):
    """Return True if dose_mg exceeds the safety threshold."""
    return dose_mg > threshold_mg
```

a) A function that raises an exception when the dose is too high.
b) A function that prints a warning message.
c) A function that returns a boolean indicating whether the dose exceeds a threshold.
d) A function that modifies the global dose variable.

---

#### Answer Key

1. **b) `def`** — Python uses `def` to define functions.
2. **c)** — Parameters are the placeholders in the definition; arguments are the concrete values supplied at the call site.
3. **b) `140.0`** — `70.0 * 2.0 = 140.0`. The default `dose_per_kg=2.0` is used because no second argument was provided.
4. **c) `180.0`** — `60.0 * 3.0 = 180.0`. The function returns the result, which is assigned to `total_dose`.
5. **b)** — Modifying a global list inside a function is a side effect because it changes state outside the function.
6. **c)** — Hidden state changes make functions harder to test in isolation and can cause subtle bugs in larger programs.
7. **c)** — The docstring clearly states the function returns `True` if the dose exceeds the threshold.

---

### Challenge

**Problem:** Write a pharmacy utility module containing three functions that a clinical pharmacist might use daily. Use Sarah Johnson's data to demonstrate all three.

**Patient data:**

```
Name            : Sarah Johnson
Age             : 45 years
Weight          : 68.0 kg
Height          : 1.65 m
Serum creatinine: 0.9 mg/dL
Sex             : Female
```

**Tasks:**

1. Write `calculate_dose(weight_kg, dose_per_kg)` — returns the total dose in mg.
2. Write `calculate_bmi(weight_kg, height_m)` — returns the Body Mass Index (BMI).
3. Write `calculate_creatinine_clearance(age, weight_kg, serum_creatinine, is_female)` — returns estimated creatinine clearance (mL/min) using the Cockcroft-Gault formula.

Each function must have a docstring. Call all three functions with Sarah's data and print the results.

**Expected output:**

```
Dose (2.5 mg/kg): 170.0 mg
BMI             : 24.98
CrCl (Cockcroft-Gault): 84.74 mL/min
```

**Reference solution:**

```python
# --- Pharmacy Challenge: utility function module ---
# Context: Three reusable clinical calculation functions for Sarah Johnson.

def calculate_dose(weight_kg, dose_per_kg):
    """
    Calculate total dose based on patient weight.

    Parameters
    ----------
    weight_kg : float
        Patient weight in kilograms.
    dose_per_kg : float
        Prescribed dose in mg per kg of body weight.

    Returns
    -------
    float
        Total dose in milligrams.
    """
    return weight_kg * dose_per_kg


def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters
    ----------
    weight_kg : float
        Patient weight in kilograms.
    height_m : float
        Patient height in metres.

    Returns
    -------
    float
        BMI rounded to two decimal places.
    """
    return round(weight_kg / (height_m ** 2), 2)


def calculate_creatinine_clearance(age, weight_kg, serum_creatinine, is_female):
    """
    Estimate creatinine clearance using the Cockcroft-Gault formula.

    Parameters
    ----------
    age : int
        Patient age in years.
    weight_kg : float
        Patient weight in kilograms.
    serum_creatinine : float
        Serum creatinine in mg/dL.
    is_female : bool
        True if the patient is female (applies 0.85 sex correction factor).

    Returns
    -------
    float
        Estimated creatinine clearance in mL/min, rounded to two decimal places.
    """
    clearance = ((140 - age) * weight_kg) / (72 * serum_creatinine)
    if is_female:
        clearance *= 0.85
    return round(clearance, 2)


# --- Sarah Johnson's data ---
name             = "Sarah Johnson"
age              = 45
weight_kg        = 68.0
height_m         = 1.65
serum_creatinine = 0.9
is_female        = True
dose_per_kg      = 2.5

# Call all three functions
dose   = calculate_dose(weight_kg, dose_per_kg)
bmi    = calculate_bmi(weight_kg, height_m)
crcl   = calculate_creatinine_clearance(age, weight_kg, serum_creatinine, is_female)

print(f"Dose (2.5 mg/kg): {dose} mg")
print(f"BMI             : {bmi}")
print(f"CrCl (Cockcroft-Gault): {crcl} mL/min")
```


---

## Chapter 10: File Handling

So far, every program you have written stores data only while it is running. The moment the script ends, all your variables disappear. File handling lets you save data permanently — to a text file, a CSV, or any other format — and load it back later. For pharmacists, this is essential: patient records, prescription logs, and dose reports all need to persist between sessions.

---

### Learning Objectives

By the end of this chapter you will be able to:

- Open, read, write, and close files using Python's built-in `open()` function
- Use the `with` statement to manage files safely and automatically
- Read a CSV-like text file of patient records and parse each line into fields
- Write prescription records to a text file, both overwriting and appending
- Use the `csv` module to read and write properly formatted CSV files
- Recognise a `FileNotFoundError` and handle it gracefully with `try/except`

---

### Section 10.1: Opening, Reading, Writing, and Closing Files

#### The `open()` Function and File Modes

Python's built-in `open()` function gives you access to a file on disk. Its two most important arguments are the file path and the **mode**:

| Mode | Meaning |
|------|---------|
| `"r"` | **Read** — open an existing file for reading (default). Raises `FileNotFoundError` if the file does not exist. |
| `"w"` | **Write** — create a new file (or overwrite an existing one) for writing. |
| `"a"` | **Append** — open a file for writing, but add new content at the end instead of overwriting. Creates the file if it does not exist. |

```python
# Open a file for reading
f = open("prescription.txt", "r")
content = f.read()
f.close()   # Always close the file when you are done!
```

Forgetting to call `f.close()` can leave the file locked or cause data loss. Python provides a cleaner way to handle this automatically.

#### The `with` Statement (Context Manager)

The `with` statement opens a file, runs your code block, and **automatically closes the file** when the block ends — even if an error occurs. This is the recommended way to work with files in Python.

```python
with open("prescription.txt", "r") as f:
    content = f.read()
# File is automatically closed here — no f.close() needed
```

Think of `with` like a dispensing cabinet that locks itself when you walk away. You don't have to remember to lock it; the system handles it for you.

#### Writing a Prescription Record to a Text File

```python
with open("prescription.txt", "w") as f:
    f.write("Patient: Sarah Johnson\n")
    f.write("Drug: Amoxicillin 500 mg\n")
    f.write("Directions: Take 1 capsule three times daily for 10 days\n")

print("Prescription saved.")
```

`\n` is the **newline character** — it moves the cursor to the next line, just like pressing Enter.

> **Note:** Mode `"w"` overwrites the file completely each time. If `prescription.txt` already existed, its previous contents are gone.

#### Reading the File Back

```python
with open("prescription.txt", "r") as f:
    content = f.read()
    print(content)
```

**Output:**
```
Patient: Sarah Johnson
Drug: Amoxicillin 500 mg
Directions: Take 1 capsule three times daily for 10 days
```

#### Reading Line by Line

For large files it is more memory-efficient to read one line at a time using a `for` loop:

```python
with open("prescription.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline
```

`line.strip()` trims any leading or trailing whitespace (including `\n`) from each line — a habit worth forming when parsing files.

---

### Section 10.2: Reading a CSV-like Text File

A common pharmacy task is loading patient records stored in a plain-text file where each line represents one patient and fields are separated by a delimiter such as a comma or pipe (`|`).

#### Sample File: `patient_records.txt`

```
name|drug|dose_mg|frequency
Sarah Johnson|Amoxicillin|500|three times daily
David Lee|Metformin|1000|twice daily
Maria Garcia|Lisinopril|10|once daily
James Patel|Atorvastatin|40|once daily at bedtime
```

The first line is a **header** that names each field. The remaining lines are data rows.

#### Reading and Parsing the File

```python
with open("patient_records.txt", "r") as f:
    lines = f.readlines()   # Read all lines into a list

# The first line is the header — skip it
header = lines[0].strip()
print(f"Columns: {header}\n")

# Process each data row
for line in lines[1:]:
    line = line.strip()          # Remove trailing newline
    if line:                     # Skip any blank lines
        fields = line.split("|") # Split on the pipe delimiter
        name      = fields[0]
        drug      = fields[1]
        dose_mg   = int(fields[2])
        frequency = fields[3]
        print(f"{name} takes {dose_mg} mg of {drug} {frequency}.")
```

**Output:**
```
Columns: name|drug|dose_mg|frequency

Sarah Johnson takes 500 mg of Amoxicillin three times daily.
David Lee takes 1000 mg of Metformin twice daily.
Maria Garcia takes 10 mg of Lisinopril once daily.
James Patel takes 40 mg of Atorvastatin once daily at bedtime.
```

Key points:
- `f.readlines()` returns a list where each element is one line (including `\n`).
- `line.split("|")` splits the string at every pipe and returns a list of fields.
- `int(fields[2])` converts the dose string to an integer so you can do arithmetic with it.

---

### Section 10.3: Writing Prescription Records to a File

#### Writing Multiple Records with a Loop

```python
prescriptions = [
    ("Sarah Johnson", "Amoxicillin 500 mg", "Take 1 capsule three times daily for 10 days"),
    ("David Lee",     "Metformin 1000 mg",  "Take 1 tablet twice daily with meals"),
    ("Maria Garcia",  "Lisinopril 10 mg",   "Take 1 tablet once daily"),
]

with open("prescriptions.txt", "w") as f:
    for name, drug, directions in prescriptions:
        f.write(f"Patient: {name}\n")
        f.write(f"Drug: {drug}\n")
        f.write(f"Directions: {directions}\n")
        f.write("-" * 40 + "\n")

print("All prescriptions written to prescriptions.txt")
```

#### Appending to an Existing File

Use mode `"a"` when you want to add new records without erasing what is already there:

```python
new_prescription = ("James Patel", "Atorvastatin 40 mg", "Take 1 tablet once daily at bedtime")

with open("prescriptions.txt", "a") as f:
    name, drug, directions = new_prescription
    f.write(f"Patient: {name}\n")
    f.write(f"Drug: {drug}\n")
    f.write(f"Directions: {directions}\n")
    f.write("-" * 40 + "\n")

print("New prescription appended.")
```

> **Tip:** Think of `"w"` as starting a fresh prescription pad, and `"a"` as adding a new sheet to an existing pad.

---

### Section 10.4: The `csv` Module

Plain text files with manual splitting work fine for simple cases, but they break down when field values contain the delimiter character (e.g., a drug name with a comma). Python's built-in `csv` module handles all of this correctly.

#### Reading a CSV File with `csv.reader`

Suppose you have a file called `patients.csv`:

```
name,drug,dose_mg,max_dose_mg
Sarah Johnson,Amoxicillin,500,1500
David Lee,Metformin,1000,2000
Maria Garcia,Lisinopril,10,40
James Patel,Atorvastatin,40,80
```

```python
import csv

with open("patients.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # Read and skip the header row
    print(f"Headers: {header}\n")

    for row in reader:
        name        = row[0]
        drug        = row[1]
        dose_mg     = int(row[2])
        max_dose_mg = int(row[3])
        print(f"{name}: {dose_mg} mg of {drug} (max {max_dose_mg} mg)")
```

**Output:**
```
Headers: ['name', 'drug', 'dose_mg', 'max_dose_mg']

Sarah Johnson: 500 mg of Amoxicillin (max 1500 mg)
David Lee: 1000 mg of Metformin (max 2000 mg)
Maria Garcia: 10 mg of Lisinopril (max 40 mg)
James Patel: 40 mg of Atorvastatin (max 80 mg)
```

> Always pass `newline=""` when opening a CSV file — this prevents the `csv` module from mishandling line endings on Windows.

#### Writing a CSV File with `csv.writer`

```python
import csv

patients = [
    ["name", "drug", "dose_mg", "max_dose_mg"],   # header row
    ["Sarah Johnson", "Amoxicillin", 500, 1500],
    ["David Lee",     "Metformin",   1000, 2000],
    ["Maria Garcia",  "Lisinopril",  10,   40],
    ["James Patel",   "Atorvastatin", 40,  80],
]

with open("patients_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(patients)   # Write all rows at once

print("patients_output.csv created.")
```

#### A Complete Example: Read, Process, Write

```python
import csv

# Read patient data
with open("patients.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    records = list(reader)

# Add a "status" column based on dose vs. max dose
results = [header + ["status"]]

for row in records:
    name        = row[0]
    drug        = row[1]
    dose_mg     = int(row[2])
    max_dose_mg = int(row[3])
    status = "OVER LIMIT" if dose_mg > max_dose_mg else "OK"
    results.append(row + [status])

# Write the enriched data to a new CSV
with open("patients_reviewed.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

print("Review complete. Results saved to patients_reviewed.csv.")
```

---

### Section 10.5: FileNotFoundError

When you open a file for reading with mode `"r"` and the file does not exist, Python raises a `FileNotFoundError`:

```python
with open("missing_file.txt", "r") as f:
    content = f.read()
```

**Error output:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'missing_file.txt'
```

This is Python's way of saying: "I looked for that file and it simply isn't there."

#### Handling the Error with `try/except`

You can catch this error and respond gracefully instead of crashing:

```python
filename = "patient_records.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Error: '{filename}' was not found. Please check the file path.")
```

If the file exists, the program reads and prints it normally. If it does not exist, the program prints a helpful message and continues running — no crash.

> Full error handling (multiple exception types, `else`, `finally`) is covered in **Chapter 11**. For now, the key takeaway is: wrap file-open calls in `try/except FileNotFoundError` whenever the file might not exist.

---

### Chapter Summary

- `open(filename, mode)` opens a file; modes `"r"`, `"w"`, and `"a"` control whether you read, overwrite, or append.
- The `with` statement is the safest way to open files — it closes the file automatically when the block ends.
- `f.read()` reads the entire file as a string; `f.readlines()` returns a list of lines; iterating `for line in f` reads one line at a time.
- `f.write(text)` writes a string to the file; use `\n` to add line breaks.
- `line.split(delimiter)` parses a delimited line into a list of fields.
- The `csv` module handles comma-separated files correctly, including fields that contain commas.
- `csv.reader` iterates over rows as lists; `csv.writer` writes lists as rows.
- `FileNotFoundError` is raised when you try to read a file that does not exist; catch it with `try/except`.

---

### Quiz

**Question 1**
Which file mode should you use to add new records to an existing file without erasing its current contents?

- A) `"r"`
- B) `"w"`
- C) `"a"`
- D) `"x"`

**Question 2**
What is the main advantage of using the `with` statement when opening a file?

- A) It makes the file read faster
- B) It automatically closes the file when the block ends, even if an error occurs
- C) It converts the file to CSV format automatically
- D) It prevents other programs from reading the file

**Question 3**
You have a line from a pipe-separated file: `"Maria Garcia|Lisinopril|10|once daily"`. Which expression gives you the drug name `"Lisinopril"`?

- A) `line.split("|")[0]`
- B) `line.split("|")[1]`
- C) `line.split(",")[1]`
- D) `line[1]`

**Question 4**
What does `next(reader)` do when `reader` is a `csv.reader` object?

- A) Closes the CSV file
- B) Reads and returns the next row, advancing the reader past it
- C) Resets the reader to the beginning of the file
- D) Counts the total number of rows

**Question 5**
A pharmacist runs the following code but the file `doses.csv` does not exist on disk. What happens?

```python
with open("doses.csv", "r") as f:
    data = f.read()
```

- A) Python creates an empty `doses.csv` file
- B) Python returns an empty string
- C) Python raises a `FileNotFoundError`
- D) Python raises a `ValueError`

**Question 6**
Which of the following correctly writes the string `"Dose: 500 mg\n"` to a file called `log.txt`?

- A) `open("log.txt").write("Dose: 500 mg\n")`
- B) `with open("log.txt", "w") as f: f.write("Dose: 500 mg\n")`
- C) `with open("log.txt", "r") as f: f.write("Dose: 500 mg\n")`
- D) `with open("log.txt", "a") as f: f.read("Dose: 500 mg\n")`

**Question 7**
Why should you pass `newline=""` when opening a CSV file with the `csv` module?

- A) It speeds up reading large files
- B) It prevents the `csv` module from mishandling line endings across operating systems
- C) It removes blank lines from the output automatically
- D) It is required for the `csv.writer` to add headers

---

#### Answer Key

1. **C** — Mode `"a"` (append) adds content at the end of the file without overwriting existing data.
2. **B** — The `with` statement acts as a context manager that guarantees the file is closed when the block exits, even if an exception is raised.
3. **B** — `line.split("|")` produces `["Maria Garcia", "Lisinopril", "10", "once daily"]`; index `[1]` is `"Lisinopril"`.
4. **B** — `next(reader)` advances the iterator by one row and returns that row, which is commonly used to skip (and optionally capture) the header row.
5. **C** — Opening a non-existent file in read mode raises `FileNotFoundError`.
6. **B** — You must open in write mode `"w"` and call `f.write()` inside the `with` block.
7. **B** — Passing `newline=""` delegates all newline handling to the `csv` module, preventing double newlines on Windows.

---

### Challenge

**Problem:** Write a program that:

1. Reads a CSV file of patient records with columns: `name`, `drug`, `dose_mg`, `max_dose_mg`
2. Filters patients whose `dose_mg` exceeds their `max_dose_mg`
3. Writes the flagged patients to a new file called `flagged_patients.csv` (with a header row)
4. Prints a summary showing how many patients were flagged

---

**Sample Input CSV (`patient_doses.csv`):**

```
name,drug,dose_mg,max_dose_mg
Sarah Johnson,Amoxicillin,500,1500
David Lee,Metformin,2500,2000
Maria Garcia,Lisinopril,10,40
James Patel,Atorvastatin,120,80
Linda Chen,Warfarin,5,10
Robert Kim,Digoxin,0.375,0.25
```

---

**Expected Output (printed to console):**

```
Dose Safety Check Complete
--------------------------
Total patients reviewed : 6
Patients flagged        : 3

Flagged patients written to flagged_patients.csv
```

**Contents of `flagged_patients.csv`:**

```
name,drug,dose_mg,max_dose_mg
David Lee,Metformin,2500,2000
James Patel,Atorvastatin,120,80
Robert Kim,Digoxin,0.375,0.25
```

---

**Reference Solution:**

```python
import csv

# ── Step 1: Create the input CSV file ──────────────────────────────────────
input_data = [
    ["name", "drug", "dose_mg", "max_dose_mg"],
    ["Sarah Johnson",  "Amoxicillin",  "500",   "1500"],
    ["David Lee",      "Metformin",    "2500",  "2000"],
    ["Maria Garcia",   "Lisinopril",   "10",    "40"],
    ["James Patel",    "Atorvastatin", "120",   "80"],
    ["Linda Chen",     "Warfarin",     "5",     "10"],
    ["Robert Kim",     "Digoxin",      "0.375", "0.25"],
]

with open("patient_doses.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(input_data)

# ── Step 2: Read the CSV and filter flagged patients ───────────────────────
flagged = []
total   = 0

with open("patient_doses.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # Skip header row

    for row in reader:
        total += 1
        name        = row[0]
        drug        = row[1]
        dose_mg     = float(row[2])
        max_dose_mg = float(row[3])

        if dose_mg > max_dose_mg:
            flagged.append(row)

# ── Step 3: Write flagged patients to a new CSV ────────────────────────────
with open("flagged_patients.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)      # Write header first
    writer.writerows(flagged)    # Write all flagged rows

# ── Step 4: Print summary ──────────────────────────────────────────────────
print("Dose Safety Check Complete")
print("-" * 26)
print(f"Total patients reviewed : {total}")
print(f"Patients flagged        : {len(flagged)}")
print()
print("Flagged patients written to flagged_patients.csv")
```

**Why `float()` instead of `int()`?**
Robert Kim's Digoxin dose is `0.375` mg — a decimal value. Using `float()` handles both whole-number and decimal doses correctly.

**Key concepts used in this challenge:**
- `csv.reader` to read structured patient data
- `next(reader)` to skip the header row
- `float()` for type conversion of numeric fields
- Conditional filtering with `if dose_mg > max_dose_mg`
- `csv.writer` with `writerow()` (single row) and `writerows()` (multiple rows)
- f-strings for formatted console output


---

## Chapter 11: Error Handling

### Learning Objectives

By the end of this chapter, you will be able to:

- Explain what an exception is and why it occurs at runtime
- Use `try`, `except`, `else`, and `finally` blocks to handle errors gracefully
- Identify and handle common built-in exceptions: `ValueError`, `TypeError`, `FileNotFoundError`, and `ZeroDivisionError`
- Raise exceptions deliberately using `raise` with a custom error message
- Write pharmacy tools that fail safely instead of crashing

---

### Section 11.1: What are Exceptions?

An **exception** is a runtime error — something that goes wrong while your program is actually running, not while Python is reading your code. When an exception occurs and is not handled, Python stops the program immediately and prints an error message (called a **traceback**).

Think of it like a prescription workflow: if a pharmacist receives an illegible prescription, they can't process it. They don't just guess — they stop and ask for clarification. In the same way, Python stops and raises an exception when it encounters something it can't process.

**Pharmacy analogy:** A patient hands you a prescription where the dose field contains the word "lots". Your dispensing system expects a number. It can't convert "lots" to milligrams, so it raises an error rather than dispensing the wrong amount.

Here is a simple example that causes a `ValueError`:

```python
# --- Pharmacy Example: Non-numeric dose input ---
# Context: A patient enters their dose as text instead of a number.

dose_input = "lots"          # This came from a form field
dose_mg = int(dose_input)    # Python cannot convert "lots" to an integer
print(f"Dose: {dose_mg} mg")
```

Running this code produces:

```
ValueError: invalid literal for int() with base 10: 'lots'
```

The program crashes at the `int()` call because `"lots"` is not a valid integer. In the next section you will learn how to catch this error and respond to it gracefully.

---

### Section 11.2: try, except, else, finally

Python gives you four blocks for handling exceptions:

| Block | Purpose |
|-------|---------|
| `try` | Wrap the code that might raise an exception |
| `except` | Runs only if an exception was raised in `try` |
| `else` | Runs only if **no** exception was raised in `try` |
| `finally` | Always runs — use it for cleanup (closing files, logging, etc.) |

The general structure looks like this:

```python
try:
    # code that might fail
except SomeException:
    # handle the failure
else:
    # runs only on success
finally:
    # always runs
```

Here is a complete pharmacy example using all four blocks:

```python
# --- Pharmacy Example: Dose input validation ---
# Context: Validate a dose value entered by a pharmacy technician.

try:
    dose_input = "abc"           # Simulating bad input from a form
    dose_mg = int(dose_input)    # This will raise ValueError
except ValueError:
    print("Invalid dose: please enter a number.")
else:
    print(f"Dose accepted: {dose_mg} mg")
finally:
    print("Dose validation complete.")
```

**Output when dose_input = "abc":**

```
Invalid dose: please enter a number.
Dose validation complete.
```

**Output when dose_input = "500":**

```
Dose accepted: 500 mg
Dose validation complete.
```

Notice that `finally` runs in both cases. This makes it ideal for actions that must always happen — like logging an audit trail or closing a database connection — regardless of whether the dose was valid.

**Catching multiple exception types:**

You can handle different exceptions differently by stacking `except` clauses:

```python
# --- Pharmacy Example: Multiple exception types ---
# Context: Process a dose calculation that could fail in different ways.

try:
    dose_per_tablet = float(input("Enter dose per tablet (mg): "))
    num_tablets = int(input("Enter number of tablets: "))
    total_dose = dose_per_tablet * num_tablets
except ValueError:
    print("Error: please enter numeric values only.")
except ZeroDivisionError:
    print("Error: number of tablets cannot be zero.")
else:
    print(f"Total dose: {total_dose} mg")
finally:
    print("Calculation attempt recorded.")
```

---

### Section 11.3: Common Built-in Exceptions

Python has many built-in exception types. Here are the four you will encounter most often in pharmacy applications.

#### ValueError

Raised when a function receives an argument of the right type but an inappropriate value.

**Pharmacy scenario:** A technician enters `"five hundred"` as a dose in a numeric field.

```python
# --- Pharmacy Example: ValueError ---
# Context: Converting a text dose to a number fails.

dose_input = "five hundred"

try:
    dose_mg = float(dose_input)
except ValueError:
    print(f"Cannot convert '{dose_input}' to a dose. Please enter a number like 500.")
```

**Output:**

```
Cannot convert 'five hundred' to a dose. Please enter a number like 500.
```

---

#### TypeError

Raised when an operation is applied to an object of an inappropriate type.

**Pharmacy scenario:** Trying to concatenate a numeric dose with the string `" mg"` without converting it first.

```python
# --- Pharmacy Example: TypeError ---
# Context: Building a dose label by accidentally mixing types.

dose_mg = 500   # int

try:
    label = dose_mg + " mg"   # Can't add int and str
except TypeError as e:
    print(f"Type error in label generation: {e}")
    label = str(dose_mg) + " mg"   # Correct approach
    print(f"Label fixed: {label}")
```

**Output:**

```
Type error in label generation: unsupported operand type(s) for +: 'int' and 'str'
Label fixed: 500 mg
```

---

#### FileNotFoundError

Raised when Python tries to open a file that does not exist.

**Pharmacy scenario:** Your script tries to load a patient records file that hasn't been created yet or has been moved.

```python
# --- Pharmacy Example: FileNotFoundError ---
# Context: Loading patient records from a file that may not exist.

filename = "patient_records.csv"

try:
    with open(filename, "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the file path.")
    print("Starting with an empty patient list.")
```

**Output (when file is missing):**

```
File 'patient_records.csv' not found. Please check the file path.
Starting with an empty patient list.
```

---

#### ZeroDivisionError

Raised when you divide a number by zero.

**Pharmacy scenario:** Calculating the dose per administration when the number of doses per day is accidentally set to zero.

```python
# --- Pharmacy Example: ZeroDivisionError ---
# Context: Calculating dose per administration from total daily dose.

total_daily_dose_mg = 1500
doses_per_day = 0   # Data entry error

try:
    dose_per_administration = total_daily_dose_mg / doses_per_day
except ZeroDivisionError:
    print("Error: doses per day cannot be zero. Please check the prescription.")
else:
    print(f"Dose per administration: {dose_per_administration} mg")
```

**Output:**

```
Error: doses per day cannot be zero. Please check the prescription.
```

---

### Section 11.4: Raising Exceptions

Sometimes you want to raise an exception yourself — for example, when input passes Python's type check but violates a business rule. You do this with the `raise` keyword.

**Why raise exceptions?** In pharmacy software, a dose of `-50 mg` is technically a valid integer, but it is medically nonsensical. Python won't catch that automatically — you have to enforce it yourself.

```python
# --- Pharmacy Example: Raising a ValueError for invalid dose ---
# Context: A dose validation function that rejects non-positive values.

def validate_dose(dose_mg):
    """
    Validate that a dose is a positive number.

    Args:
        dose_mg (float): The dose in milligrams.

    Returns:
        float: The validated dose.

    Raises:
        ValueError: If dose_mg is zero or negative.
    """
    if dose_mg <= 0:
        raise ValueError(f"Dose must be positive, got {dose_mg} mg")
    return dose_mg
```

Using the function:

```python
# Valid dose
try:
    approved_dose = validate_dose(500)
    print(f"Dose approved: {approved_dose} mg")
except ValueError as e:
    print(f"Validation failed: {e}")

# Invalid dose
try:
    approved_dose = validate_dose(-50)
    print(f"Dose approved: {approved_dose} mg")
except ValueError as e:
    print(f"Validation failed: {e}")
```

**Output:**

```
Dose approved: 500 mg
Validation failed: Dose must be positive, got -50 mg
```

**Raising exceptions in a chain:**

You can also raise exceptions inside `except` blocks to re-raise or wrap them:

```python
# --- Pharmacy Example: Wrapping a low-level error with context ---
# Context: Provide a clearer error message when a file is missing.

def load_patient_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Patient file '{filename}' is missing. "
            "Contact your system administrator."
        )
```

---

### Chapter Summary

- An **exception** is a runtime error that stops program execution if not handled.
- Use `try` to wrap risky code, `except` to handle specific errors, `else` for success-only logic, and `finally` for cleanup that always runs.
- Common exceptions in pharmacy applications: `ValueError` (bad value), `TypeError` (wrong type), `FileNotFoundError` (missing file), `ZeroDivisionError` (division by zero).
- Use `raise` to deliberately trigger an exception when input violates a business rule (e.g., negative dose).
- Good error handling makes pharmacy software robust — it fails safely with a clear message instead of crashing silently or producing wrong results.

---

### Quiz

**Question 1**
A pharmacy technician enters `"250mg"` into a dose field. Your code runs `dose = int("250mg")`. What exception is raised?

A) `TypeError`
B) `ValueError`
C) `SyntaxError`
D) `NameError`

---

**Question 2**
Which block in a `try/except/else/finally` structure is guaranteed to run regardless of whether an exception occurred?

A) `try`
B) `except`
C) `else`
D) `finally`

---

**Question 3**
Your script opens `"prescriptions.csv"` for reading, but the file was accidentally deleted. Which exception will Python raise?

A) `ValueError`
B) `IOError`
C) `FileNotFoundError`
D) `OSError`

---

**Question 4**
A pharmacist's script calculates `dose_per_day / num_administrations`. A data entry error sets `num_administrations = 0`. What exception is raised?

A) `ValueError`
B) `ArithmeticError`
C) `ZeroDivisionError`
D) `OverflowError`

---

**Question 5**
Which of the following correctly raises a `ValueError` when a dose is negative?

A)
```python
if dose_mg < 0:
    print("Invalid dose")
```

B)
```python
if dose_mg < 0:
    raise ValueError("Dose cannot be negative")
```

C)
```python
except ValueError:
    dose_mg = abs(dose_mg)
```

D)
```python
try:
    dose_mg = -50
```

---

**Question 6**
What is the difference between the `else` block and the `finally` block in a `try` statement?

A) `else` runs when an exception occurs; `finally` runs when no exception occurs
B) `else` runs only when no exception occurs; `finally` always runs
C) Both run only when an exception occurs
D) Both always run

---

**Question 7**
A function receives `dose_mg = "500"` (a string) and tries to compute `dose_mg * 2`. What exception is raised?

A) `ValueError`
B) `TypeError`
C) No exception — Python will return `"500500"`
D) `AttributeError`

---

#### Answer Key

1. **B — ValueError.** `int()` raises `ValueError` when the string contains non-numeric characters like `"mg"`.
2. **D — finally.** The `finally` block always executes, making it ideal for cleanup operations.
3. **C — FileNotFoundError.** Python raises this specific exception when `open()` cannot locate the file.
4. **C — ZeroDivisionError.** Dividing any number by zero raises this exception.
5. **B.** Using `raise ValueError(...)` deliberately triggers the exception with a descriptive message.
6. **B.** `else` runs only on success (no exception); `finally` always runs regardless of outcome.
7. **C — No exception.** Python's `*` operator on a string and int repeats the string: `"500" * 2 = "500500"`. This is a logic bug, not a runtime error — which is why explicit type validation matters.

---

### Challenge

**Building on:** The `calculate_dose()` function from Chapter 9.

**Problem:** Add robust error handling to the dose calculator from Chapter 9. The updated function should handle three failure modes gracefully:

1. Non-numeric input (e.g., the user types `"abc"` for the dose)
2. Negative dose (e.g., `-100` mg)
3. Zero patient weight (which would cause a division by zero in weight-based dosing)

**Requirements:**
- Use `try/except/else/finally`
- Use `raise` for business-rule validation (negative dose, zero weight)
- Print a clear, pharmacy-appropriate error message for each failure mode
- The `finally` block should always print `"Dose calculation attempt logged."`

**Expected output — successful case:**

```
Dose calculation attempt logged.
Weight-based dose: 340.0 mg
```

**Expected output — non-numeric input:**

```
Invalid input: please enter numeric values only.
Dose calculation attempt logged.
```

**Expected output — negative dose:**

```
Validation error: Dose per kg must be positive, got -5 mg/kg
Dose calculation attempt logged.
```

**Expected output — zero weight:**

```
Validation error: Patient weight must be greater than zero, got 0 kg
Dose calculation attempt logged.
```

**Reference solution:**

```python
# --- Pharmacy Challenge: Robust dose calculator with error handling ---
# Context: A weight-based dose calculator that handles bad input gracefully.

def calculate_weight_based_dose(dose_per_kg_input, weight_kg_input):
    """
    Calculate a weight-based dose with full error handling.

    Args:
        dose_per_kg_input: Dose per kilogram (may be a string from user input).
        weight_kg_input:   Patient weight in kg (may be a string from user input).

    Returns:
        float: Total dose in mg, or None if calculation failed.
    """
    total_dose = None

    try:
        # Step 1: Convert inputs to numbers (raises ValueError if non-numeric)
        dose_per_kg = float(dose_per_kg_input)
        weight_kg = float(weight_kg_input)

        # Step 2: Validate business rules (raises ValueError for bad values)
        if dose_per_kg <= 0:
            raise ValueError(f"Dose per kg must be positive, got {dose_per_kg} mg/kg")
        if weight_kg <= 0:
            raise ValueError(f"Patient weight must be greater than zero, got {weight_kg} kg")

        # Step 3: Perform the calculation
        total_dose = dose_per_kg * weight_kg

    except ValueError as e:
        # Distinguish between type-conversion errors and our custom raises
        if "could not convert" in str(e) or "invalid literal" in str(e):
            print("Invalid input: please enter numeric values only.")
        else:
            print(f"Validation error: {e}")

    else:
        print(f"Weight-based dose: {total_dose} mg")

    finally:
        print("Dose calculation attempt logged.")

    return total_dose


# --- Test all four scenarios ---

print("=== Scenario 1: Valid input ===")
calculate_weight_based_dose(5, 68)

print()
print("=== Scenario 2: Non-numeric dose ===")
calculate_weight_based_dose("abc", 68)

print()
print("=== Scenario 3: Negative dose per kg ===")
calculate_weight_based_dose(-5, 68)

print()
print("=== Scenario 4: Zero patient weight ===")
calculate_weight_based_dose(5, 0)
```

**Full expected output:**

```
=== Scenario 1: Valid input ===
Weight-based dose: 340.0 mg
Dose calculation attempt logged.

=== Scenario 2: Non-numeric dose ===
Invalid input: please enter numeric values only.
Dose calculation attempt logged.

=== Scenario 3: Negative dose per kg ===
Validation error: Dose per kg must be positive, got -5.0 mg/kg
Dose calculation attempt logged.

=== Scenario 4: Zero patient weight ===
Validation error: Patient weight must be greater than zero, got 0.0 kg
Dose calculation attempt logged.
```


---

## Mini-Project 1: Medication Tracker

**Overview:** Build a command-line tool to add, remove, and display a patient's current medications.

**Concepts used:** variables, lists, dictionaries, loops, conditionals, functions

---

### Problem Statement

A pharmacist needs a simple tool to manage a patient's current medication list. The tool should allow:

- Viewing the current medication list
- Adding a new medication (with drug name, dose, and frequency)
- Removing a discontinued medication
- Displaying a formatted summary

---

### Step-by-Step Guided Implementation

We'll build this project in four steps, each adding one piece of functionality.

#### Step 1: Define the Data Structure

We'll store medications as a **list of dictionaries**. Each dictionary represents one medication entry with three keys: `drug`, `dose_mg`, and `frequency`.

```python
# A list to hold all current medications
medications = []

# Each medication is a dictionary
# Example entry:
# {"drug": "Metformin", "dose_mg": 500, "frequency": "twice daily"}
```

Why a list of dictionaries? A list keeps the medications ordered and lets us add or remove entries easily. A dictionary for each entry lets us label each piece of data (drug name, dose, frequency) so we never mix them up.

#### Step 2: Write the `display_medications()` Function

This function takes the patient's name and the medication list, then prints a formatted summary. It uses a `for` loop to iterate over the list and an `if` conditional to handle the empty-list case.

```python
def display_medications(patient_name, medications):
    """Display all current medications for a patient."""
    print(f"\n=== Medication List: {patient_name} ===")
    if not medications:
        print("  No medications on file.")
    else:
        for i, med in enumerate(medications, 1):
            print(f"  {i}. {med['drug']} — {med['dose_mg']} mg — {med['frequency']}")
    print("=" * 40)
```

Key points:
- `if not medications` is `True` when the list is empty — a clean Pythonic check.
- `enumerate(medications, 1)` gives us a counter starting at 1 so the list is numbered naturally.
- `med['drug']`, `med['dose_mg']`, and `med['frequency']` pull values from each dictionary.

#### Step 3: Write the `add_medication()` Function

This function appends a new medication dictionary to the list. It takes the list and the three medication fields as parameters.

```python
def add_medication(medications, drug, dose_mg, frequency):
    """Add a new medication to the list."""
    medications.append({"drug": drug, "dose_mg": dose_mg, "frequency": frequency})
    print(f"Added: {drug} {dose_mg} mg ({frequency})")
```

Key points:
- We build the dictionary inline inside `append()` — no need for a separate variable.
- Because lists are mutable, the change to `medications` is visible everywhere the same list is used.

#### Step 4: Write the `remove_medication()` Function

This function searches the list for a matching drug name and removes it. It uses a `for` loop and a case-insensitive comparison so "lisinopril" and "Lisinopril" both work.

```python
def remove_medication(medications, drug_name):
    """Remove a medication by drug name."""
    for med in medications:
        if med["drug"].lower() == drug_name.lower():
            medications.remove(med)
            print(f"Removed: {drug_name}")
            return
    print(f"'{drug_name}' not found in medication list.")
```

Key points:
- `.lower()` on both sides makes the comparison case-insensitive.
- `return` exits the function immediately after removing the first match — we don't want to keep looping.
- If no match is found after the loop finishes, we print a helpful "not found" message.

#### Step 5: Write the Main Program

Now we wire everything together. The main program creates the patient name and empty list, adds some initial medications, displays them, adds one more, and then removes a discontinued one.

```python
# Main program
patient_name = "Sarah Johnson"
medications = []

# Add initial medications
add_medication(medications, "Metformin", 500, "twice daily")
add_medication(medications, "Lisinopril", 10, "once daily")
add_medication(medications, "Atorvastatin", 40, "once daily at bedtime")

display_medications(patient_name, medications)

# Add a new medication
add_medication(medications, "Aspirin", 81, "once daily")
display_medications(patient_name, medications)

# Remove a discontinued medication
remove_medication(medications, "Lisinopril")
display_medications(patient_name, medications)
```

---

### Complete Working Solution

```python
# Mini-Project 1: Medication Tracker
# Manages a patient's current medication list

def display_medications(patient_name, medications):
    """Display all current medications for a patient."""
    print(f"\n=== Medication List: {patient_name} ===")
    if not medications:
        print("  No medications on file.")
    else:
        for i, med in enumerate(medications, 1):
            print(f"  {i}. {med['drug']} — {med['dose_mg']} mg — {med['frequency']}")
    print("=" * 40)

def add_medication(medications, drug, dose_mg, frequency):
    """Add a new medication to the list."""
    medications.append({"drug": drug, "dose_mg": dose_mg, "frequency": frequency})
    print(f"Added: {drug} {dose_mg} mg ({frequency})")

def remove_medication(medications, drug_name):
    """Remove a medication by drug name."""
    for med in medications:
        if med["drug"].lower() == drug_name.lower():
            medications.remove(med)
            print(f"Removed: {drug_name}")
            return
    print(f"'{drug_name}' not found in medication list.")

# Main program
patient_name = "Sarah Johnson"
medications = []

# Add initial medications
add_medication(medications, "Metformin", 500, "twice daily")
add_medication(medications, "Lisinopril", 10, "once daily")
add_medication(medications, "Atorvastatin", 40, "once daily at bedtime")

display_medications(patient_name, medications)

# Add a new medication
add_medication(medications, "Aspirin", 81, "once daily")
display_medications(patient_name, medications)

# Remove a discontinued medication
remove_medication(medications, "Lisinopril")
display_medications(patient_name, medications)
```

---

### Expected Output

**After adding the three initial medications and calling `display_medications()`:**

```
Added: Metformin 500 mg (twice daily)
Added: Lisinopril 10 mg (once daily)
Added: Atorvastatin 40 mg (once daily at bedtime)

=== Medication List: Sarah Johnson ===
  1. Metformin — 500 mg — twice daily
  2. Lisinopril — 10 mg — once daily
  3. Atorvastatin — 40 mg — once daily at bedtime
========================================
```

**After adding Aspirin:**

```
Added: Aspirin 81 mg (once daily)

=== Medication List: Sarah Johnson ===
  1. Metformin — 500 mg — twice daily
  2. Lisinopril — 10 mg — once daily
  3. Atorvastatin — 40 mg — once daily at bedtime
  4. Aspirin — 81 mg — once daily
========================================
```

**After removing Lisinopril:**

```
Removed: Lisinopril

=== Medication List: Sarah Johnson ===
  1. Metformin — 500 mg — twice daily
  2. Atorvastatin — 40 mg — once daily at bedtime
  3. Aspirin — 81 mg — once daily
========================================
```

---

## Mini-Project 2: Prescription Label Generator

Generate a formatted prescription label from patient and drug data using strings, f-strings, and functions.

**Concepts used:** strings, f-strings, functions, dictionaries, string methods

---

### Problem Statement

A pharmacy needs to generate standardised prescription labels from patient and drug data. The label must include: patient name, Rx number, drug name and strength, dosing directions, prescriber name, and date. The system should be able to generate labels for multiple prescriptions.

---

### Step-by-Step Guided Implementation

#### Step 1: Define the prescription data as a dictionary

Each prescription is stored as a dictionary with keys for all the fields that appear on the label. This mirrors the `Prescription` data model introduced in Chapter 6.

```python
prescription = {
    "rx_number": "RX-20240115-001",
    "date": "2024-01-15",
    "patient_name": "Sarah Johnson",
    "drug": "Amoxicillin 500 mg Capsules",
    "directions": "Take 1 capsule PO TID for 10 days",
    "prescriber": "Dr. Emily Chen",
}
```

#### Step 2: Write a `format_directions()` helper function

Prescription directions often use abbreviations like `PO` (by mouth) and `TID` (three times daily). This helper expands them into plain English using a dictionary and the `replace()` string method you learned in Chapter 4.

```python
def format_directions(directions):
    """Expand common prescription abbreviations in directions."""
    abbreviations = {
        "PO": "by mouth",
        "TID": "three times daily",
        "BID": "twice daily",
        "QD": "once daily",
        "PRN": "as needed",
        "AC": "before meals",
        "PC": "after meals",
    }
    for abbrev, expansion in abbreviations.items():
        directions = directions.replace(abbrev, expansion)
    return directions
```

Test it in the REPL before moving on:

```python
print(format_directions("Take 1 tablet PO BID PRN"))
# Take 1 tablet by mouth twice daily as needed
```

#### Step 3: Write a `generate_label()` function

This function takes a prescription dictionary, calls `format_directions()` to expand abbreviations, then uses an f-string to build and return the full label. The multi-line f-string (Chapter 4) keeps the layout readable.

```python
def generate_label(prescription):
    """Generate a formatted prescription label from a prescription dictionary."""
    directions = format_directions(prescription["directions"])
    label = f"""
╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        {prescription["rx_number"]}
  Date:       {prescription["date"]}
──────────────────────────────────────────────────
  Patient:    {prescription["patient_name"]}
  Drug:       {prescription["drug"]}
  Directions: {directions}
  Prescriber: {prescription["prescriber"]}
╚══════════════════════════════════════════════════╝"""
    return label
```

#### Step 4: Write the main program

Store multiple prescriptions in a list and loop over them (Chapter 8) to print a label for each one.

```python
prescriptions = [
    { ... },  # prescription 1
    { ... },  # prescription 2
]

for rx in prescriptions:
    print(generate_label(rx))
```

---

### Complete Working Solution

```python
# Mini-Project 2: Prescription Label Generator
# Generates formatted prescription labels from patient and drug data

def format_directions(directions):
    """Expand common prescription abbreviations in directions."""
    abbreviations = {
        "PO": "by mouth",
        "TID": "three times daily",
        "BID": "twice daily",
        "QD": "once daily",
        "PRN": "as needed",
        "AC": "before meals",
        "PC": "after meals",
    }
    for abbrev, expansion in abbreviations.items():
        directions = directions.replace(abbrev, expansion)
    return directions

def generate_label(prescription):
    """Generate a formatted prescription label from a prescription dictionary."""
    directions = format_directions(prescription["directions"])
    label = f"""
╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        {prescription["rx_number"]}
  Date:       {prescription["date"]}
──────────────────────────────────────────────────
  Patient:    {prescription["patient_name"]}
  Drug:       {prescription["drug"]}
  Directions: {directions}
  Prescriber: {prescription["prescriber"]}
╚══════════════════════════════════════════════════╝"""
    return label

# Sample prescriptions
prescriptions = [
    {
        "rx_number": "RX-20240115-001",
        "date": "2024-01-15",
        "patient_name": "Sarah Johnson",
        "drug": "Amoxicillin 500 mg Capsules",
        "directions": "Take 1 capsule PO TID for 10 days",
        "prescriber": "Dr. Emily Chen",
    },
    {
        "rx_number": "RX-20240115-002",
        "date": "2024-01-15",
        "patient_name": "David Lee",
        "drug": "Metformin 1000 mg Tablets",
        "directions": "Take 1 tablet PO BID with meals",
        "prescriber": "Dr. James Wilson",
    },
]

# Generate and print labels for all prescriptions
for rx in prescriptions:
    print(generate_label(rx))
```

---

### Expected Output

**Label for Sarah Johnson (Rx 001):**

```
╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        RX-20240115-001
  Date:       2024-01-15
──────────────────────────────────────────────────
  Patient:    Sarah Johnson
  Drug:       Amoxicillin 500 mg Capsules
  Directions: Take 1 capsule by mouth three times daily for 10 days
  Prescriber: Dr. Emily Chen
╚══════════════════════════════════════════════════╝
```

**Label for David Lee (Rx 002):**

```
╔══════════════════════════════════════════════════╗
  PRESCRIPTION LABEL
  Rx#:        RX-20240115-002
  Date:       2024-01-15
──────────────────────────────────────────────────
  Patient:    David Lee
  Drug:       Metformin 1000 mg Tablets
  Directions: Take 1 tablet by mouth twice daily with meals
  Prescriber: Dr. James Wilson
╚══════════════════════════════════════════════════╝
```

---

## Mini-Project 3: Dose Safety Checker

A pharmacy needs an automated system that reads patient prescription data from a CSV file, checks each dose against the maximum safe dose for that drug, and generates a written safety report.

**Concepts used:** file handling, csv module, conditionals, functions, error handling, loops

**Building on:** This project extends the Chapter 10 file challenge — reading a CSV of patient records and filtering by dose threshold — and adds structured report generation and error handling from Chapter 11.

---

### Problem Statement

A pharmacy needs an automated dose safety checker. The system reads a CSV file of patient prescriptions, checks each dose against the maximum safe dose for that drug, and generates a safety report file. The report must include: all patients reviewed, flagged patients with their doses, and a summary count.

---

### Step-by-Step Guided Implementation

#### Step 1: Create the input CSV file with patient data

The CSV file needs four columns: `name`, `drug`, `dose_mg`, and `max_dose_mg`. You can create it manually in a text editor or let your program generate it. Each row represents one patient's prescription.

```
name,drug,dose_mg,max_dose_mg
Sarah Johnson,Amoxicillin,500,1500
David Lee,Metformin,2500,2000
Maria Garcia,Lisinopril,10,40
James Patel,Atorvastatin,120,80
```

Save this as `patient_doses.csv`. Notice that David Lee and James Patel have doses that exceed their maximum — those are the patients we expect to flag.

#### Step 2: Write a `check_dose_safety()` function

This function takes a dose and a maximum dose, and returns either `"SAFE"` or `"FLAGGED"`. It's a pure function — no file I/O, just logic.

```python
def check_dose_safety(dose_mg, max_dose_mg):
    """Check if a dose is within safe limits."""
    if dose_mg > max_dose_mg:
        return "FLAGGED"
    return "SAFE"
```

Test it mentally: `check_dose_safety(500, 1500)` → `"SAFE"`, `check_dose_safety(2500, 2000)` → `"FLAGGED"`. Simple and reliable.

#### Step 3: Write a `read_patient_data()` function

This function opens the CSV file using the `csv` module and returns a list of patient dictionaries. It handles the `FileNotFoundError` gracefully so the program doesn't crash if the file is missing.

```python
import csv

def read_patient_data(filename):
    """Read patient data from a CSV file."""
    patients = []
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                patients.append({
                    "name": row["name"],
                    "drug": row["drug"],
                    "dose_mg": float(row["dose_mg"]),
                    "max_dose_mg": float(row["max_dose_mg"]),
                })
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    return patients
```

`csv.DictReader` maps each row to a dictionary using the header row as keys — the same technique introduced in Chapter 10. We convert `dose_mg` and `max_dose_mg` to `float` so we can compare them numerically.

#### Step 4: Write a `generate_safety_report()` function

This function takes the patient list, runs the safety check on each patient, and writes a formatted report to a file. It returns the count of flagged patients so the main program can display a summary.

```python
def generate_safety_report(patients, report_filename):
    """Generate a safety report and write it to a file."""
    flagged = [p for p in patients if check_dose_safety(p["dose_mg"], p["max_dose_mg"]) == "FLAGGED"]

    with open(report_filename, "w") as f:
        f.write("DOSE SAFETY REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total patients reviewed: {len(patients)}\n")
        f.write(f"Patients flagged: {len(flagged)}\n\n")

        if flagged:
            f.write("FLAGGED PATIENTS:\n")
            f.write("-" * 30 + "\n")
            for p in flagged:
                f.write(f"  {p['name']}: {p['drug']} {p['dose_mg']} mg (max: {p['max_dose_mg']} mg)\n")
        else:
            f.write("No patients flagged.\n")

    return len(flagged)
```

The list comprehension on the first line filters patients using `check_dose_safety()` — reusing the function from Step 2. The report is written with `open(..., "w")`, which creates the file if it doesn't exist and overwrites it if it does.

#### Step 5: Write the main program

The main program creates the sample CSV, reads it, generates the report, and prints a confirmation message.

```python
# Create sample input CSV
input_data = [
    ["name", "drug", "dose_mg", "max_dose_mg"],
    ["Sarah Johnson", "Amoxicillin", "500", "1500"],
    ["David Lee", "Metformin", "2500", "2000"],
    ["Maria Garcia", "Lisinopril", "10", "40"],
    ["James Patel", "Atorvastatin", "120", "80"],
]
with open("patient_doses.csv", "w", newline="") as f:
    csv.writer(f).writerows(input_data)

# Main program
patients = read_patient_data("patient_doses.csv")
num_flagged = generate_safety_report(patients, "safety_report.txt")

print(f"Safety check complete. {num_flagged} patient(s) flagged.")
print("Report saved to safety_report.txt")
```

---

### Complete Working Solution

```python
import csv

def check_dose_safety(dose_mg, max_dose_mg):
    """Check if a dose is within safe limits."""
    if dose_mg > max_dose_mg:
        return "FLAGGED"
    return "SAFE"

def read_patient_data(filename):
    """Read patient data from a CSV file."""
    patients = []
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                patients.append({
                    "name": row["name"],
                    "drug": row["drug"],
                    "dose_mg": float(row["dose_mg"]),
                    "max_dose_mg": float(row["max_dose_mg"]),
                })
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    return patients

def generate_safety_report(patients, report_filename):
    """Generate a safety report and write it to a file."""
    flagged = [p for p in patients if check_dose_safety(p["dose_mg"], p["max_dose_mg"]) == "FLAGGED"]

    with open(report_filename, "w") as f:
        f.write("DOSE SAFETY REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total patients reviewed: {len(patients)}\n")
        f.write(f"Patients flagged: {len(flagged)}\n\n")

        if flagged:
            f.write("FLAGGED PATIENTS:\n")
            f.write("-" * 30 + "\n")
            for p in flagged:
                f.write(f"  {p['name']}: {p['drug']} {p['dose_mg']} mg (max: {p['max_dose_mg']} mg)\n")
        else:
            f.write("No patients flagged.\n")

    return len(flagged)

# Create sample input CSV
input_data = [
    ["name", "drug", "dose_mg", "max_dose_mg"],
    ["Sarah Johnson", "Amoxicillin", "500", "1500"],
    ["David Lee", "Metformin", "2500", "2000"],
    ["Maria Garcia", "Lisinopril", "10", "40"],
    ["James Patel", "Atorvastatin", "120", "80"],
]
with open("patient_doses.csv", "w", newline="") as f:
    csv.writer(f).writerows(input_data)

# Main program
patients = read_patient_data("patient_doses.csv")
num_flagged = generate_safety_report(patients, "safety_report.txt")

print(f"Safety check complete. {num_flagged} patient(s) flagged.")
print("Report saved to safety_report.txt")
```

---

### Expected Output

When you run the script, you'll see this in the terminal:

```
Safety check complete. 2 patient(s) flagged.
Report saved to safety_report.txt
```

And the generated `safety_report.txt` will contain:

```
DOSE SAFETY REPORT
==================================================

Total patients reviewed: 4
Patients flagged: 2

FLAGGED PATIENTS:
------------------------------
  David Lee: Metformin 2500.0 mg (max: 2000.0 mg)
  James Patel: Atorvastatin 120.0 mg (max: 80.0 mg)
```

Two patients are flagged: David Lee's Metformin dose of 2500 mg exceeds the 2000 mg maximum, and James Patel's Atorvastatin dose of 120 mg exceeds the 80 mg maximum. Sarah Johnson and Maria Garcia are within safe limits and do not appear in the flagged section.

---

## Final Challenge: Pharmacy Management Script

### Overview

This is the capstone challenge that integrates all three mini-project themes into a single integrated pharmacy management script. You'll combine medication tracking, prescription label generation, and dose safety checking — plus file I/O and error handling — into one complete program. By the time you finish, you'll have a working tool that reflects real pharmacy workflows and demonstrates everything you've learned in this course.

---

### Problem Statement

Build a complete pharmacy management script that combines:

1. **Medication tracking** (from Mini-Project 1) — manage a patient's medication list
2. **Prescription label generation** (from Mini-Project 2) — generate formatted labels
3. **Dose safety checking** (from Mini-Project 3) — validate doses against safe limits
4. **File I/O** — save and load patient data from CSV files
5. **Error handling** — handle all errors gracefully

The script should:
- Load patient data from a CSV file (or create sample data if the file doesn't exist)
- Display the patient's current medications
- Check all doses against safe limits and flag any issues
- Generate a prescription label for each medication
- Save a safety report to a file
- Print a final summary

**Concepts used:**
- Variables and data types (Chapter 2)
- Operators (Chapter 3)
- Strings and f-strings (Chapter 4)
- Lists and dictionaries (Chapters 5–6)
- Conditionals (Chapter 7)
- Loops (Chapter 8)
- Functions with docstrings (Chapter 9)
- File handling with `csv` module (Chapter 10)
- Error handling with `try`/`except` (Chapter 11)

---

### Expected Output

When you run the script (with no existing `patients.csv`), you'll see:

```
============================================================
       PHARMACY MANAGEMENT SYSTEM
============================================================

Sample data file created: patients.csv

============================================================
PATIENT MEDICATION LIST
============================================================
Patient: Sarah Johnson (Age: 45)
  1. Metformin        500.0 mg  twice daily
  2. Lisinopril        10.0 mg  once daily
  3. Atorvastatin      20.0 mg  once daily

Patient: David Lee (Age: 62)
  1. Amoxicillin      500.0 mg  three times daily
  2. Metformin       2500.0 mg  twice daily
  3. Warfarin          15.0 mg  once daily

============================================================
DOSE SAFETY CHECK
============================================================
  Sarah Johnson  | Metformin       500.0 mg  | OK       (max: 2550 mg)
  Sarah Johnson  | Lisinopril       10.0 mg  | OK       (max:   40 mg)
  Sarah Johnson  | Atorvastatin     20.0 mg  | OK       (max:   80 mg)
  David Lee      | Amoxicillin     500.0 mg  | OK       (max: 3000 mg)
  David Lee      | Metformin      2500.0 mg  | WARNING  (max: 2550 mg)
  David Lee      | Warfarin         15.0 mg  | EXCEEDED (max:   10 mg)

============================================================
PRESCRIPTION LABELS
============================================================

----------------------------------------------------------
Rx: RX-001
Patient:    Sarah Johnson
Drug:       Metformin 500.0 mg
Directions: Take as directed — twice daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

----------------------------------------------------------
Rx: RX-002
Patient:    Sarah Johnson
Drug:       Lisinopril 10.0 mg
Directions: Take as directed — once daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

----------------------------------------------------------
Rx: RX-003
Patient:    Sarah Johnson
Drug:       Atorvastatin 20.0 mg
Directions: Take as directed — once daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

----------------------------------------------------------
Rx: RX-004
Patient:    David Lee
Drug:       Amoxicillin 500.0 mg
Directions: Take as directed — three times daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

----------------------------------------------------------
Rx: RX-005
Patient:    David Lee
Drug:       Metformin 2500.0 mg
Directions: Take as directed — twice daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

----------------------------------------------------------
Rx: RX-006
Patient:    David Lee
Drug:       Warfarin 15.0 mg
Directions: Take as directed — once daily
Prescriber: Dr. A. Smith
Date:       2024-01-15
----------------------------------------------------------

============================================================
SAFETY REPORT SAVED
============================================================
Report written to: safety_report.txt

============================================================
FINAL SUMMARY
============================================================
Total patients:    2
Total medications: 6
Labels generated:  6
Doses flagged:     2
Safety report:     safety_report.txt
============================================================
```

---

### Complete Reference Solution

```python
# pharmacy_management.py
# Final Challenge: Pharmacy Management Script
# Integrates medication tracking, label generation, dose safety checking,
# file I/O, and error handling into one complete program.

import csv
import os
from datetime import date

# ------------------------------------------------------------------ #
# Safe dose limits (mg/day) for the drug database
# ------------------------------------------------------------------ #
DRUG_LIMITS = {
    "Metformin":    2550,
    "Lisinopril":     40,
    "Atorvastatin":   80,
    "Amoxicillin":  3000,
    "Warfarin":       10,
}

PRESCRIBER = "Dr. A. Smith"
TODAY = date.today().isoformat()   # e.g. "2024-01-15"
SAMPLE_FILE = "patients.csv"
REPORT_FILE = "safety_report.txt"


# ------------------------------------------------------------------ #
# 1. FILE I/O — load patient data from CSV
# ------------------------------------------------------------------ #

def create_sample_csv(filepath: str) -> None:
    """Create a sample patients CSV file if none exists.

    Args:
        filepath: Path to the CSV file to create.
    """
    rows = [
        ["patient_name", "age", "drug", "dose_mg", "frequency"],
        ["Sarah Johnson", "45", "Metformin",    "500",  "twice daily"],
        ["Sarah Johnson", "45", "Lisinopril",    "10",  "once daily"],
        ["Sarah Johnson", "45", "Atorvastatin",  "20",  "once daily"],
        ["David Lee",     "62", "Amoxicillin",  "500",  "three times daily"],
        ["David Lee",     "62", "Metformin",   "2500",  "twice daily"],
        ["David Lee",     "62", "Warfarin",      "15",  "once daily"],
    ]
    with open(filepath, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"\nSample data file created: {filepath}")


def load_patients(filepath: str) -> dict:
    """Load patient medication data from a CSV file.

    Builds a dictionary keyed by patient name. Each value is a dict
    containing the patient's age and a list of medication entries.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A dict of {patient_name: {"age": int, "medications": [...]}}

    Raises:
        FileNotFoundError: If the file cannot be found after creation attempt.
        ValueError: If a dose value cannot be converted to float.
    """
    patients = {}

    try:
        with open(filepath, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["patient_name"].strip()
                try:
                    age = int(row["age"])
                    dose = float(row["dose_mg"])
                except ValueError as e:
                    print(f"  Warning: skipping row for {name} — {e}")
                    continue

                # Build the patient entry if first time seeing this name
                if name not in patients:
                    patients[name] = {"age": age, "medications": []}

                # Append this medication to the patient's list
                patients[name]["medications"].append({
                    "drug":      row["drug"].strip(),
                    "dose_mg":   dose,
                    "frequency": row["frequency"].strip(),
                })

    except FileNotFoundError:
        print(f"File '{filepath}' not found. Creating sample data...")
        create_sample_csv(filepath)
        return load_patients(filepath)   # retry after creating the file

    return patients


# ------------------------------------------------------------------ #
# 2. MEDICATION TRACKING — display the medication list
# ------------------------------------------------------------------ #

def display_medications(patients: dict) -> None:
    """Print a formatted medication list for all patients.

    Args:
        patients: Dict returned by load_patients().
    """
    print("\n" + "=" * 60)
    print("PATIENT MEDICATION LIST")
    print("=" * 60)

    for name, info in patients.items():
        print(f"Patient: {name} (Age: {info['age']})")
        for i, med in enumerate(info["medications"], start=1):
            print(
                f"  {i}. {med['drug']:<16} {med['dose_mg']:>6.1f} mg"
                f"  {med['frequency']}"
            )
        print()   # blank line between patients


# ------------------------------------------------------------------ #
# 3. DOSE SAFETY CHECKING — validate doses against safe limits
# ------------------------------------------------------------------ #

def check_dose(drug: str, dose_mg: float) -> str:
    """Return a safety status string for a given drug and dose.

    Args:
        drug:    Drug name (must be a key in DRUG_LIMITS).
        dose_mg: Prescribed dose in milligrams.

    Returns:
        "OK", "WARNING" (within 10% of limit), or "EXCEEDED".
    """
    max_dose = DRUG_LIMITS.get(drug)
    if max_dose is None:
        return "UNKNOWN"

    if dose_mg > max_dose:
        return "EXCEEDED"
    elif dose_mg >= max_dose * 0.9:   # within 10% of the limit
        return "WARNING"
    else:
        return "OK"


def run_safety_checks(patients: dict) -> list:
    """Check every medication for every patient and return flagged entries.

    Args:
        patients: Dict returned by load_patients().

    Returns:
        A list of dicts describing each flagged medication.
    """
    print("\n" + "=" * 60)
    print("DOSE SAFETY CHECK")
    print("=" * 60)

    flagged = []

    for name, info in patients.items():
        for med in info["medications"]:
            drug    = med["drug"]
            dose    = med["dose_mg"]
            status  = check_dose(drug, dose)
            max_val = DRUG_LIMITS.get(drug, "N/A")

            # Format the status column with colour-coded labels
            status_label = f"{status:<8}"

            print(
                f"  {name:<14} | {drug:<16} {dose:>6.1f} mg"
                f"  | {status_label} (max: {str(max_val):>4} mg)"
            )

            if status in ("WARNING", "EXCEEDED"):
                flagged.append({
                    "patient": name,
                    "drug":    drug,
                    "dose_mg": dose,
                    "max_mg":  max_val,
                    "status":  status,
                })

    return flagged


# ------------------------------------------------------------------ #
# 4. PRESCRIPTION LABEL GENERATION
# ------------------------------------------------------------------ #

def generate_label(rx_number: str, patient_name: str, med: dict) -> str:
    """Build a formatted prescription label string.

    Args:
        rx_number:    Unique Rx identifier (e.g. "RX-001").
        patient_name: Full name of the patient.
        med:          Medication dict with keys drug, dose_mg, frequency.

    Returns:
        A multi-line string containing the formatted label.
    """
    separator = "-" * 58
    label = (
        f"\n{separator}\n"
        f"Rx: {rx_number}\n"
        f"Patient:    {patient_name}\n"
        f"Drug:       {med['drug']} {med['dose_mg']} mg\n"
        f"Directions: Take as directed — {med['frequency']}\n"
        f"Prescriber: {PRESCRIBER}\n"
        f"Date:       {TODAY}\n"
        f"{separator}"
    )
    return label


def print_all_labels(patients: dict) -> int:
    """Generate and print prescription labels for every medication.

    Args:
        patients: Dict returned by load_patients().

    Returns:
        Total number of labels generated.
    """
    print("\n" + "=" * 60)
    print("PRESCRIPTION LABELS")
    print("=" * 60)

    rx_counter = 1
    for name, info in patients.items():
        for med in info["medications"]:
            rx_id = f"RX-{rx_counter:03d}"
            print(generate_label(rx_id, name, med))
            rx_counter += 1

    return rx_counter - 1   # total labels printed


# ------------------------------------------------------------------ #
# 5. SAVE SAFETY REPORT TO FILE
# ------------------------------------------------------------------ #

def save_safety_report(flagged: list, filepath: str, total_patients: int,
                        total_meds: int) -> None:
    """Write a safety report to a text file.

    Args:
        flagged:        List of flagged medication dicts from run_safety_checks().
        filepath:       Output file path.
        total_patients: Total number of patients processed.
        total_meds:     Total number of medications reviewed.
    """
    try:
        with open(filepath, "w") as f:
            f.write("PHARMACY SAFETY REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Date:              {TODAY}\n")
            f.write(f"Total patients:    {total_patients}\n")
            f.write(f"Total medications: {total_meds}\n")
            f.write(f"Doses flagged:     {len(flagged)}\n\n")

            if flagged:
                f.write("FLAGGED MEDICATIONS\n")
                f.write("-" * 60 + "\n")
                for entry in flagged:
                    f.write(
                        f"  {entry['patient']:<16} | {entry['drug']:<16}"
                        f" {entry['dose_mg']:>6.1f} mg"
                        f" [{entry['status']}]"
                        f" (max: {entry['max_mg']} mg)\n"
                    )
            else:
                f.write("No doses flagged — all patients within safe limits.\n")

        print("\n" + "=" * 60)
        print("SAFETY REPORT SAVED")
        print("=" * 60)
        print(f"Report written to: {filepath}")

    except OSError as e:
        print(f"Error saving report: {e}")


# ------------------------------------------------------------------ #
# 6. MAIN — tie everything together
# ------------------------------------------------------------------ #

def main() -> None:
    """Run the complete pharmacy management workflow."""
    print("=" * 60)
    print("       PHARMACY MANAGEMENT SYSTEM")
    print("=" * 60)

    # Step 1: Load (or create) patient data
    patients = load_patients(SAMPLE_FILE)

    # Step 2: Display medication list
    display_medications(patients)

    # Step 3: Run dose safety checks
    flagged = run_safety_checks(patients)

    # Step 4: Generate prescription labels
    total_labels = print_all_labels(patients)

    # Step 5: Save safety report
    total_patients = len(patients)
    total_meds = sum(len(info["medications"]) for info in patients.values())
    save_safety_report(flagged, REPORT_FILE, total_patients, total_meds)

    # Step 6: Print final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"Total patients:    {total_patients}")
    print(f"Total medications: {total_meds}")
    print(f"Labels generated:  {total_labels}")
    print(f"Doses flagged:     {len(flagged)}")
    print(f"Safety report:     {REPORT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
```

---

### How It All Fits Together

| Section | Concepts from handbook |
|---|---|
| `create_sample_csv()` / `load_patients()` | Chapter 10 (file handling, `csv` module), Chapter 11 (error handling) |
| `display_medications()` | Chapter 5 (lists), Chapter 6 (dicts), Chapter 8 (loops), Chapter 4 (f-strings) |
| `check_dose()` | Chapter 3 (operators), Chapter 7 (conditionals), Chapter 6 (dict `.get()`) |
| `run_safety_checks()` | Chapter 8 (loops), Chapter 9 (functions), Chapter 4 (f-strings) |
| `generate_label()` | Chapter 4 (strings, f-strings), Chapter 9 (functions, docstrings) |
| `print_all_labels()` | Chapter 8 (loops), Chapter 9 (functions) |
| `save_safety_report()` | Chapter 10 (file writing), Chapter 11 (`try`/`except`) |
| `main()` | Chapter 9 (functions), Chapter 2 (variables) |

Well done — you've just written a real pharmacy management tool using nothing but the Python fundamentals from this handbook. From here, the sky's the limit.

---

## What's Next

You now have a strong foundation in Python fundamentals and can build practical scripts for pharmacy workflows. The next step is to turn this foundation into deeper technical skills that support clinical practice, data analysis, and digital health projects.

### 1) Keep Building Python Fundamentals

- Revisit your chapter challenges and rewrite them from memory.
- Add one improvement to each mini-project (for example, input validation, better reporting, or cleaner menus).
- Practice reading other people's Python code to improve fluency.

### 2) Use the Official Python Documentation

The official docs should become your first reference when you forget syntax or want to understand a library deeply:

- Python docs home: [https://docs.python.org/3/](https://docs.python.org/3/)
- Python tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Standard library reference: [https://docs.python.org/3/library/](https://docs.python.org/3/library/)

### 3) Explore Pharmacy Informatics Learning Paths

To connect coding with your profession, look for structured learning in:

- Pharmacy informatics certificate programs at universities
- Hospital health informatics training modules
- Continuing professional development (CPD) courses in digital health and medication safety systems
- Introductory SQL and healthcare data standards training (for example: HL7/FHIR fundamentals)

These programs help bridge Python skills with real clinical systems like EHRs, dispensing platforms, and medication safety dashboards.

### 4) Learn `pandas` for Pharmacy Data Analysis

`pandas` is the most important next Python library for healthcare data tasks. It helps you clean, filter, analyze, and summarize CSV or spreadsheet data quickly.

Start here:

- Pandas docs: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- 10-minute guide: [https://pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)

Practice ideas:

- Analyze dispensing records by drug class
- Flag duplicate therapies and high-dose outliers
- Build monthly medication utilization summaries

### 5) Learn Flask for Simple Web Apps

After command-line scripts, web apps are a natural progression. `Flask` lets you turn your pharmacy tools into browser-based interfaces for easier use by colleagues.

Start here:

- Flask docs: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask tutorial: [https://flask.palletsprojects.com/en/latest/tutorial/](https://flask.palletsprojects.com/en/latest/tutorial/)

Possible first web app projects:

- A dose checker form for ward pharmacists
- A prescription label generator page
- A medication reconciliation checklist tool

### 6) Useful Python Libraries for Healthcare Workflows

As your projects grow, these libraries are often useful:

- `numpy` for numerical operations and clinical calculations
- `matplotlib` / `seaborn` for trend and safety visualization
- `openpyxl` for Excel report automation
- `requests` for working with APIs
- `scikit-learn` for introductory predictive modeling
- `fhir.resources` for experimenting with FHIR-formatted healthcare data

### Suggested 30-Day Roadmap

- **Week 1:** Rebuild Mini-Project 1 and add extra validation.
- **Week 2:** Learn basic `pandas` and analyze one real or sample medication dataset.
- **Week 3:** Rebuild Mini-Project 2 as a small Flask web app.
- **Week 4:** Expand the Final Challenge with better reports and error logging.

If you can complete this roadmap, you will move from "beginner who can follow examples" to "practitioner who can build useful pharmacy software independently."

Keep going — consistent practice beats intensity. One small script per day is enough to create major progress over a few months.
