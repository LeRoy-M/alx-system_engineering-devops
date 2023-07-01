## 0x05. Processes and signals

**0. What is my PID** `[0-what-is-my-pid]` >> Bash script that displays its own PID.

**1. List your processes** `[1-list_your_processes]` >> Bash script that displays a list of all currently running processes for all users, including those which might not have a TTY, and displays in a user-oriented format with process hierarchy.

**2. Show your Bash PID** `[2-show_your_bash_pid]` >> Bash script that displays lines containing the `bash` word using the previous tasks command, thus allowing one to easily get the PID of your Bash process.

**3. Show your Bash PID made easy** `[3-show_your_bash_pid_made_easy]` >> Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

**4. To infinity and beyond** `[4-to_infinity_and_beyond]` >> Bash script that displays `To infinity and beyond` indefinitely, with a `sleep`  of `2 secs` between each iteration.

**5. Don't stop me now!** `[5-dont_stop_me_now]` >> Bash script that stops `4-to_infinity_and_beyond` process, using `kill`.

**6. Stop me if you can** `[6-stop_me_if_you_can]` >> Bash script that stops `4-to_infinity_and_beyond` process, but without using `kill` or `killall`.

**7. Highlander** `[7-highlander]` >> Bash script that displays `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration, and displays `I am invincible!!!` when receiving a `SIGTERM` signal.

**8. Beheaded process** `[8-beheaded_process]` >> Bash script that kills the process `7-highlander`.

**9. Process and PID file** `[100-process_and_pid_file]` >> Bash script that creates the file `/var/run/myscript.pid` containing its PID, displays `To infinity and beyond` indefinitely or `I hate the kill command` when receiving a SIGTERM signal or `Y U no love me?!` when receiving a SIGINT signal, and deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal.

**10. Manage my process** `[101-manage_my_process, manage_my_process]` >> `manage_my_process` bash script that indefinitely writes `I am alive!` to the file `/tmp/my_process`, pausing for 2 seconds in between every message. The bash (init) script `101-manage_my_process` that manages `manage_my_process`.

**11. Zombie** `[102-zombie.c]` >> C program that creates 5 zombie processes, and displays `Zombie process created, PID: ZOMBIE_PID` for every zombie process created.
