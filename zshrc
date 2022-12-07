# Case-insensitive matching
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

# Prompt
PS1='%F{red}%1~%f %F{blue}->%f '


# Aliases
alias lls="ls"
alias ls="exa"
alias la="exa -a"

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
