del .\\dist\\love.zip
pyinstaller ./editor/main.py --onefile
copy .\\api\\*.lua .\\love2d\\
powershell -command "Compress-Archive .\love2d\*.* .\dist\love.zip -Update"
del .\\love2d\\*.lua
copy /b .\\dist\\main.exe + .\\dist\\love.zip .\\dist\\release\\Bit7.exe
copy .\\love2d\\license.txt .\\dist\\release\\license.txt
del .\\dist\\love.zip
del .\\dist\\main.exe