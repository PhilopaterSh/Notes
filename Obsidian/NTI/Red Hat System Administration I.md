
- [ ] Chapter 1.  Get Started with Red Hat Enterprise Linux
      #Quiz: Get Started with Red Hat Enterprise Linux
		    1.Which two statements are benefits of open source software for the user? 
			    - You can learn from real-world code and develop more effective applications.
			    - Code can survive the loss of the original developer or distributor.
			2.Which two statements are ways in which Red Hat develops products for the future and interacts with the community?
				- Participate in upstream projects.
				- Sponsor and integrate open source projects into the community-driven Fedora project.
			3.Which two statements describe the benefits of Linux?
				- Linux includes a powerful and scriptable command-line interface, which enables easier automation and provisioning.
				- Linux is modular and can be configured for a full graphical desktop or a small appliance.
- [ ] Chapter 2.  Access the Command Line
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
- [ ] Chapter 3.  Manage Files from the Command Line
	       **The File-system Hierarchy**
	      ![[Pasted image 20250501163055.png]]
	      The `/` directory is the root directory at the top of the file-system hierarchy. The `/` character is also used as a directory separator in file names. For example, if `etc` is a subdirectory of the `/` directory, then refer to that directory as `/etc`. Likewise, if the `/etc` directory contains a file that is named `issue`, then refer to that file as `/etc/issue`.
	**Significant Red Hat Enterprise Linux Directories**

