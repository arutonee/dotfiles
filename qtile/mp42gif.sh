if [[ $1 == "-h" ]]; then
  echo "mp42gif.sh [input] [fps] [width] [output] [every nth frame]"
else
  ffmpeg -i "$1" -vf palettegen /tmp/palette.png
  ffmpeg -i "$1" \
    -i /tmp/palette.png \
    -filter_complex "paletteuse=dither=none,select=not(mod(n\,$5)),fps=$(($2 / $5)),scale=$3:-1:flags=lanczos" \
    -vsync vfr \
    "$4"
fi
