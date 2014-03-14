NAME
====

directory-history - a better history for zsh

DESCRIPTION
===========

directory-history is a plugin for the zsh which provides you with a per directory history which can fall back on a global history.  
It will fall back on a global history if there are no suggestions for the directory any more.  
It will create an advanced history under `.directory_history` in your home directory.
This plugin was built to work together with the awesome _zsh-history-substring-search_ plugin.
Therefore it is necessary to provide a modified version of the _zsh-history-substring-search_ plugin.

INSTALL
=======

First you have to copy `directory_history.py` and `directory_logger.py` to `/usr/bin` or any other directory which is included in your PATH environment variable.

This is followed by `cd /usr/bin && chmod +x directory_history.py directory_logger.py`.

If you are already using the _zsh-history-substring-search_ plugin, please remove it now from your _.zshrc_ file.

Now you have to include both `directory-history.plugin.zsh` and the modified version of `zsh-history-substring-search.zsh` into your _.zshrc_ file.  
You can do that by appending those lines to your _.zshrc_ file.  

         source /path/to/modified/zsh-history-substring-search.zsh
		 source /path/to/directory-history.plugin.zsh

All you have left to do now is to configure the _zsh-history-substring-search_ plugin (if you didn't already had it configured).  
For that take a look here: https://github.com/zsh-users/zsh-history-substring-search
