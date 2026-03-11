@echo off

set /p msg=Commit message kiriting:

git pull
git add .
git commit -m "%msg%"
git push

pause