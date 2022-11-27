killall picom xgifwallpaper dunst
xset -dpms
xset s noblank
xset s off
if [[ $# -gt 2 ]]; then
  sleep 0.5
  xgifwallpaper "$HOME/.config/qtile/themes/$2/background.gif" -d $((100 / $(cat "$HOME/.config/qtile/themes/$2/fps"))) -s FILL &
fi

sleep 5
dunst -conf "$HOME/.config/qtile/themes/$2/dunstrc" &
picom --corner-radius $1 &
