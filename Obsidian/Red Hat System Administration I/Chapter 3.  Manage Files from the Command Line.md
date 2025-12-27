Chapter 3.  Manage Files from the Command Line
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
