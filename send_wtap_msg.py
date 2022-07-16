"""Functionality To send Automated WhatsApp Message!"""

import pywhatkit
import pandas as pd


MSG_PATH = 'msg.txt'
IMG_PATH = 'chess_tournament_pamplate_1.jpeg'
CONTACTS_PATH = 'contacts.csv'


def convert_to_int(string):
	return int(round(float(string)))	

def process_number(number):
	# Just sanity check, it should be integer.
	# Otherwise the Exception will be raised.
	number = int(number)
	number = str(number)
	number = number.rstrip()
	if len(number) == 10:
		number = '+91' + str(number)
	if len(number) != 13:
		raise Exception("Invalid Number.")
	return number

def get_msg(name, msg_path, add_greeting=True):
	file = open(msg_path, 'r')
	msg = ''
	if add_greeting:
		msg += 'Hi - ' + '*{}*\n\n'.format(name)
	for line in file:
		msg += line
	return msg

def send_msg(number, text, image_path=None):

	number = process_number(number)

	if image_path:
		pywhatkit.sendwhats_image(number, image_path, text, tab_close=True)
	
	else:
		pywhatkit.sendwhatmsg_to_group_instantly(number, text, tab_close=True)


def read_contacts(contacts_path):
	contacts = {}
	contacts_df = pd.read_csv(contacts_path)
	for _,row in contacts_df.iterrows():
		contacts[row['Number']] = row['Name']
	return contacts


def send_msg_to_all_contacts(contacts, image_path=None, msg_path=MSG_PATH):
	for number, name in contacts.items():

		try:
			print('\n\nSending Message to {}: {}'.format(number, name))

			send_msg(number, get_msg(name, msg_path,
				add_greeting=True), image_path)

			print('Sent to: {}'.format(name))

		except Exception as e:
			print('Exception for {}: {}'.format(number, name))
			print(e)



if __name__ == '__main__':
	send_msg_to_all_contacts(
		contacts=read_contacts(CONTACTS_PATH),
		msg_path=MSG_PATH,
		# image_path=IMG_PATH, 
	)



