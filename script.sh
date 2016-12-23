echo "Converto file "$1


rm -rf fotoe/foto/*
rm -rf foto/*

mkdir fotoe/foto
mkdir foto

ffmpeg -i video/$1 foto/image%d.jpg

for image_file in foto/*.jpg
do
  convert $image_file  -blur 0x1 -paint 3 fotoe/$image_file  #best solution is 0x1 -paint 3
  convert fotoe/$image_file +level-colors 'rgb(69,56,12)','rgb(255,234,170)' fotoe/$image_file
done

ffmpeg -f image2 -i fotoe/foto/image%d.jpg videoe/$1
