Cynthia Halim  
March 1, 2021  
Foundations of Programming: Python  
Assignment 07   
GitHub URL: https://github.com/CXHUW/ITFnd100-Mod07/blob/main/doc/Pickling_and_Error_Handling.md

# **Pickling and Error Handling**

## **Introduction**

For this assignment, students are given a task to create a Python script which uses pickling as well as error handling. Pickling serialized arbitrary object structure into byte 
forms (unpickling is opposite). Error handling is what to use when errors (non fatal) in Python are detected and resolved.

## **Information Sources**

I went to several sources in the internet by googling “Pickling in Python” and “error Handling” in Python. I found the websites that are extremely helpful for this particular
assignment. The websites include the following: https://betterprogramming.pub/how-to-handle-and-raise-exceptions-in-python-12-things-to-know-4dfef7f02e4 (external) as well as 
https://www.datacamp.com/community/tutorials/exception-handling-python (external) for error handling and https://www.tutorialspoint.com/python-pickling (external) as well as
https://docs.python.org/3/library/pickle.html (external) for pickling.

## **Scripting**

I add the title, name, date and change log as well as brief synopsis on what the script does using pseudo-code in comment form. 
The assignment contains menu option that includes a list of input from user (Figure 1). I keep it really simple for this particular script.


![image](https://user-images.githubusercontent.com/79155761/109900458-4613e600-7c4c-11eb-90e9-73f61f61e1ad.png)

*Figure 1. Input*

Next is to set up script for pickling by opening a DAT file with “wb” command which is write in binary for pickling, while “rb” is to read the binary (Figure 2).

![image](https://user-images.githubusercontent.com/79155761/109900708-a99e1380-7c4c-11eb-8fc9-11dfa82f4004.png)

*Figure 2. Pickling*

Next is to set up the error handling. For this purpose, I set it up so that it will flag an error message if a numeric is entered instead of alphabets (Figure 3).

![image](https://user-images.githubusercontent.com/79155761/109900875-e79b3780-7c4c-11eb-8b9a-c74a15e52e52.png)

*Figure 3. Setting Up Error Handling*

## **Running PyCharm**

I run the script in PyCharm by right clicking in the script and hit “run”. A text file is created and show the data provided by user (Figure 4) in binary form.

![image](https://user-images.githubusercontent.com/79155761/109900988-17e2d600-7c4d-11eb-91ac-729a19d93b40.png)

*Figure 4. Pickling Results*

In addition, I also run the script in the Command prompt to ensure that the codes will work (Figure 5).

![image](https://user-images.githubusercontent.com/79155761/109901036-2c26d300-7c4d-11eb-838b-e0945e7e7529.png)

*Figure 5. Input in Command prompt*

## **Summary**

I found the error handling is a bit challenging since placement is key where it’s located at (within the loop or outside) as well as how it is relative to the pickling (ie: flag the appropriate error relative to previous script).



