# Interview Practice!
As I've been going through the job hunt, I've realized I need practice interviewing.  So I decided to take some initiative and wrote a python script to help me practice!  I wanted to create something short that I could practice everyday.  So I create a Flask app that would ask me two random questions (with a 60 second delay between them) and then I could start over if I wanted.

## Files Included in this Repo:
1.) <b>Static folder</b> that includes the style.css.  (<i>NOTE - </i>When using Flask, the style.css needs to be stored in a folder titled 'Static')       
2.) <b>Templates folder</b> that contains three separarte html pages. (1 for the first question, 1 for the second question, and 1 for the final page which gives the option to go back to the start)       
3.) File <b>app.py</b> which contains three routes.  The three routes correspond to the three different index.html files.              
4.) File <b>question_functions.py</b> which contains two functions that return the random questions that are then called in the app.py file       
5.) Two .txt files (<b>questions_list1.txt, questions_list2.txt</b>). These files contain various questions, not organized in any particular manner.  These files are called within the two functions found in the question_functions.py file.       


