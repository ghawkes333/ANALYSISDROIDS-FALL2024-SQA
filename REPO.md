# REPO.md

Jenna Chiarella - 4a - Git Hooks
The activity I completed was 4.a, create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. During this activity I had to combine workshop 6 and workshop 8. I learned how to combine these two workshops and their lessons. In workshop 6 we used Bandit to identify security weaknesses. In workshop 8 we used GitHooks to run static security analysis whenever a c or cpp file was changed. I had to combine these lessons. I had to add to the pre-commit file in .git/hooks to run bandit and then report the security weaknesses to a csv file. I had to use what I learned in workshop 8 to copy the pre-commit file, add to it, commit it, and then change, in the case of workshop 8, a cpp file to make the code I added in the pre-commit file run.In this project I had to change a .py file not a cpp file and instead of just printing out the security weaknesses, I had to save it to a csv file. I enjoyed connecting those lessons together for this activity. 

Ruisong Li - 4b - Fuzzing. The activity I completed was 4.b. I created a fuzz.py file that would automatically fuzz test 5 Python methods chosen by our group. In this activity, I had to combine the knowledge from workshop 11, and I learned how to use the content of this workshop and its course.


Mary Ann Hollinghead - Forensics. I completed the 4.c, the Integrated Forensics. I used the main.py file given within the project files and implemented logging. Once implemented I created a test log file to test the logs I implemented and ran the logging test file. I took screenshots and wrote a proper report and placed it on our group github labeled, GroupProject_Report_4c.pdf.  


Gabriella Hawkes - Github Actions

I wrote YML scripts that define tasks that the GitHub Actions runs. I learned how to write YML files and automatically run the scripts via GitHub Actions. I learned that GitHub Actions includes numerous templates for YML files that are easy to plug in. The GitHub Actions in the repo compiles, lints, and fuzzes the project files. 