| Location | Purpose                                                                                                                                                                                                                                                                                                                     |
| :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/boot`  | Files to start the boot process.                                                                                                                                                                                                                                                                                            |
| `/dev`   | Special device files that the system uses to access hardware.                                                                                                                                                                                                                                                               |
| `/etc`   | System-specific configuration files.                                                                                                                                                                                                                                                                                        |
| `/home`  | Home directory, where regular users store their data and configuration files.                                                                                                                                                                                                                                               |
| `/root`  | Home directory for the administrative superuser, `root`.                                                                                                                                                                                                                                                                    |
| `/run`   | Runtime data for processes that started since the last boot. This data includes process ID files and lock files. The contents of this directory are re-created on reboot. This directory consolidates the `/var/run` and `/var/lock` directories from earlier versions of Red Hat Enterprise Linux.                         |
| `/tmp`   | A world-writable space for temporary files. Files that are not accessed, changed, or modified for 10 days are deleted from this directory automatically. The `/var/tmp` directory is also a temporary directory, in which files that are not accessed, changed, or modified in more than 30 days are deleted automatically. |
| `/usr`   | Installed software, shared libraries, including files, and read-only program data. Significant subdirectories in the `/usr` directory include the following commands:<br><br>- `/usr/bin`: User commands<br>    <br>- `/usr/sbin`: System administration commands<br>    <br>- `/usr/local`: Locally customized software    |
| `/var`   | System-specific variable data should persist between boots. Files that dynamically change, such as databases, cache directories, log files, printer-spooled documents, and website content, might be found under `/var`.                                                                                                    |
		#Quiz Quiz: Describe Linux File System Hierarchy Concepts
			**1.** Which directory contains persistent, system-specific configuration data?
				- /etc
			**2.** Which directory is the top of the system's file-system hierarchy?
				-  /
			**3.** Which directory contains user home directories?
				- /home
			**4.** Which directory contains files to boot the system?
				 - /boot
			**5.** Which directory contains system files to access hardware?
				- `/dev`
			**6.** Which directory is the administrative superuser's home directory?
				- `/root`
			**7.** Which directory contains regular commands and utilities?
				- /usr/bin
			**8.** Which directory contains non-persistent process runtime data?
				- /run
			**9.** Which directory contains installed software programs and libraries?
				- /usr
		Specify Files by Name
		### Navigate Paths in the File System
			- The `pwd` command displays the full path name of the current working directory for that shell. This command helps you to determine the syntax to reach files by using relative path names. 
			- The `ls` command lists directory contents for the specified directory or, if no directory is given, for the current working directory.
			- The `ls` command has multiple options for displaying attributes on files. The most common options are `-l` (long listing format), `-a` (all files, including _hidden_ files), and `-R` (recursive, to include the contents of all subdirectories).
			- Use the `cd` command to change your shell's current working directory. If you do not specify any arguments to the command, then it changes to your home directory.
			- The prompt displays the tilde character (`~`) when your current working directory is your home directory.
			- The `touch` command updates the time stamp of a file to the current date and time without otherwise modifying it. This command is useful for creating empty files, and can be used for practice, because when you use the `touch` command with a file name that does not exist, the file is created.
			- At the top of the listing are two special directories. One dot (`.`) refers to the current directory, and two dots (`..`) refer to the parent directory. These special directories exist in every directory on the system, and they are useful when using file management commands.
			- ==> File names that begin with a dot (`.`) indicate _hidden_ files; you cannot see them in the normal view with `ls` and other commands. This behavior is _not_ a security feature. Hidden files keep necessary user configuration files from cluttering home directories. Many commands process hidden files only with specific command-line options, and prevent one user's configuration from being accidentally copied to other directories or users.
			  To protect file _contents_ from improper viewing requires the use of _file permissions_.
			-  The `cd -` command changes to the previous directory, where the user was _previously_ to the current directory.
				[user@host ~]$ **`cd Videos`**
				[user@host Videos]$ **`pwd`**
				/home/user/Videos
				[user@host Videos]$ **`cd /home/user/Documents`**
				[user@host Documents]$ **`pwd`**
				/home/user/Documents
				[user@host Documents]$ **`cd -`**
				[user@host Videos]$ **`pwd`**
				/home/user/Videos
			- The `cd ..` command uses the (`..`) hidden directory to move up one level to the parent directory, without needing to know the exact parent name. The other hidden directory (`.`) specifies the _current directory_ on commands where the current location is either the source or destination argument, and avoids the need to type the directory's absolute path name.
			### References
				`info libc 'file name resolution'` (_GNU C Library Reference Manual_)
				- Section 11.2.2 File Name Resolution
				[https://www.gnu.org/software/libc/manual/html_node/File-Name-Resolution.html](https://www.gnu.org/software/libc/manual/html_node/File-Name-Resolution.html)`bash`(1), `cd`(1), `ls`(1), `pwd`(1), `unicode`(7), and `utf-8`(7) man pages
				[UTF-8 and Unicode](http://www.utf-8.com/)
			#Quiz Quiz: Specify Files by Name
				**1.** Which command returns to your current home directory, assuming that the current working directory is `/tmp` and your home directory is `/home/user`?
					- `cd`
				**2.** Which command displays the absolute path name of the current location?
					- `pwd`
				**3.** Which command returns you to the working directory before the current working directory?
					- `cd -`
				**4.** Which command changes the working directory up two levels from the current location?
					- `cd ../..`
				**5.** Which command lists files in the current location, with a long format, and including hidden files?
					- `ls -al`
				**6.** Which command creates an empty file called `helloworld.py` in the `user` home directory, assuming that your current directory is `/home`?
					- `touch ~/helloworld.py`
				**7.** Which command changes the working directory to the parent of the current location?
					- `cd ..`
				**8.** Which command changes the working directory to `/tmp` if the current working directory is `/home/student`?
					- `cd ../../tmp`
		Manage Files with Command-line Tools
		### Command-line File Management
			- The `mkdir` command creates one or more directories or subdirectories. It takes as an argument a list of paths to the directories that you want to create.
			- The `mkdir` command `-p` (_parent_) option creates any missing parent directories for the requested destination. In the following example, the `mkdir` command creates three ``Chapter_`N`_`` subdirectories with one command. The `-p` option creates the missing `Thesis` parent directory.
				[user@host Documents]$ **`mkdir -p Thesis/Chapter1 Thesis/Chapter2 Thesis/Chapter3`**
				[user@host Documents]$ **`ls -R Thesis/`**
				Thesis/:
				Chapter1  Chapter2  Chapter3
				Thesis/Chapter1:
				Thesis/Chapter2:
				Thesis/Chapter3:
			- The `cp` command copies a file, and creates a file either in the current directory or in a different specified directory.
			- You can also use the `cp` command to copy multiple files to a directory. In this scenario, the last argument must be a directory. The copied files retain their original names in the new directory. If a file with the same name exists in the target directory, then the existing file is overwritten.
			==> ### Note
			  By default, the `cp` command does not copy directories; it ignores them.
			- You can copy directories and their contents by using the `cp` command `-r` option. Keep in mind that you can use the `.` and `..` special directories in command combinations. 
				  [user@host Documents]$ **`cd ProjectY`**
				  [user@host ProjectY]$ **`cp -r ../Thesis/ .`**
				  [user@host ProjectY]$ **`ls -lR`**
				  .:
				  total 0
				  drwxr-xr-x. 5 user user 54 Mar  7 15:08 Thesis				
				./Thesis:
				total 0
				drwxr-xr-x. 2 user user 6 Mar  7 15:08 Chapter1
				drwxr-xr-x. 2 user user 6 Mar  7 15:08 Chapter2
				drwxr-xr-x. 2 user user 6 Mar  7 15:08 Chapter3
				./Thesis/Chapter1:
				total 0\
				./Thesis/Chapter2:
				total 0
				./Thesis/Chapter3:
				total 0
			-The `mv` command moves files from one location to another. If you think of the absolute path to a file as its full name, then moving a file is effectively the same as renaming a file. The contents of the files that are moved remain unchanged.
			- Use the `mv` command to _rename_ a file.
			- Use the `mv` command to _move_ a file to a different directory. You can use the `mv` command `-v` option to display a detailed output of the command operations.
			- The `rm` command removes files. By default, `rm` does not remove directories. You can use the `rm` command `-r` or the `--recursive` option to enable the `rm` command to remove directories and their contents. The `rm -r` command traverses each subdirectory first, and individually removes their files before removing each directory.
			- You can use the `rm` command `-i` option to interactively prompt for confirmation before deleting. This option is essentially the opposite of using the `rm` command `-f` option, which forces the removal without prompting the user for confirmation.
			- You can also use the `rmdir` command to remove empty directories. Use the `rm` command `-r` option to remove non-empty directories.
				[user@host Documents]$ **`pwd`**
				/home/user/Documents
				[user@host Documents]$ **`rmdir ProjectZ`**
				[user@host Documents]$ **`rmdir ProjectX`**
				rmdir: failed to remove 'ProjectX': Directory not empty
				[user@host Documents]$ **`rm -r ProjectX`**[user@host Documents]$ **`pwd`**
				/home/user/Documents
				[user@host Documents]$ **`rmdir ProjectZ`**
				[user@host Documents]$ **`rmdir ProjectX`**
				rmdir: failed to remove 'ProjectX': Directory not empty
				[user@host Documents]$ **`rm -r ProjectX`**
		Make Links Between Files
		###  Create Hard Links
			==Every file starts with a single hard link, from its initial name to the data on the file system. When you create a hard link to a file, you create another name that points to that same data. The new hard link acts exactly like the original file name. After the link is created, you cannot tell the difference between the new hard link and the original name of the file.==
			- You can determine whether a file has multiple hard links by using the `ls -l` command. One item that it reports is each file's _link count_, the number of hard links that the file has. In the next example, the link count of the `newfile.txt` file is 1. It has exactly one absolute path, which is the `/home/user/newfile.txt` location.
				[user@host ~]$ **`pwd`**
				/home/user
				[user@host ~]$ **`ls -l newfile.txt`**
				-rw-r--r--. `1` user user 0 Mar 11 19:19 newfile.txt
			- You can use the `ln` command to create a hard link (another file name) that points to an existing file. The command needs at least two arguments: a path to the existing file, and the path to the hard link that you want to create.
				[user@host ~]$ **`ln newfile.txt /tmp/newfile-hlink2.txt`**
				[user@host ~]$ **`ls -l newfile.txt /tmp/newfile-hlink2.txt`**
				-rw-rw-r--. `2` user user 12 Mar 11 19:19 newfile.txt
				-rw-rw-r--. `2` user user 12 Mar 11 19:19 /tmp/newfile-hlink2.txt
			- To determine whether two files are hard linked, use the `ls` command `-i` option to list each file's _inode number_. If the files are on the same file system and their inode numbers are the same, then the files are hard links that point to the same data file content.
				 [user@host ~]$ **`ls -il newfile.txt /tmp/newfile-hlink2.txt`**
				`8924107` -rw-rw-r--. 2 user user 12 Mar 11 19:19 newfile.txt
				`8924107` -rw-rw-r--. 2 user user 12 Mar 11 19:19 /tmp/newfile-hlink2.txt
			==> Hard links that reference the same file share the inode structure with the link count, access permissions, user and group ownership, time stamps, and file content. When that information is changed for one hard link, then the other hard links for the same file also show the new information. This behavior is because each hard link points to the same data on the storage device.
			- Even if the original file is deleted, you can still access the contents of the file provided that at least one other hard link exists. Data is deleted from storage only when the last hard link is deleted, which makes the file contents unreferenced by any hard link.
				[user@host ~]$ **`rm -f newfile.txt`**
				[user@host ~]$ **`ls -l /tmp/newfile-hlink2.txt`**
				-rw-rw-r--. `1` user user 12 Mar 11 19:19 /tmp/newfile-hlink2.txt
			--#### Limitations of Hard Links
				- Hard links have some limitations. First, you can use hard links only with regular files. You cannot use the `ln` command to create a hard link to a directory or special file.
				- Second, you can use hard links only if both files are on the same _file system_. The file-system hierarchy can be composed of multiple storage devices. Depending on the configuration of your system, when you change into a new directory, that directory and its contents might be stored on a different file system.
				- You can use the `df` command to list the directories that are on different file systems.
		### Create Symbolic Links
			- The `ln` command `-s` option creates a symbolic link, which is also called a "soft link". A symbolic link is not a regular file, but a special type of file that points to an existing file or directory.
			Symbolic links have some advantages over hard links:
				. Symbolic links can link two files on different file systems.
				. Symbolic links can point to a directory or special file, not just to a regular file.
			- n the following example, the `ln -s` command creates a symbolic link for the `/home/user/newfile-link2.txt` file. The name for the symbolic link is `/tmp/newfile-symlink.txt`.
				[user@host ~]$ **`ln -s /home/user/newfile-link2.txt /tmp/newfile-symlink.txt`**
				[user@host ~]$ **`ls -l newfile-link2.txt /tmp/newfile-symlink.txt`**
				-rw-rw-r--. **`1`** user user 12 Mar 11 19:19 newfile-link2.txt
				**`l`**rwxrwxrwx. **`1`** user user 11 Mar 11 20:59 /tmp/newfile-symlink.txt -> /home/user/newfile-link2.txt
			- When the original regular file is deleted, the symbolic link still points to the file but the target is gone. A symbolic link that points to a missing file is called a "dangling symbolic link".
				 [user@host ~]$ **`rm -f newfile-link2.txt`**
				[user@host ~]$ **`ls -l /tmp/newfile-symlink.txt`**
				**`l`**rwxrwxrwx. **`1`** user user 11 Mar 11 20:59 /tmp/newfile-symlink.txt -> /home/user/newfile-link2.txt
				[user@host ~]$ **`cat /tmp/newfile-symlink.txt`**
				cat: /tmp/newfile-symlink.txt: No such file or directory
			==### Important
			One side-effect of the dangling symbolic link in the preceding example is that if you create a file with the same name as the deleted file (`/home/user/newfile-link2.txt`), then the symbolic link is no longer "dangling" and points to the new file. Hard links do not work in this way. If you delete a hard link and then use normal tools (rather than `ln`) to create a file with the same name, then the new file is not linked to the old file. Consider the following way to compare hard links and symbolic links, to understand how they work:
			- A hard link points a name to data on a storage device.
			- A symbolic link points a name to another name, which points to data on a storage device.==
			- A symbolic link can point to a directory. The symbolic link then acts like the directory. If you use `cd` to change to the symbolic link, then the current working directory becomes the linked directory. Some tools might track that you followed a symbolic link to get there. For example, by default, `cd` updates your current working directory by using the name of the symbolic link rather than the name of the actual directory. If you want to update the current working directory by using the name of the actual directory, then you can use the `-P` option.
				[user@host ~]$ **`ln -s /etc /home/user/configfiles`**
				[user@host ~]$ **`cd /home/user/configfiles`**
				[user@host configfiles]$ **`pwd`**
				/home/user/configfiles
				[user@host configfiles]$ **`cd -P /home/user/configfiles`**
				[user@host etc]$ **`pwd`**
				/etc
		Match File Names with Shell Expansions
		### Command-line Expansions
			When you type a command at the Bash shell prompt, the shell processes that command line through multiple _expansions_ before running it. You can use these shell expansions to perform complex tasks that would otherwise be difficult or impossible.
			
			#### Pathname Expansion and Pattern Matching
				
| Pattern       | Matches                                                                                                       |
| :------------ | :------------------------------------------------------------------------------------------------------------ |
| *             | Any string of zero or more characters                                                                         |
| ?             | Any single character                                                                                          |
| [_abc…​_]     | Any one character in the enclosed class (between the square brackets)                                         |
| [!_abc…​_]    | Any one character _not_ in the enclosed class                                                                 |
| [^_abc…​_]    | Any one character _not_ in the enclosed class                                                                 |
| `[[:alpha:]]` | Any alphabetic character                                                                                      |
| `[[:lower:]]` | Any lowercase character                                                                                       |
| `[[:upper:]]` | Any uppercase character                                                                                       |
| `[[:alnum:]]` | Any alphabetic character or digit                                                                             |
| `[[:punct:]]` | Any printable character that is not a space or alphanumeric                                                   |
| `[[:digit:]]` | Any single digit from 0 to 9                                                                                  |
| `[[:space:]]` | Any single white space character, which might include tabs, newlines, carriage returns, form feeds, or spaces |
			**For the next example** create some sample files:-
				[user@host ~]$ **`mkdir glob; cd glob`**
				[user@host glob]$ **`touch alfa bravo charlie delta echo able baker cast dog easy`**
				[user@host glob]$ **`ls`**
				able  alfa  baker  bravo  cast  charlie  delta  dog  easy  echo
				[user@host glob]$
				- the first two commands use simple pattern matches with the asterisk (*) to match all the file names that start with "a" and all the file names that contain an "a", respectively. The third command uses the asterisk and square brackets to match all the file names that start with "a" or "c".
				[user@host glob]$ **`ls a*`**
				able  alfa
				[user@host glob]$ **`ls *a*`**
				able  alfa  baker  bravo  cast  charlie  delta  easy
				[user@host glob]$ **`ls [ac]*`**
				able  alfa  cast  charlie
				- also uses question mark (?) characters to match some of those file names. The two commands match only file names with four and five characters in length, respectively.
				[user@host glob]$ **`ls ????`**
				able  cast  easy  echo
				[user@host glob]$ **`ls ?????`**
				baker  bravo  delta
				#### Brace Expansion
				- Brace expansion is used to generate discretionary strings of characters. Braces contain a comma-separated list of strings, or a sequence expression. The result includes the text that precedes or follows the brace definition. Brace expansions might be nested, one inside another. You can also use double-dot syntax (..), which expands to a sequence. For example, the `{m..p}` double-dot syntax inside braces expands to `m n o p`.
				[user@host glob]$ **`echo {Sunday,Monday,Tuesday,Wednesday}.log`**
				Sunday.log Monday.log Tuesday.log Wednesday.log
				[user@host glob]$ **`echo file{1..3}.txt`**
				file1.txt file2.txt file3.txt
				[user@host glob]$ **`echo file{a..c}.txt`**
				filea.txt fileb.txt filec.txt
				[user@host glob]$ **`echo file{a,b}{1,2}.txt`**
				filea1.txt filea2.txt fileb1.txt fileb2.txt
				[user@host glob]$ **`echo file{a{1,2},b,c}.txt`**
				filea1.txt filea2.txt fileb.txt filec.txt
				- ==A practical use of brace expansion is to create multiple files or directories.==
				[user@host glob]$ **`mkdir ../RHEL{7,8,9}`**
				[user@host glob]$ **`ls ../RHEL*`**
				RHEL7 RHEL8 RHEL9
				#### Tilde Expansion
				- The tilde character (~), matches the current user's home directory. If it starts with a string of characters other than a slash (/), then the shell interprets the string up to that slash as a username, if one matches, and replaces the string with the absolute path to that user's home directory. If no username matches, then the shell uses an actual tilde followed by the string of characters.
				The `echo` command displays the value of the tilde (`~`).
				[user@host glob]$ **`echo ~root`**
				/root
				[user@host glob]$ **`echo ~user`**
				/home/user
				[user@host glob]$ **`echo ~/glob`**
				/home/user/glob
				[user@host glob]$ **`echo ~nonexistinguser`**
				~nonexistinguser
				#### Variable Expansion
				- A variable acts like a named container that stores a value in memory. Variables simplify accessing and modifying the stored data either from the command line or within a shell script.
				- Variable names can contain only letters (uppercase and lowercase), numbers, and underscores. Variable names are case-sensitive and cannot start with a number.
				- You can assign data as a value to a variable with the following syntax:
				[user@host ~]$ **`VARIABLENAME=value`**
				==You can use variable expansion to convert the variable name to its value on the command line. If a string starts with a dollar sign ($), then the shell tries to use the rest of that string as a variable name and to replace it with the variable value.==
				[user@host ~]$ **`USERNAME=operator`**
				[user@host ~]$ **`echo $USERNAME`**
				operator
				==To prevent mistakes due to other shell expansions, you can put the name of the variable in curly braces==
				[user@host ~]$ **`USERNAME=operator`**
				[user@host ~]$ **`echo ${USERNAME}`**
				operator
				#### Command Substitution
				- Command substitution enables the output of a command to replace the command itself on the command line. Command substitution occurs when you enclose a command in parentheses and precede it by a dollar sign (`$`). The ``$(_`command`_)`` form can nest multiple command expansions inside each other.
				[user@host glob]$ **`echo Today is $(date +%A).`**
				Today is Wednesday.
				[user@host glob]$ **`echo The time is $(date +%M) minutes past $(date +%l%p).`**
				The time is 26 minutes past 11AM.
				### Protecting Arguments from Expansion
				- Many characters have a special meaning in the Bash shell. To prevent shell expansions on parts of your command line, you can quote and escape characters and strings.
				- The backslash (`\`) is an escape character in the Bash shell. It protects the following character from expansion.
				The value of /home/user is your home directory.
				[user@host glob]$ **`echo The value of $HOME is your home directory.`**
				[user@host glob]$ **`echo The value of \$HOME is your home directory.`**
				- The value of $HOME is your home directory.
				In the preceding example, with the dollar sign protected from expansion, Bash treats it as a regular character, without variable expansion on `$HOME`.
				- To protect longer character strings, you can use single quotation marks (`'`) or double quotation marks (`"`) to enclose strings. They have slightly different effects. Single quotation marks stop all shell expansion. Double quotation marks stop _most_ shell expansion.
				- Double quotation marks suppress special characters other than the dollar sign (`$`), backslash (`\`), backtick (`), and exclamation point (`!`) from operating inside the quoted text. Double quotation marks block pathname expansion, but still allow command substitution and variable expansion to occur.
				[user@host glob]$ **`myhost=$(hostname -s); echo $myhost`**
				host
				[user@host glob]$ **`echo "***** hostname is ${myhost} *****"`**
				***** hostname is host *****
				Use single quotation marks to interpret _all_ text between the - quotes literally.
				[user@host glob]$ **`echo "Will variable $myhost evaluate to $(hostname -s)?"`**
				Will variable host evaluate to host?
				[user@host glob]$ **`echo 'Will variable $myhost evaluate to $(hostname -s)?'`**
				Will variable $myhost evaluate to $(hostname -s)?
				==> It is easy to confuse the single quotation mark ( ' ) and the command substitution backtick ( ` ), on both the screen and the keyboard. The use of one when you mean to use the other leads to unexpected shell behavior.
	 			#Quiz: Match File Names with Shell Expansions
		 			**1.** Which pattern matches only file names that end with "b"?
		 			*b
		 			**2.** Which pattern matches only file names that begin with "b"?
		 			b*
		 			**3.** Which pattern matches only file names where the first character is not "b"?
		 			`[!b]*`
		 			**4.** Which pattern matches all file names that contain a "b"?
		 			*b*
		 			**5.** Which pattern matches only file names that contain a number?
		 			`*[[:digit:]]*`
		 			**6.** Which pattern matches only file names that begin with an uppercase letter?
		 			`[[:upper:]]*`
		 			**7.** Which pattern matches only file names with at least three characters?
		 			???*
		 ## Summary
		- Files on a Linux system are organized into a single inverted tree of directories, a file-system hierarchy.
		- Absolute paths start with a forward slash character (`/`) and specify the location of a file in the file-system hierarchy.
		- Relative paths do not start with a forward slash character.
		- Relative paths specify a file location in relation to the current working directory.
		- You can use commands in combination with the dot (`.`), double dot (`..`), and tilde (`~`) special characters to refer to a file location in the file system.
		- The `mkdir`, `rmdir`, `cp`, `mv`, and `rm` commands are key commands to manage files in Linux.
		- Hard links and soft links are different ways for multiple file names to point to the same data.
		- The Bash shell provides pattern matching, expansion, and substitution features to help you to run commands efficiently.

- [ ]  Chapter 4.  Get Help in Red Hat Enterprise Linux
		- The `man` command also has its own manual pages. Open the `man`(1) command manual page.
		- [student@workstation ~]$ **`man gedit`**
		GEDIT(1)    General Commands Manual      GEDIT(1)
		NAME
		       gedit - text editor for the GNOME Desktop
		SYNOPSIS
		       gedit [OPTION...] [FILE...] [+LINE[:COLUMN]]
		       gedit [OPTION...] -
		_...output omitted..._
		Press **q** to quit the man page.
		- The `/usr/share/man` directory contains all man pages. Locate the binary, source, and manual pages for the `passwd` utility by using the `whereis` command. Verify that the `/ï»¿usr/share/man` directory contains the man pages for the `passwd` utility.
		[student@workstation ~]$ **`whereis passwd`**
		passwd: /usr/bin/passwd /etc/passwd `/usr/share/man/man1/passwd.1ossl.gz /usr/share/man/man1/passwd.1.gz /usr/share/man/man5/passwd.5.gz`
		## Summary
	- Use the `man` command to view man pages and to display information about components of a Linux system, such as files, commands, and functions.
	- By convention, to refer to a man page, the name of a page is followed by its section number in parentheses.
	- You can use regular expressions to search content in man pages.
      
- [ ]   Chapter 5.  Create, View, and Edit Text Files
	### Objectives
	- Save output or errors to a file with shell redirection, and process command output through multiple command-line programs with pipes.
	### Standard Input, Standard Output, and Standard Error
	A running program, or _process_, reads input and writes output. When you run a command from the shell prompt, it normally reads its input from the keyboard and sends its output to the terminal window.
	A process uses numbered channels called _file descriptors_ to get input and send output. All processes start with at least three file descriptors. _Standard input_ (channel 0) reads input from the keyboard. _Standard output_ (channel 1) sends normal output to the terminal. _Standard error_ (channel 2) sends error messages to the terminal.
	If a program opens separate connections to other files, then it might use higher-numbered file descriptors.
	![[Pasted image 20250615060004.png]]
	### Redirect Output to a File
	- The Input/Output (I/O) redirection changes how the process gets its input or output. Instead of getting input from the keyboard, or sending output and errors to the terminal, the process can read from or write to files. With redirection, you can save the messages to a file instead of displaying the output on the terminal. Alternatively, you can use redirection to discard output or errors, so they are not displayed on the terminal or saved.
	- You can redirect a process `stdout` to suppress the process output from appearing on the terminal. If you redirect `stdout` to a file and the file does not exist, then the file is created. If the file does exist and the redirection does not append to the file, then the redirection overwrites the file's contents. To discard the output of a process, you can redirect to the empty `/dev/null` special file that discards channel output that is redirected to it.
	- As viewed in the following table, redirecting _only_ `stdout` does not suppress displaying `stderr` error messages on the terminal.
**Table 5.2. Output Redirection Operators**

| Usage          | Explanation                                                         | Visual aid                                                                                                         |
| :------------- | :------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| > _file_       | Redirect `stdout` to overwrite a file.                              | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/redirection-overview.svg) |
| >> _file_      | Redirect `stdout` to append to a file.                              | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/redirection-append.svg)   |
| 2> _file_      | Redirect `stderr` to overwrite a file.                              | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/redirection-error.svg)    |
| 2> /dev/null   | Discard `stderr` error messages by redirecting them to `/dev/null`. | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/dev-null.svg)             |
| > _file_ 2>&1  | Redirect `stdout` and `stderr` to overwrite the same file.          | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/combine-overwrite.svg)    |
| &> _file_      |                                                                     |                                                                                                                    |
| >> _file_ 2>&1 | Redirect `stdout` and `stderr` to append to the same file.          | ![](https://static.ole.redhat.com/rha/courses/rh124-9.3/images/edit/redirect/images/edit/combine-append.svg)       |
| &>> _file_     |                                                                     |                                                                                                                    |
	### Construct Pipelines
	A _pipeline_ is a sequence of one or more commands that are separated by the vertical bar character (`|`). A pipeline connects the standard output of the first command to the standard input of the next command.
	![[Pasted image 20250615130430.png]]
	Use pipelines to manipulate and format the output of a process by other processes before it is output to the terminal. Imagine that data "flows" through the pipeline from one process to another, and is altered by each command in the pipeline that it flows through.
	#### Pipelines, Redirection, and Appending to a File
	When you combine redirection with a pipeline, the shell sets up the entire pipeline first, and then it redirects the input/output. If you use output redirection in the _middle_ of a pipeline, then the output goes to the file and not to the next command in the pipeline.
	![[Pasted image 20250615130837.png]]
	#Quiz 
		1.	Which output redirection operator displays output to a terminal and discards all error messages?
			2> /dev/null
		2. Which output redirection operator sends output to a file and sends errors to a different file?
			> file 2> file2
		3. Which output redirection operator sends both output and errors to a file, and creates it or overwrites its contents?
			&> file
		4. Which output redirection operator sends output and errors to the same file and preserves the file content if it exists?
			>> file 2>&1
		5. Which output redirection operator discards all messages that are normally sent to the terminal?
			&> /dev/null
		6. Which output redirection operator sends output to both the screen and a file at the same time?
			| tee file
		7. Which output redirection operator saves output to a file and discards all error messages?
			> file 2> /dev/null
		


- [ ] 
- [ ] 
- [ ] 




✅ Steps to Make All Prompt Text Green:
🟢 Edit your .bashrc file:
Open terminal and run:

bash
Copy
Edit
nano ~/.bashrc
🟢 Find or add the line that starts with PS1=
Replace it with this:

bash
Copy
Edit
PS1='\[\e[32m\]\u@\h:\w\$ \[\e[0m\]'
🔍 Explanation:
\[\e[32m\] → Sets green color

\u → Username

\h → Hostname

\w → Current working directory

\$ → Symbol ($ or #)

\[\e[0m\] → Resets color to normal (just to be safe after the prompt)

✅ Save and apply:
Press Ctrl + X, then Y, then Enter to save.

Apply changes:

bash
Copy
Edit
source ~/.bashrc
💡 Final Look:
bash
Copy
Edit
mustafa@ubuntu:~/Desktop$
➡ All in green color!


#### create symbolic link
ln -s + Path  + name shortcut
we can used s"name" 
can we used cd -P and ls -l  for know where this symbolic link

#### Create hard link 

[^1]: Name Machine

[^2]: IP address
