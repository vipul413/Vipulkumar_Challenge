This Repo contains two sections:

[1] Python Program to validate the Credit Card Number passed as Standard Input from the terminal

Logic:
This program takes Credit Card number as input and pass it to the function for further restrictions. It checks for below restrictions. 
Remove any extra spaces user has entered
Check if the card number consists only of digits and hyphens
Validate the number of digits (considering potential hyphens)
Check if the card number starts with a valid prefix (4, 5, or 6)
Validate hyphen usage (only one hyphen allowed, separating groups of 4 digits)
Check for consecutive repeated digits (allow leading zeros)

**Pre-Requsite: **
You need to have python installed on your machine to run this. Perform below steps to execute:

git clone https://github.com/vipul413/Vipulkumar_Challenge.git
cd Vipulkumar_Challenge
python3 validate_Credit_Card.py

[2] Use Ansible Configurations to create Amazon Linux EC2 and install Apache Server
It contains two files 
(a) Inventory file (contains EC2 SSH Key & EC2 host details)
(b) Ansible Playbook (Install Apache web server, Start and enable Apache service, Create the Hello World page, Open port 80 for HTTP traffic)

We can enhance the scalability and security of the application by deploying this in private subnet. I've created Custom VPC with private subnet, followed by Creating Launch Config,
Auto Scaling Group, and Load Balancer (Targeted on the private EC2s) 
