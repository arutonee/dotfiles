# Case-insensitive matching
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

# Prompt
PS1='%F{red}%1~%f %F{blue}->%f '


# Aliases
alias ls="exa --icons"
alias la="exa -a --icons"
alias hx="helix"

alias tldr='python3 $TLDR/main.py'

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
export TLDR=/home/baka/git/dotfiles/tldr
