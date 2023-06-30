## 0x04. Loops, conditions and parsing

**0. Create a SSH RSA key pair** `[0-RSA_public_key.pub]` >> Creating a RSA key pair.

**1. For Best School loop** `[1-for_best_school]` >> Bash script that displays `Best School` 10 times using a `for` loop.

**2. While Best School loop** `[2-while_best_school]` >> Bash script that displays `Best School` 10 times using a `while` loop.

**3. Until Best School loop** `[3-until_best_school]` >> Bash script that displays `Best School` 10 times using a `until` loop.

**4. If 9, say Hi!** `[4-if_9_say_hi]` >> Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line. Uses `while` loop and `if` statement.

**5. 4 bad luck, 8 is your chance** `[5-4_bad_luck_8_is_your_chance]` >> Bash script that loops from 1 to 10, and displays `bad luck` for the 4th loop iteration, or `good luck` for the 8th loop iteration, else `Best School` for the other iterations. Uses `while` loop, and `if`, `elif` and `else` statements.

**6. Superstitious numbers** `[6-superstitious_numbers]` >> Bash script that displays numbers from 1 to 20, and displays `4` and then `bad luck from China` for the 4th loop iteration, or `9` and then `bad luck from Japan` for the 9th loop iteration, or `17` and then `bad luck from Italy` for the 17th loop iteration. Uses `while` loop, and `case` statements.

**7. Clock** `[7-clock]` >> Bash script that displays the time for 12 hours and 59 minutes; that is, displays hours from 0 to 12 and minutes from 1 to 59, using a `while` loop.

**8. For ls** `[8-for_ls]` >> Bash script that displays the content of the current directory in a list format where only the part of the name after the first dash is displayed. Uses `for` loop.

**9. To file, or not to file** `[9-to_file_or_not_to_file]` >> Bash script that gives you information about the `school` file. Uses `if` `else` statements, checks if the file exists and prints `school file exists` if it does or `school file does not exist` if it does not exist. In the case the file exists, it prints `school file is empty` if the file is empty, `school file is not empty` if the file is not empty, `school file is not empty` if the file is a regular one, and prints nothing if it is not a regular file.

**10. FizzBuzz** `[10-fizzbuzz]` >> Bash script that displays numbers from 1 to 100. Displays `FizzBuzz` when the number is a multiple of 3 and 5, or `Fizz` when the number is multiple of 3, or `Buzz` when the number is a multiple of 5, otherwise displays the number, all in a list format.

**11. Read and cut** `[100-read_and_cut]` >> Bash script that displays the content of the file `/etc/passwd` using a `while` loop. The script displays only username, user id, and home directory path for the user.

**12. Tell the story of passwd** `[101-tell_the_story_of_passwd]` >> Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS. Format `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`.

**13. Let's parse Apache logs** `[102-lets_parse_apache_logs]` >> Bash script that displays the visitor IP along with the [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) from the Apache log file, in `IP HTTP_CODE` format and in a list format, using `awk`. [apache-access.log file](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log) downloaded and committed along with answer files.

**14. Dig the data** `[103-dig_the-data]` >> Bash script that groups visitors by IP and HTTP status code, and displays this data in `OCCURENCE_NUMBER IP HTTP_CODE` format and in a list format, ordered from the greatest to the lowest number of occurrences.
