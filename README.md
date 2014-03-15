NAME
----

directory-history - a better history for zsh

DESCRIPTION
-----------

directory-history is a plugin for the zsh which provides you with a per directory history which can fall back on a global history.  

It will fall back on a global history if there are no suggestions for the directory any more.  
It will create an advanced history under `.directory_history` in your home directory.  
This plugin was built to work together with the awesome _zsh-history-substring-search_ plugin.
Therefore it is necessary to provide a modified version of the _zsh-history-substring-search_ plugin.

Since _directory-history_ comes with it's own history, it will need some time to fill up it's history and until it becomes useful.

INSTALL
-------

1. Copy `directory_history.py` and `directory_logger.py` to `/usr/bin` or any other directory which is included in your PATH environment variable  

         cp directory_history.py /usr/bin/directory_history.py
         cp directory_logger.py /usr/bin/directory_logger.py

2. Adjust permissions

         cd /usr/bin
         sudo chmod +x directory_history.py directory_logger.py

3. Source plugins from your _.zshrc_
   * If you are already using the _zsh-history-substring-search_ plugin, please remove it now from your _.zshrc_ file.
   * Now you have to include both `directory-history.plugin.zsh` and the modified version of `zsh-history-substring-search.zsh` into your _.zshrc_ file.  
   You can do that by appending those lines to your _.zshrc_ file.  

             source /path/to/modified/zsh-history-substring-search.zsh
             source /path/to/directory-history.plugin.zsh

4. Configure the _zsh-history-substring-search_ plugin (if you didn't already)  
For that take a look here: https://github.com/zsh-users/zsh-history-substring-search
