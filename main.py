#!/usr/bin/python

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_ADDRESS=""
GMAIL_PASSWORD=""
SENDER_NAME="Thibaut Forest"
MAX_ITERATIONS=10


Emails={'Emeline':'dummy@email.com','Thibaut':'dummy@email.com','Marine':'dummy@email.com','Francois':'dummy@email.com','Michel':'dummy@email.com','Nathalie':'dummy@email.com','Mamou':'dummy@email.com','Bonne Maman':'dummy@email.com','Alix':'dummy@email.com','Maxence':'dummy@email.com','Philippine':'dummy@email.com'}

Families={'Forest':['Emeline','Thibaut'],'TroisFontaine':['Marine','Francois'],'Forest2':['Michel','Nathalie'],'Forest3':['Philippine'],'Forest4':['Maxence','Alix']
,'Delforges':['Mamou'],'Forest5':['Bonne Maman']}

def Check_deadend(dict_receive,dict_give):
	largest_family_size=0
	largest_family_name=""
	for k,v in dict_receive.iteritems():
		if len(v)>largest_family_size:
			largest_family_size=len(v)
			largest_family_name=k
	
	sum_other_families=0		
	for k,v in dict_give.iteritems():
		if k!=largest_family_name:
			sum_other_families+=len(v)
			
	if (largest_family_size>sum_other_families and largest_family_size>1):
		return True
	else: return False
	
def Check_one_remaining(dict_receive,dict_give):
	receive_remaining=0
	receive_remaining_name=""
	giving_remaining=0
	giving_remaining_name=""
	
	for k,v in dict_receive.iteritems():
		if len(v)>0:
			receive_remaining+=1
			receive_remaining_name=k
			
	for k,v in dict_give.iteritems():
		if len(v)>0:
			giving_remaining+=1
			giving_remaining_name=k
	
	if (receive_remaining==1) and (giving_remaining==1) and (receive_remaining_name==giving_remaining_name):return True
	else:return False
		
def send_email(receiver_email,receiver_name,gift_name):

	
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Christmas Lottery Result"
	msg['From'] = SENDER_NAME
	msg['To'] = receiver_email
	
	# Create the body of the message (a plain-text and an HTML version).

	html = """\
	<html>
	  <head></head>
	  <body>
	    <h2>Hi """ +str(receiver_name)+"""!</h2><br>
	       <h4><i>The christmas lottery has picked someone for you :)
	       This year you have picked :</i></h4>
	       <h2><font color="red">""" +str(gift_name)+"""</font></h2>
	    <img src=http://gif.toutimages.com/images/fete/noel/noel_018.gif >
	  </body>
	</html>
	"""

	part = MIMEText(html, 'html')
	msg.attach(part)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
	s.sendmail(GMAIL_ADDRESS, receiver_email, msg.as_string())
	s.quit()

def dict_to_list(dict):
	list=[]
	for k,v in dict.iteritems():
		for value in v:
			list+=[value]
	return list


def Extract_family(dict):
	Family_list=[]

	while len(Family_list)==0:
		Random_family=random.choice(dict.keys())
		Family_list=dict[Random_family]
		
	return Random_family,Family_list

def Choose_family(dict,name=None,giving=False):

	if not giving:
		Random_family,Family_list=Extract_family(dict)
	else:
		same_family_test=False
		while not (same_family_test):
			Random_family,Family_list=Extract_family(dict)
			if name!=Random_family:same_family_test=True

	return Random_family,Family_list
	
def Remove_from_dict(dict,key,value,list):
	dict[key]=[v for v in list if not v==value]
	return dict


def Plot_connections():
	import matplotlib.pyplot as plt
	
	plt.show()



def Different_person_giving(dict):
	for k,v in dict.iteritems():
		if k==v:
			return False
	return True

def Everyone_giving_receiving(dict,number):
	
	if (len(list(set(dict.keys())))==number and len(list(set(dict.values())))==number):
		return True
	else:
		return False#
	
def Send_emails_to_everyone(dict):
	for k,v in dict.iteritems():
		print "Sending mail to",v,Emails[v]
		send_email(Emails[v],k,v)	
	return

iterations=0

Families_list=dict_to_list(Families)

print "Starting Script\n"
for iteration in range(0,MAX_ITERATIONS):
	
	
	Families_receive=Families.copy()
	Families_give=Families.copy()
	Results={}

	for person in Families_list:
		
		Random_family_receive,Family_list_receive=Choose_family(Families_receive)
	
		Random_person_receive=random.choice(Family_list_receive)
	
		Families_receive=Remove_from_dict(Families_receive,Random_family_receive,Random_person_receive,Family_list_receive)
	
		
		Random_family_give,Family_list_give=Choose_family(Families_give,Random_family_receive,True)
	
		Family_list_give_all=dict_to_list(Families_give)
	
		Random_person_give=Random_person_receive
		while Random_person_give==Random_person_receive:
			Random_person_give=random.choice(Family_list_give)	
			
	
		Families_give=Remove_from_dict(Families_give,Random_family_give,Random_person_give,Family_list_give)
	
		Results[Random_person_receive]=Random_person_give
		
		Deadend=Check_deadend(Families_receive,Families_give)
		Same_person=Check_one_remaining(Families_receive,Families_give)
		
		if Deadend or Same_person: break
	
	if Everyone_giving_receiving(Results,len(Families_list)) and Different_person_giving(Results) and not Deadend and not Same_person :
		print "Lottery finished, sending mails:\n"
		break
		

		
	iterations+=1

#Send_emails_to_everyone(Results)

print "\nScript finished"
