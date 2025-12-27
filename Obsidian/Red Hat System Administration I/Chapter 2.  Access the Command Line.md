Chapter 2.  Access the Command Line
      Introduction to the Bash Shell
	      + The default user shell in Red Hat Enterprise Linux (RHEL) is the `GNU Bourne-Again Shell` (`bash`). The `bash` shell is an improved version of the original `Bourne Shell` (`sh`) on UNIX systems.
	      + The shell isplays a string when it is waiting for user input, called the _shell prompt_. When a regular user starts a shell, the prompt includes an ending dollar (`$`) character: `[user@host ~]$`
	      + A hash (`#`) character replaces the dollar (`$`) character when the shell is running as the superuser, `root`. This character indicates that it is a superuser shell, which helps to avoid mistakes that can affect the whole system. `[root@host ~]#`
		  +	Commands that are entered at the shell prompt have three basic parts:
			• Command to run.
		    • Options to adjust the behavior of the command.
			• Arguments, which are typically targets of the command.    
			- For example, Use the ``date`` command to display the current time and date.
			- Use the `+%R` argument with the date command to display the current time in **24-hour**  clock time.
			 ![[Pasted image 20250410120928.png]]
			- To type more than one command on a single line, use the semicolon ( ; ) as a command separator.
			  ![[Screenshot 2025-04-10 121207.png]]
			- The `passwd` command with no options changes the current user's password.
			  ![[Pasted image 20250410121730.png]]
			- With tab completion, users can quickly complete commands or file names after typing enough at the prompt to make it unique. If the typed characters are not unique, then pressing the Tab key twice displays all commands that begin with the typed characters.
			  ![[Pasted image 20250410122958.png]]
			  ![[Pasted image 20250410123602.png]]
			- Linux does not require file name extensions to classify files by type. The `file` command scans the compiled header of a file for a 2-digit magic number and displays its type. Text files are recognized because they are not compiled.
			  ![[Pasted image 20250410125345.png]]
			- The `cat` command is one of the most simple and frequently used commands in Linux.
			- The `head` and `tail` commands display the beginning and the end of a file, respectively. By default, these commands display 10 lines of the file, but they both have a `-n` option to specify a different number of lines.
			- The `wc` command counts lines, words, and characters in a file. Use the - l, -w, or -c options to display only the given number of lines, words, or characters, respectively.
			- The `history` command displays a list of previously executed commands prefixed with a command number. The `!` number command expands to the command that matches the specified number.
			- Use either the `ESC+ . or Alt+ .` key combination to insert the last word of the previous command at the cursor's current location.
			- An alternative would be to enter the shortcut command `!!` and then press Enter (uses four keystrokes) to run the most recent command in the command history. 
			- A hardware keyboard and display for input and output might be directly connected to the computer. This is the physical console from the Linux machine. The physical console supports multiple virtual consoles, which can run on separate terminals. Each virtual console supports an independent login session. You can switch between the virtual consoles by pressing `Ctrl+Alt` and a function key `(Fl through F6)` at the same time.
			- In Linux, the most common way to get a shell prompt on a remote system is to use Secure Shell (SSH). Most Linux systems (including Red Hat Enterprise Linux) and macOS provide the `OpenSSH` command-line program `ssh` for this purpose. The ssh command encrypts the connection to secure the communication against eavesdropping or hijacking of the passwords and content.
			  ssh remoteuser@remotehost
			  password
			- 
		#### Edit the Command Line
		![[Pasted image 20250425233205.png]]
		## #Quiz: Execute Commands with the Bash Shell
			**1.** Which Bash command displays the last five lines of the `/var/log/messages` file?
				- tail -n 5 /var/log/messages
			**2.** Which Bash shortcut or command separates commands on the same line?
				- ;
			**3.** Which Bash command is used to change a user's password?
				- passwd
			**4.** Which Bash command is used to display the file type?
				- file
			**5.** Which Bash shortcut or command is used for completing commands, file names, and options?
				- Pressing **Tab**
			**6.** Which Bash shortcut or command re-executes a specific command in the history list?
				- !_`number`_
			**7.** Which Bash shortcut or command jumps to the beginning of the command line?
				- Pressing **Ctrl**+**A**
			**8.** Which Bash shortcut or command displays the list of previously executed commands?
				- history
			**9.** Which Bash shortcut or command copies the last argument of previous commands?
				- Pressing **Esc**+**.**
	## Summary
	- The Bash shell is a command interpreter that prompts interactive users to specify Linux commands.
    - Many commands have a `--help` option that displays a usage message or screen.
    - You can use workspaces to organize multiple application windows.
    - The Activities button at the upper-left corner of the top bar provides an overview mode that helps to organize windows and to start applications.
    - The `file` command scans the beginning of a file and displays what type it is.
	- The `head` and `tail` commands display the beginning and end of a file, respectively.
	- You can use tab completion to complete file names when typing them as arguments to commands.
	- You can use the graphical interface for many administrative tasks. You can disable the interface to preserve resources for running applications.
	- You can write many commands in the same line by using the semicolon `;` character, and can run a single command in multiple lines by using the backslash `\` character.
	    

[Previous](https://rha.ole.redhat.com/rha/app/courses/rh124-9.3/pages/ch02s07/18266e1a-fcc0-4b25-a0a6-e337782b61a1)[Next](https://rha.ole.redhat.com/rha/app/courses/rh124-9.3/pages/ch03/18266e1a-fcc0-4b25-a0a6-e337782b61a1)	 