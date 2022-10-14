0. What is my PID [0-what-is-my-pid] >> Bash script that displays its own PID
1. List your processes [1-list_your_processes] >> Bash script that displays a list of currently running processes
2. Show your Bash PID [2-show_your_bash_pid] >> Bash script that displays lines containing the 'bash' word, thus allowing for easy access to the PID of the Bash process
3. Show your Bash PID made easy [3-show_your_bash_pid_made_easy] >> Bash script that displays the PID, along with the process name, of processes whose name contain the word 'bash'
4. To infinity and beyond [4-to_infinity_and_beyond] >> Bash script that displays 'To infinity and beyond' indefinitely; adding a 'sleep 2' between each iteration of the loop
5. Don't stop me now! [5-dont_stop_me_now] >> Bash script that stops '4-to_infinity_and_beyond' process; using 'kill'
6. Stop me if you can [6-stop_me_if_you_can] >> Bash script that stops '4-to_infinity_and_beyond' process; using 'kill' or 'killall'
7. Highlander [7-highlander] >> Bash script that displays 'To infinity and beyond' indefinitely, with a 'sleep 2' in between each iteration, and 'I am invincible!!!' when receiving a 'SIGTERM' signal
8. Beheaded process [8-beheaded_process] >> Bash script that kills the process '7-highlander'
9. Process and PID file [100-process_and_pid_file] >> Bash script that creates the file '/var/run/myscript.pid' containing its PID, displays 'To infinity and beyond' indefinitely, displays 'I hate the kill command' when receiving a SIGTERM signal, displays 'Y U no love me?!' when receiving a SIGINT signal, and deletes the file '/var/run/myscript.pid' and terminates itself when receiving a SIGQUIT or SIGTERM signal
10. Manage my process [101-manage_my_process, manage_my_process] >> Bash script 'manage_my_process' that indefinitely writes 'I am alive!' to the file '/tmp/my_process', and in between every 'I am alive!' message, the program should pause for 2 seconds
11. Zombie [11. Zombie] >> C program that creates 5 zombie processes where for every zombie process created, it displays 'Zombie process created, PID: ZOMBIE_PID', and makes use of the function provided
