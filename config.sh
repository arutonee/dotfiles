d="$(dirname $0)"

for var in "$@"; do
  if [[ "-h" == "$var" ]]; then
    echo "-a | Installs everything included in these dotfiles."
    echo "-h | Shows this message."
    echo "-z | Sets up zshrc."
  fi
  if [[ "-z" == "$var" ]]; then
    cp $d/zshrc ~/.zshrc
    echo "Copying $d/zshrc to ~/.zshrc"
  fi
  if [[ "-a" == "$var" ]]; then
    $d/config.sh -z
  fi
done
