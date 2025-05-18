# Git Cheatsheet

## _Terminal Commands_

#### Show current working directory:
\> pwd

#### Display files within the directory (add suffix -a to show hidden files)
\> ls

#### Change working directory
\> cd [directory name]

## _Baisc Git Commands_

#### Create New or Initialize repository
\> git init [repo name]

#### Create a remote repository
\> git remote -v _(list remote repositories)_

\> git remote add [repo name] [url]

\> git remote remove [repo name] _(remove repository)_

#### Fetch data from remote repository
\> git fetch [remote repo] [branch-to-fetch] _(default branch to fetch is main)_

#### Fetch & merge data from remote repository
\> git pull [remote repo] [branch-to-fetch]

#### Create New or Overwrite Existing file
\> echo ["insert data here"] > [filename]

#### Open file editor
\> nano [filename]
> ctrl + o (to save changes) 

> ctrl + x (to exit editor)

#### Display file content
\> git cat [filename]

#### Add file to stage
\> git add [filename]

\> git add . _(adds all files in directory to stage)_

#### Remove file from stage
\> git reset HEAD [filename]

#### Undo changes to an unstaged file (_in the repository_)
\> git checkout -- [filename] _(defaults to last commit)_

\> git checkout [hash key] [filename] _(revert to a specific commit)_

#### Save file
\> git commit -m ["insert message"]

\> git commit --amend -m ["insert new message"]

#### Compare file version
\> git diff [filename]

\> git diff [filename1] [filename2]

#### View commit information
\> git log
> git log -5 (restrict to 5 displays)

> git log -5 [filename] (restrict to file-specific log)

> git log --since='Month Day Year' (restrict by date)

\> git show [6-8 chars of hash key]

#### Identifying branches
\> git branch _(* represents current branch)_

\> git checkout -b [branch name] _(creates a new branch)_

\> git checkout [branch name] _(switch branch)_

\> git merge [source] [destination] _(merge branches)_

#### Clone local repository
\> git clone [path-to-project-directory] [repo name]

\> git clone [url] _(clone remote repository)_

#### Push commits to remote repository
\> git push [remmote repo] [local branch]




