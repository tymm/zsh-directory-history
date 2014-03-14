# Don't name the prompt DIR_IMPROVED
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

# Call generate_history() everytime the directory is changed
chpwd_functions=(${chpwd_functions[@]} "generate_history")
# Call log_directory() everytime the directory is changed
chpwd_functions=(${chpwd_functions[@]} "log_directory")

# Call generate_history() everytime the user opens a prompt
precmd_functions=(${precmd_functions[@]} "generate_history")
# Call log_directory() everytime the user opens a prompt
precmd_functions=(${precmd_functions[@]} "log_directory")

# Call generate_history() everytime a command is executed
preexec_functions=(${preexec_functions[@]} "generate_history")
# Call log_command() everytime a command is executed
preexec_functions=(${preexec_functions[@]} "log_command")
