# BOT ID is 0 based.
#Assuming there is a file on server positions.csv

path="botPos.csv"

import csv

def init_data(data):
	pass

def send_message(botID, current_pos_x, current_pos_y , movetype):

	if(movetype==1):
		new_pos_x=current_pos_x-1
		new_pos_y=current_pos_y+1
	elif(movetype==2):
		new_pos_y=current_pos_y+1
		new_pos_x=current_pos_x
	elif(movetype==3):
		new_pos_x=current_pos_x+1
		new_pos_y=current_pos_y+1
	elif(movetype==4):
		new_pos_x=current_pos_x+1
		new_pos_y=current_pos_y
	elif(movetype==5):
		new_pos_x=current_pos_x+1
		new_pos_y=current_pos_y-1
	elif(movetype==6):
		new_pos_y=current_pos_y-1
		new_pos_x=current_pos_x
	elif(movetype==7):
		new_pos_x=current_pos_x-1
		new_pos_y=current_pos_y-1
	elif(movetype==8):
		new_pos_x=current_pos_x-1
		new_pos_y=current_pos_y
	else:
		print("Invalid Move!")
		return

	update(botID, new_pos_x, new_pos_y)



def update(botID, new_pos_x, new_pos_y):
	csvFile=open(path, "r")
	data=csv.reader(csvFile)
	csvFile.close()

	data[botID][0]=str(new_pos_x)
	data[botID][1]=str(new_pos_y)

	new_csvFile=open(path, "w")
	csvWriter = csv.writer(new_csvFile, delimiter=',')
	csvWriter.writerows(data)


'''
import pickle

def update(botID, new_pos_x, new_pos_y):
	with open("botPos.pickle", "r") as dataFile:
		data=pickle.load(dataFile)
		data[botID]['x']=new_pos_x
		data[botID]['y']=new_pos_y
		data['score']=data['score']+1

	with open("botPos.pickle", "w") as dataFile:
		pickle.dump(data, dataFile)

'''