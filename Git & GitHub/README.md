# Git & GitHub

### Introduction
To get started, we need to have Git installed on our workstation. If you haven't installed Git yet, please refer to [Git SCM](https://git-scm.com/).

To verify if Git is installed, run:
```bash
git --version
```
If Git is not installed, you will receive an error.

---

### Installing Git on Debian 12

If you are using Debian 12, follow these steps to install Git:

1. **Update the package list:**
    ```bash
    sudo apt update
    ```

2. **Install Git:**
    ```bash
    sudo apt install git
    ```

3. **Verify the installation:**
    ```bash
    git --version
    ```

You should see Git's version number, confirming a successful installation. For further configuration (e.g., setting your name and email), please refer to the [Git documentation](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

---

### Common Git Commands

#### Help
For general help with Git, run:
```bash
git --help
```
Or for help with a specific command, for example:
```bash
git clone --help
```

#### Cloning a Repository
If we have a repository on GitHub and want a local copy, we clone it using:
```bash
git clone "repository_url"
```

#### Initializing a New Repository
To start a project from scratch, initialize a new repository with:
```bash
git init
```
This creates an empty Git repository in your current directory.

#### Editing, Adding, and Committing Changes
We can then edit files or create new ones in our IDE. Once we are satisfied with the changes, we need to sync the modified files with our remote repository. To do so, we add the files we want to commit:
```bash
git add "path_to_your_files"
```

If we need to remove files from the staging area, use:
```bash
git rm "path_to_your_files"
```

To check the status of our working directory:
```bash
git status
```
This command shows the current branch and the changes ready to be committed.

When all desired files are added, we commit the changes:
```bash
git commit
```
Git will prompt us for a commit message, which is crucial for communicating the changes to others. Alternatively, we can use the `-m` option to add the commit message directly:
```bash
git commit -m "Your commit message"
```

Finally, we push our commits to the remote repository:
```bash
git push "repository_URL" "branch_name"
```
