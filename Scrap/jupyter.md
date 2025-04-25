**Writing and Running Code in Jupyter Notebook**

Jupyter Notebooks have become the preferred tool for data scientists and analysts due to their ease of use and ability to combine code, text, and images in a single document.

### Key Topics Covered:

- **Starting Jupyter Notebook**: You can launch it via Anaconda Navigator or by searching it on your computer. It opens in a web browser and runs locally, not requiring internet.

- **Navigating the Interface**: The interface shows your local file system. You can navigate directories and create new notebooks by selecting “New > Python 3.”

- **Working in a Notebook**:
  - Rename your notebook for clarity.
  - Write and run Python code in cells marked with `In [ ]`.
  - Run cells using “Run” or `Ctrl + Enter`.
  - Outputs appear below each code cell.
  - Cells are numbered in the order they are executed.
  - You can reset cell numbering with "Kernel > Restart & Run All."

- **Running External Scripts**: You can run Python scripts from a cell using `!python script_name.py`.

- **Using Variables**: Variables defined in one cell are available across all cells in the notebook's environment.

- **Text and Images**:
  - Use **Markdown** cells for formatted text and images.
  - Switch a cell to Markdown and use syntax like:
    ```markdown
    ## Text and Images in a Notebook
    ---
    In a Jupyter notebook, you can mix:
    * Code
    * Text
    * Images
    ```
  - To display images programmatically, use:
    ```python
    import numpy as np
    from matplotlib import pyplot as plt

    rad = np.linspace(0, 2 * np.pi, 200)
    x = np.sin(rad) ** 3
    y = 20 * np.cos(rad) - 10 * np.cos(2 * rad) - 5 * np.cos(3 * rad) - 2 * np.cos(4 * rad)

    plt.plot(x, y)
    plt.show()
    ```

- **Common Pitfalls**:
  - **Cell Execution Order**: The order matters. Notebooks don't enforce a top-to-bottom execution.
  - **Variable State**: Be cautious about variable values lingering from previous executions.
  - Always consider restarting the kernel and running all cells to ensure consistency.

Jupyter is user-friendly and widely documented. For further help, resources like Stack Overflow and official documentation are highly useful.

---

### CLI Command Syntax Reference

A command typically follows this structure:
```
command [options] [arguments]
```
- **command**: What you want to do (e.g., `ls`)
- **options**: Extra instructions to modify the command (e.g., `-r` to reverse order)
- **arguments**: What the command should operate on (e.g., a folder name)

#### Examples:
- Basic command:
  ```
  ls
  ```
  Lists files and folders in the current directory.

- With options:
  ```
  ls -r
  ```
  Lists content in reverse order.

  ```
  ls -a
  ```
  Shows hidden files too.

  ```
  ls -ra
  ```
  Combines both: reverse order and includes hidden files.

- With an argument (e.g., a folder name):
  ```
  ls -r work
  ```
  Lists the contents of the folder `work` in reverse order.

Notes:
- Options usually start with `-` or `--`.
- Commands and options are **case-sensitive**.
- Some commands can run without options or arguments.
- Not all commands accept options.

You can test these in the terminal provided in Jupyter or your system's terminal (Mac/Linux/Windows).

---

### File System Navigation Commands

#### `pwd` – Print Working Directory
Displays the full path of the current working directory.
```
pwd
```

#### `cd` – Change Directory
Changes the current working directory.
```
cd [directory path]
```

#### `ls` – List Directory Contents
Lists files and folders in a directory.
```
ls [options] [directory]
```

---

### Directory and File Management Commands

#### `mkdir` – Make Directory
Creates one or more directories.
```
mkdir [options] [directories]
```

#### `rm` – Remove Files or Directories
Deletes files or directories.
```
rm [options] [files/directories]
```

---

### Additional File and Directory Commands

#### `echo` – Print Text or Write to File
```
echo [options] [string]
```
Examples:
- Print text:
  ```
  echo I want to know CLI
  ```
- Print with line break:
  ```
  echo -e 'Line 1\nLine 2'
  ```
- Write to file (overwrite):
  ```
  echo 'text' > file.txt
  ```
- Append to file:
  ```
  echo 'text' >> file.txt
  ```

#### `touch` – Create Empty File(s)
```
touch [file1] [file2] [...]
```
Example:
```
touch new_file.txt
```

#### `mv` – Move or Rename Files/Directories
```
mv [source] [destination]
```
Examples:
- Move file:
  ```
  mv file.txt folder/
  ```
- Rename file:
  ```
  mv old.txt new.txt
  ```
- Prevent overwrite:
  ```
  mv -n source.txt destination.txt
  ```
- Prompt before overwrite:
  ```
  mv -i source.txt destination.txt
  ```

#### `cp` – Copy Files or Directories
```
cp [options] [source] [destination]
```
Examples:
- Copy file:
  ```
  cp file.txt copy.txt
  ```
- Copy directory and contents:
  ```
  cp -r dir1/ dir2/
  ```
- Prevent overwrite:
  ```
  cp -n file.txt destination.txt
  ```
- Prompt before overwrite:
  ```
  cp -i file.txt destination.txt
  ```
