The access control mechanism is designed based on the principle Attribute-Based Access Control 
and achieved the access control using a combination of policy rule and access control matrix. 
The program will determine the access granted or not based on three attributes, subject, object, 
and environment, and determine the access way, Ex, view-only/modify, etc., by checking the access 
control matrix. The access control mechanism follows all the policies listed in the contract.

The password mechanism involves three different parts, password storage, password checker 
and password verification. The password is stored within a text file locally, includes 
user ID, plaintext Salt and the hash code of the password. The storage of passwords is 
separate from user information to maximally protect the user’s information and the 
password due to the password file might need a higher security level than the common 
user information. The selected encryption way of the password is SHA-256 and a randomly 
32 bytes Salt value with 100,000 iterations and the encryption of the password is 
one-way encryption due to the characteristic of hash, that brings the password verification 
not involve calculation using the existing hash code of the password, only the comparison. 
The password checkers involved all the password policies listed in the contract. The 
examples of the weak password are stored separately in a text file called weekPasswd.txt. 
The purpose of storage the weak password in a separate file is for convenience the future 
maintenance

Setup instruction:
Part I: Enroll Users
1. Enter the following command and press enter to run the python program for enroll users, 
    Python3 Proactive_Password_Checker_New.py
2. Follow the program concole output, and enter a series of personal information

Part II: Login the System
1. Enter the following command and press enter to run the python program for login users,
    Python3 Password_Verification_Mechanism_ACM.py
2. Enter UserID and passwork to login in the system.

The project is for implement access control in bank's employee system,
The access control follows below rules,
1.    Clients  can  view  their  account  balance,  view  their  investments  portfolio,  and  view  the  contact  details of  their  Financial  Advisor.
2.    Premium  Clients  can  modify  their  investment  portfolio  and  view  the  contact  details  of  their  Financial Planner  and  Investment  Analyst.
3. All SecVault Investments, Inc. employees (expect for Technical Support) can view a client’s account balance and investment portfolio, but only Financial Advisors, Financial Planners, and Investment Analysts can modify a client’s investment portfolio.
5.    Tellers  can  only  access  the  system  during  business  hours  from  9:00AM  to  5:00PM.
6.    Technical   Support   can   view   a   client’s   information   and   request   client   account   access   to   troubleshoot client’s  technical  issues.
7.    Financial  Advisors  and  Financial  Planners  can  view  private  consumer  instruments.
8.    Financial  Planners  can  view  money  market  instruments.
9.    Investment   Analysts   can   view   money   market   instruments,   derivatives   trading,   interest   instruments, and  private  consumer  instruments.
10.    Compliance  Oﬃcers  can  validate  modiﬁcations  to  investment  portfolios.

Below are detail information about the access control mechanism:
Objects:
0.	Client’s Account Balance
1.	Client’s Information
2.	Client’s Account (Assume different with Account Balance and Client’s Information)
3.	Contact details of Client’s Financial Advisor
4.	Contact details of Client’s Financial Planner and Investment Analyst
5.	Investments Portfolio
6.	Private Consumer Instruments
7.	Money Market Instruments
8.	Derivatives Trading
9.	Interest Instruments

Subjects:
0.	Clients
1.	Premium Clients
2.	Tellers
3.	Technical Support
4.	Financial Advisors
5.	Financial Planners
6.	Investment Analysts
7.	Compliance Officers
8.	Others(All employees)

Environment:
1.	Current Time

Access Control Matrix:
*row: object
*column: subject
    0	1	2	3	4	5	6	7	8	9
    
0   V	N	N	V	N	V	N	N	N	N

1	V	N	N	N	V	M	N	N	N	N

2	V	N	N	N	N	V	N	N	N	N

3	N	V	R	N	N	N	N	N	N	N

4	V	N	N	N	N	V	V	N	N	N

5	V	N	N	N	N	M	V	V	N	N

6	V	N	N	N	N	M	V	V	V	V

7	V	N	N	N	N	C	N	N	N	N

8	V	N	N	N	N	V	N	N	N	N

V: View		M: Modify		R: Request Access		C: Check(Validate Modifications)
N: No Access Right		O: Object Attributes		S: Subject Attributes


