# Don't name the prompt DIR_HISTORY
unsetopt autonamedirs

# Generates a new history for the current directory
function generate_history() {
	history_dir=("${(@f)$(directory_history.py -a -d $(pwd))}")
	export history_dir
}

# Append to history file
function log_command() {
	directory_logger.py $1 $(pwd)
}

# Export the current directory
function log_directory() {
	DIR_HISTORY=$(pwd)
	export DIR_HISTORY
}

# Call log_directory() everytime the directory is changed
chpwd_functions=(${chpwd_functions[@]} "log_directory")
# Call generate_history() everytime the directory is changed
chpwd_functions=(${chpwd_functions[@]} "generate_history")

# Call log_directory() everytime the user opens a prompt
precmd_functions=(${precmd_functions[@]} "log_directory")
# Call generate_history() everytime the user opens a prompt
precmd_functions=(${precmd_functions[@]} "generate_history")

# Call log_command() everytime a command is executed
preexec_functions=(${preexec_functions[@]} "log_command")
# Call generate_history() everytime a command is executed
preexec_functions=(${preexec_functions[@]} "generate_history")

INDEX_HISTORY=0

directory-history-search-backward() {
	if [[ $INDEX_HISTORY -gt 0 ]] && (( INDEX_HISTORY=$INDEX_HISTORY - 1 ))
	COMMAND=$(directory_history.py -i $INDEX_HISTORY -d $DIR_HISTORY)

	zle kill-whole-line
	BUFFER=$COMMAND
	zle end-of-line
	zle vi-backward-char
}

directory-history-search-forward() {
	(( INDEX_HISTORY=$INDEX_HISTORY + 1 ))
	COMMAND=$(directory_history.py -i $INDEX_HISTORY -d $DIR_HISTORY)

	if [[ $? -eq 1 ]]; then
		(( INDEX_HISTORY=$INDEX_HISTORY - 1 ))
	else
		zle kill-whole-line
		BUFFER=$COMMAND
		zle end-of-line
		zle vi-backward-char
	fi
}

zle -N directory-history-search-backward
zle -N directory-history-search-forward
