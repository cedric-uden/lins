#!/bin/bash

# cd to current dir
dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" && cd $dir

wget -O 1.jpg https://imgsv.imaging.nikon.com/lineup/coolpix/p/p7000/img/sample/img_02_b.jpg
wget -O 2.jpg https://res.cloudinary.com/demo/image/upload/v1312461204/sample.jpg
wget -O 3.jpg https://www.w3schools.com/css/img_mountains.jpg
