# evoSim
Hobby project trying to create emergent evolutionary behaviors in python

## git guide
The general structure of using git is:
code -> choose changes that are good -> "lock in" the changes in a bundle -> upload them to the github project
In git, this is called
code -> stage -> commit -> push

Git tracks the differences in the code very time we commit something, so it's easy to go through what happened in the code chronologically, and if a new version breaks something we can easily see what changed since the old version, thus helping us to find issues.

### `git add "filename"`
This adds a file to your staging. You do it when you are done making a change and have tested it. This ensures that all the bugs you make during coding don't end up on the repository, since you only stage them after you want to upload it.

### `git commit -m "message"`
This bundles up all the changes you've added using `git add` into a so-called commit and locks it in as definitive. The message usually describes the changes that you made to the overall code, for example "Added food and food spawning". The commits are stored locally first. We can revert the code to any commit easily.
This guide was made in the "added git guide" commit.

### `git push`
This uploads all changes you've committed to the online github server

### `git pull`
This downloads the newest version of the code from the online server and merges it with your code if there is new stuff. If the online version has new stuff AND your local version has other, new stuff, git will find where things are in conflict with another and ask you how to handle it.