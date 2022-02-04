```
The files/folder in your version control will not just delete themselves just because you added them to the .gitignore. They are already in the repository and you have to
remove them. You can just do that with this:

Remember to commit everything you've changed before you do this!

git rm -rf --cached .
git add .

This removes all files from the repository and adds them back (this time respecting the rules in your .gitignore).
```

```
git fetch --all
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git pull --all
```
