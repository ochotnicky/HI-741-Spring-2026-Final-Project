# HI-741-Spring-2026-Final-Project
Hospital user interface for staff to handle patient data

Short description:
The code creates a simple and easy-to-use UI, through which users can interact with a program to add, remove, retrieve patient information, or perform other tasks. Admin, management, cinicians, and nurses have access to certain information through a controled login system. As the program grows, users are able to properly store and maintain the program code using a version control system so that the staff members can access and modify the code for continued development and integration. All actions performed within the program system are tracked and stored on a .csv file. 

How to run the file: 
If using the code to practice, first use data_generator.py to great a synthetic data set that can be inputed into the user interface code. Otherwise, the healthcare system using the code will need to have csv files of credentials, patients, providers, departments, encounters, procedures, and notes that will be used to run the program. Once the csv files are generated through the syntheic data file or actual hospital files, you can run the program code. The code will promt the user to enter their credentials which will show their allowed actions based on their role. The user can use the allowed action functions to perform their job. All actions performed by a user will be tracked and stored. All changes to patient information will be tracked and stored.

Packages needed:
You will need the pandas package to run this code 
tkinter, pandas, datetime, csv, timedelta, getpass, messagebox. These packages are avalible on the base(root) environment in Anaconda

Additinal information: 
Have fun using the program :) 
