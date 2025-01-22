# Git & Github

### Introduction
First of all, I'm working with VScode, so some things might be different on your side. 

To start things off:
you need to have git installed on your workstation
https://git-scm.com/

To check whether it is installed or not, you need to do a quick:
> git --version or git -v 

If git is not installed, it will return an error

---
### Commands:

First of all, ff you need help:
> git -h or git --help

I do have this github repository, I want to have a local copy of it on my workstation, so I need to clone the repository using:
> git clone "url of my repo"

If you want to start a project from scratch:
>git init 

It will create an empty project on the working directory of your workstation

I can then edit files, create new ones on my IDE or whatever, and when I'm satisfied with the changes that I made, I need to sync the modified file on the github/gitlab, to do so, I need to add the files that I want to commit with
> git add "path_of_the_local_files"

To remove files from a commit, use:
>git rm "path_of_the_local_files"

To get the status of the working tree, user:
> git status
> 
I will show infos of the current status of you working directory(branch, changes that you will commit)

When all the files are added, I need to commit the changes, to do so:
>git commit 

You will then be promted for a commit message, this message is very important, it help other peaple working on the same project  you know what you have done in the commit.
You can also use the -m option to add your commit msg directly in the command line 
> git commit -m "msg"

Then you need to push it to the distant repository with 
> git push "repository URL" "branch_name"

