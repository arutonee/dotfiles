d="$(dirname $0)"

if [[ $# == 0 ]]; then
  echo "Use the -h flag for help."
else
  for var in "$@"; do
    if [[ "-h" == "$var" ]]; then
      echo "-a  | Installs everything included in these dotfiles."
      echo "-h  | Shows this message."
      echo "-al | Sets up Alacritty."
      echo "-p  | Sets up Picom."
      echo "-q  | Sets up Qtile."
      echo "-z  | Sets up Zsh."
    fi
    if [[ "-al" == "$var" ]]; then
      rm ~/.config/alacritty -r
      cp $d/alacritty ~/.config/ -r
      echo "Copying $d/alacritty to ~/.config/alacritty"
    fi
    if [[ "-p" == "$var" ]]; then
      cp $d/picom.conf ~/.config/picom.conf
      echo "Copying $d/picom.conf to ~/.config/picom.conf"
    fi
    if [[ "-q" == "$var" ]]; then
      rm ~/.config/qtile -r
      cp $d/qtile ~/.config/ -r
      echo "Copying $d/qtile to ~/.config/qtile"
    fi
    if [[ "-z" == "$var" ]]; then
      cp $d/zshrc ~/.zshrc
      echo "Copying $d/zshrc to ~/.zshrc"
    fi
    if [[ "-a" == "$var" ]]; then
      $d/config.sh -al -p -q -z
    fi
  done
fi
