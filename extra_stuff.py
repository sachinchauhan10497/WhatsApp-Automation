import pywhatkit


# pywhatkit.sendwhats_image("+919974663110", 
# 	"chess_tournament_pamplate_1.jpeg", 
# 	"Image Test",
# 	tab_close=True)


# file = open('msg.txt', 'r')
# msg = ''
# for line in file:
# 	msg += line

# print(msg)

import pandas as pd

contacts = {}
contacts_df = pd.read_csv('contacts.csv')
print(contacts_df.columns)
for _,row in contacts_df.iterrows():
	contacts[row['Name']] = row['Number']

print(contacts)

def get_next_time():
	hour, minute, seconds = str(pd.Timestamp.now()).split(' ')[1].split(':')
	hour, minute, seconds = convert_to_int(hour), convert_to_int(minute), convert_to_int(seconds)
	if seconds > 50:
		minute += 1
	minute += 1
	if minute == 60:
		minute = 0
		hour += 1
		hour = hour % 24
	return hour, minute

	# hour, minute = get_next_time()

	# print('Send next Message at: {}: {}'.format(hour, minute))

	# pywhatkit.sendwhatmsg(number, text, hour, minute, 15, True, 3)