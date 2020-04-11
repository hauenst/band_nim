import numpy as np
import matplotlib.pyplot as plt
import math

# Read in data
B_field = []
events = []
events_unc = []
cover = []
shield = []
with open("data_sr90_0deg.txt") as f:
	for line in f:
		if '#' in line: continue
#		print line
		line_mod = line.replace("\t", " ")
		parse = line_mod.strip().split(" ")
#Ignoring data points with 2.5 or 10 cm covers		
		if parse[1] == '10' or parse[1] == '2.5': continue
#		print parse
		B_field.append( float(parse[0]) )
		cover.append( float(parse[1])  )
		shield.append( float(parse[2]) )
		events.append( float(parse[3]) )
		events_unc.append( math.sqrt(float(parse[3]) ) )

#print B_field[2:5]
#print events[2:5]

#Filtering of data sets, a
#no shield data cover and shield = 0
res_noshield = []
B_noshield = []
error_noshield = []
#soft iron data 2.5 shield thickness and cover 5
res_softiron = []
B_softiron = []
error_softiron = []
#0.9 mm mu
res_mu09 = []
B_mu09 = []
error_mu09 = []
#1.5 mm mu
res_mu15 = []
B_mu15 = []
error_mu15 = []
#1.8 mm mu
res_mu18 = []
B_mu18 = []
error_mu18 = []
#2.4 mm mu 
res_mu24 = []
B_mu24 = []
error_mu24 = []
#3.0 mm mu
res_mu30 = []
B_mu30 = []
error_mu30 = []

for item in range(len(cover)):
	if (cover[item] == 0) :
		res_noshield.append( 2*events[item])
		error_noshield.append( 2*events_unc[item])
		B_noshield.append( B_field[item])
	if (cover[item] == 5 and shield[item] == 2.5):
		res_softiron.append( events[item])
		error_softiron.append( events_unc[item])
		B_softiron.append( B_field[item])
	if (shield[item] == 0.9):
		res_mu09.append( events[item])
		error_mu09.append( events_unc[item])
		B_mu09.append( B_field[item]+0.5)
	if (shield[item] == 1.5):
		res_mu15.append( events[item])
		error_mu15.append( events_unc[item])
		B_mu15.append( B_field[item]-0.5)
	if (shield[item] == 1.8):
		res_mu18.append( events[item])
		error_mu18.append( events_unc[item])
		B_mu18.append( B_field[item]+1)
	if (shield[item] == 2.4):
		res_mu24.append( events[item])
		error_mu24.append( events_unc[item])
		B_mu24.append( B_field[item] )
	if (shield[item] == 3.0 and events[item]>1000 and B_field[item]>35):
		res_mu30.append( events[item])
		error_mu30.append( events_unc[item])
		B_mu30.append( B_field[item]-1)

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),

     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))
]

plt.figure(1)

plt.errorbar(B_mu15,res_mu15,error_mu15,fmt='o',linestyle=(0, (3, 1, 1, 1, 1, 1)),linewidth=2,color='blue')
plt.errorbar(B_mu18,res_mu18,error_mu18,fmt='s',linestyle='-.',linewidth=2,color='purple')
#plt.errorbar(B_mu30,res_mu30,error_mu30,fmt='o',linestyle='dashdot',linewidth=2,color='darkolivegreen')
plt.errorbar(B_mu24,res_mu24,error_mu24,fmt='v',linestyle='--',linewidth=2,color='orange')
plt.errorbar(B_mu09,res_mu09,error_mu09,fmt='^',linestyle='dotted',linewidth=2,color='red')
#plt.errorbar(B_softiron,res_softiron,error_softiron,fmt='o',linestyle=(0,(5,10)),linewidth=2,color='brown')
plt.errorbar(B_noshield,res_noshield,error_noshield,fmt='o',linestyle='-',color='green',linewidth=2)
#plt.plot(B_softiron,res_softiron,color='orange',linewidth=3)
# Labeling
plt.text(25,5000,"No shield",color='green',fontsize=15)
#plt.text(35,7000,"Softiron",color='orange',fontsize=15)
plt.text(30,10000,"0.9 mm",color='red',fontsize=15)
plt.text(57,5000,"1.5 mm",color='blue',fontsize=15)
plt.text(74,6800,"1.8 mm",color='purple',fontsize=15)
plt.text(65,14000,"2.4 mm ",color='orange',fontsize=15)
# Formatting
#plt.axhline(y=1,linestyle='--',color='black')
plt.xlabel(r"B [gauss]",fontsize=18)
plt.xlim([0,90])
plt.ylim([0,17000])
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xticks(np.linspace(0,80,9))
plt.yticks(np.linspace(0,16000,5))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel(r"Events",fontsize=18,labelpad=16)
plt.tight_layout()
plt.show()

