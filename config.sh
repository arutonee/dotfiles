d="$(realpath $(dirname $0))"

if [[ $# == 0 ]]; then
  echo "Use the -h flag for help."
else
  for var in "$@"; do
    if [[ "-h" == "$var" ]]; then
      echo "-aa | Installs everything included in these dotfiles."
      echo "-a  | Installs everything not specific to the Qtile config."
      echo "-h  | Shows this message."
      echo "-p  | Sets up Picom."
      echo "-q  | Sets up Qtile."
      echo "-z  | Sets up Zsh (including custom TLDR script)."
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
      echo "export TLDR=$d/tldr" >> ~/.zshrc
    fi
    if [[ "-a" == "$var" ]]; then
      $d/config.sh -z
    fi
    if [[ "-aa" == "$var" ]]; then
      $d/config.sh -p -q -z
    fi
  done
fi
