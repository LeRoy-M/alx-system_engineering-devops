Issue Summary 📃
-------------

The website's downtime occurred on **Wednesday 8th February, 2023** from __0300hrs (EAT)__ to __0400hrs (EAT)__ due to an accidental powering down of the server by the automated CI/CD system. The outage lasted for an **1 hour**, and affected . This led to users being unable to reach the site, as trying to access it returned a _503 status code_. Fortunately, due to the time of occurrence, only about __3.6%__ of users were affected.

Timeline ⏱
--------

Herein is a breakdown of the order of occurrences:

* The fault was detected at 0330hrs (EAT), when the monitoring system alerted the engineer on-call of the website server having been successfully powered down.
* The engineer immediately alerted their supervisor incharge about the matter who got to restoring the server's power as services back to normal running (talk about an ASAP response👍).
* The supervisor set the Puppet manifest to work restoring normal service provision about __10 mins__ after the fault came to light.
* Normal running of operations was restored by __0400hrs (EAT)__.

Root Cause 💥
----------

The website went down due to human error. A junior engineer on duty accidentally passed an invalid entry to the CI/CD automation system that then resulted in the website's host server of our region powering down (trust junior engineers to give you a heart attack😅).

Resolution 🔧
----------

The supervising engineer on site retrieved the configuration file for the master and executed it that it might restart the server that had powered down and set it and any other affected server back to optimal and required working conditions (Puppet to the rescue💪).

Corrective and Preventative Measures ☑️ 
------------------------------------

To avoid such incidents going forward:
* Sensitive operations to be carried on the server would need approval from the project lead. Permissions for the operations will as well be limited to the project lead and one other senior engineer.
* The Puppet manifest will has also been updated to automatically deal with similar occurences if ever there would be a repeat of the same.

![Hi Five!](https://github.com/LeRoy-M/alx-system_engineering-devops/blob/master/0x19-postmortem/hi-five.gif)

**All in all, job well done!**
