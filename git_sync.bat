@echo off

echo === Git pull boshlanyapti ===
git pull

IF %ERRORLEVEL% NEQ 0 (
    echo === Pull xatolik berdi. Stash qilinyapti... ===

    git stash
    IF %ERRORLEVEL% NEQ 0 (
        echo Stash qilishda xatolik chiqdi
        pause
        exit /b
    )

    echo === Qayta pull qilinyapti ===
    git pull
    IF %ERRORLEVEL% NEQ 0 (
        echo Pull yana xatolik berdi
        pause
        exit /b
    )

    echo === Stash qaytarilyapti ===
    git stash pop
)

echo === O'zgarishlar tekshirilyapti ===
git status --porcelain > temp_git_status.txt

for %%A in (temp_git_status.txt) do set size=%%~zA

if %size%==0 (
    echo Hech qanday ozgarish yoq. Push qilinmaydi.
    del temp_git_status.txt
    pause
    exit
)

del temp_git_status.txt

echo === Git add ===
git add .

set /p msg=Commit message kiriting:

echo === Git commit ===
git commit -m "%msg%"

IF %ERRORLEVEL% NEQ 0 (
    echo Commit qilishda xatolik chiqdi
    pause
    exit /b
)

echo === Git push qilinyapti ===
git push

IF %ERRORLEVEL% NEQ 0 (
    echo Push qilishda xatolik chiqdi
    pause
    exit /b
)

echo === Hammasi muvaffaqiyatli tugadi ===
pause