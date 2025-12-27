Chapter 4.  Get Help in Red Hat Enterprise Linux
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