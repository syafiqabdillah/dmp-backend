# Dataset Management Platform (Backend)

Author: Syafiq Abdillah Umarghanis
# Disclaimer
This homework project doesn't fullfil technical requirement no 7 "Use SQLite" because Heroku doesn't support SQLite due to its "disk backed storage" while Heroku server's disk storage will be cleared periodically. 
Source: https://devcenter.heroku.com/articles/sqlite3.
For the alternative, I use PostgreSQL as the relational database. But worry not, the database is integrated whether you use the live demo version of trying to install this project locally on your machine.
# Live Demo (Heroku)
You can access the live demo version at <br>
https://dmp-konvergenai.herokuapp.com <br>
username: user1 <br>
password: user1
# Installation Manual
## System Requirements 
1. Python 3.8.3 
2. Git 2.27.01
## Prerequisites
1. Go to certain directory or make a new one. Let's call it DMP <br> 
`mkdir DMP && cd DMP`
2. Clone this repo to DMP <br> 
`git clone https://github.com/syafiqabdillah/dmp-backend.git backend`
3. Download .env file that has been sent via email
## Installation 
1. Go to DMP directory
2. Go to backend directory <br>
`cd backend`
3. Install virtualenv library for python (if you don't have any similar library) <br>
`python install virtualenv`
4. Create a new environtment called venv <br>
`virtualenv venv`
5. Get into the virtual environtment <br>
`source venv/bin/activate` for Linux & MacOS <br>
`venv\Scripts\activate` for Windows
6. Install all dependencies <br>
`pip install -r requirements.txt`
7. Copy paste .env file for backend (sent via email) to backend directory
8. Run the server <br>
`uvicorn main:app --reload`
9. Your server is running on port 8000. Open http://localhost:8000 in your browser to make sure that it is installed properly.
## Questions 
Any questions or difficulties? Don't hesitate to ask me by posting new issue in this repo or sending me emails at abdillah.syafiq@gmail.com