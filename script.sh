echo $1


#ffmpeg -i video/$1 foto/image%d.jpg

for image_file in foto/*.jpg
do
  convert $image_file  -blur 0x3 -paint 5 fotoe/$image_file
done

ffmpeg -f image2 -i fotoe/foto/image%d.jpg videoe/$1
