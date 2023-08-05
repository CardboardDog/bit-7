pyinstaller ./editor/main.py --onefile
powershell -command "Compress-Archive .\love2d\ .\dist\love.zip -Update"
copy /b .\\dist\\main.exe + .\\dist\\love.zip .\\dist\\release\\Bit7.exe
copy .\\love2d\\license.txt .\\dist\\release\\license.txt
.\\dist\\release\\Bit7.exe