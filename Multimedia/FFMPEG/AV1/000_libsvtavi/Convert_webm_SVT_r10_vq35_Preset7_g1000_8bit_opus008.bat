for /r %%v in (*.mp4) do ffmpeg -i "%%v" -c:v libsvtav1 -r 10 -crf 35 -preset 7 -g 1000 -c:a libopus -ab 8k "%%~nv.webm" 
Rem ECHO "%%v.webm"
