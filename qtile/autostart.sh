killall picom xgifwallpaper
sleep 0.5
picom -o 0 --fade-in-step 0.05 --fade-out-step 0.05 --inactive-opacity 0.8 --corner-radius $1 &

if [[ $# -gt 0 ]]; then
  sleep 0.5
  xgifwallpaper "$HOME/.config/qtile/themes/$2/background.gif" -d $((100 / $(cat "$HOME/.config/qtile/themes/$2/fps"))) & #-s FILL &
fi
