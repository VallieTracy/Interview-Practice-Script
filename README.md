# Interview Practice!
As I've been going through the job hunt, I've realized I need practice interviewing.  So I decided to take some initiative and wrote a python script to help me practice!  I wanted to create something short that I could practice everyday.  So I create a Flask app that would ask me two random questions (with a 60 second delay between them) and then I could start over if I wanted.


## Files Included in this Repo:
* <b>Static folder</b> that includes the style.css. (<i>NOTE - </i>When using Flask, the style.css needs to be stored in a folder titled 'static')                
* <b>Templates folder</b> that contains three separarte html pages. (1 for the first question, 1 for the second question, and 1 for the final page which gives the option to go back to the start)                      
* File <b>app.py</b> which contains three routes.  The three routes correspond to the three different index.html files.                       
* File <b>question_functions.py</b> which contains two functions that return the random questions that are then called in the app.py file.                        
* Two .txt files (<b>questions_list1.txt, questions_list2.txt</b>). These files contain various questions, not organized in any particular manner.  These files are called within the two functions found in the question_functions.py file.                        

## Clone and Run the Repo:
1. Clone to your desktop
2. Install Flask with the command `pip install Flask` if you don't already have it installed in your virtual environment
3. Go into question_functions.py, line 10, and insert your name in place of `Vallie`      
4. Put your mouse over the folder where this repo is cloned on your computer, right click, click on 'Git Bash Here' to pull up the Git Bash terminal
5. Type `python app.py` into the terminal    
6. Copy and paste `http://127.0.0.1:5000/` into your browser and voila!

##### If you'd like to lessen (or greaten) the time lapse for the questions, first navigate to index.html and/or index2.html. It's `line 41` in both files.  You'll see some javascript code; this is what creates the time lapse.  It's currently set to 60,000ms ( = 60 seconds).  Change it to what you like.

Flask Website: https://flask.palletsprojects.com/en/1.1.x/


Home Screen:
![interview_script](/static/interview_script.PNG)                
