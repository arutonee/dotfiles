killall picom xgifwallpaper
xset -dpms
xset s noblank
xset s off
if [[ $# -gt 0 ]]; then
  sleep 0.5
  xgifwallpaper "$HOME/.config/qtile/themes/$2/background.gif" -d $((100 / $(cat "$HOME/.config/qtile/themes/$2/fps"))) -s FILL &
fi

sleep 5
picom --corner-radius $1 &
