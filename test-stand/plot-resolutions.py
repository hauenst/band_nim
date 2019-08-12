from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c):
	return a * np.exp(-b * x) + c



r13089_en = []
r13089_res = []
r772410_en = []
r772410_res = []
r7724100_en = []
r7724100_res = []
r13435_en = []
r13435_res = []
et9214_en = []
et9214_res = []
with open("r13089.txt","rb") as f, open("r7724-10.txt","rb") as g, open("r7724-100.txt","rb") as h,  open("r13435.txt","rb") as i, open("et.txt","rb") as j:
	for line in f:
		parse = line.strip().split(" ")
		r13089_en.append( float(parse[0]) )
		r13089_res.append( float(parse[1]) )
	for line in g:
		parse = line.strip().split(" ")
		r772410_en.append( float(parse[0]) )
		r772410_res.append( float(parse[1]) )
	for line in h:
		parse = line.strip().split(" ")
		r7724100_en.append( float(parse[0]) )
		r7724100_res.append( float(parse[1]) )
	for line in i:
		parse = line.strip().split(" ")
		r13435_en.append( float(parse[0]) )
		r13435_res.append( float(parse[1]) )
	for line in j:
		parse = line.strip().split(" ")
		et9214_en.append( float(parse[0]) )
		et9214_res.append( float(parse[1]) )

r13089_en 	= np.asarray(r13089_en)
r13089_res 	= np.asarray(r13089_res)
r772410_en 	= np.asarray(r772410_en)
r772410_res 	= np.asarray(r772410_res)
r7724100_en 	= np.asarray(r7724100_en)
r7724100_res 	= np.asarray(r7724100_res)
r13435_en 	= np.asarray(r13435_en)
r13435_res 	= np.asarray(r13435_res)
et9214_en 	= np.asarray(et9214_en)
et9214_res 	= np.asarray(et9214_res)

ens = [r772410_en,et9214_en,r13089_en,r7724100_en,r13435_en]
res = [r772410_res,et9214_res,r13089_res,r7724100_res,r13435_res]

ctr=0
colors=['red','blue','orange','dimgrey','darkolivegreen']
labels=['R7724-10 (Chosen)','ET9214 (Chosen)','R13089','R7724-100','R-13435']
for x,y in zip(ens,res):
	popt, pcov = curve_fit(func, x, y, p0 = [900,1,400] )
	xdata = np.linspace(0.3,10,200)
	#plt.plot(xdata, func(xdata, *popt), linestyle='--', label=labels[ctr]+' fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt),color=colors[ctr],linewidth=3)
	if ctr < 2: plt.plot(xdata, func(xdata, *popt), linestyle='-', label=labels[ctr],color=colors[ctr],linewidth=3,zorder=99-ctr)
	else: plt.plot(xdata, func(xdata, *popt), linestyle='--', label=labels[ctr],color=colors[ctr],linewidth=3,zorder=99-ctr)
	#plt.plot(x,y,marker='o',linestyle='',color=colors[ctr])
	plt.ylim([0,900])
	plt.xlim([0.3,2])
	plt.legend(numpoints=1,loc='best',fontsize=14)
	plt.xlabel(r"MeV Energy Deposited",fontsize=17)
	plt.ylabel(r"PMT Resolution",fontsize=17)
	plt.yticks(np.arange(0,901,200))
	plt.xticks(np.arange(0.4,2.1,.4))
	plt.xticks(fontsize=14) 
	plt.yticks(fontsize=14) 
	
	plt.tight_layout()
	
	ctr+=1

plt.savefig("test-resolutions.pdf",bbox_inches="tight")
plt.show()

# R7724-10 Fit:
#	a = 929.521
#	b = 0.664
# 	c = -7.132

# R7724-100 Fit:
#	a = 543.915
#	b = 1.320
# 	c = 173.612

# R13089 Fit:
#	a = 508.809
#	b = 2.536
# 	c = 218.045

# R13435 Fit:
#	a = 1385.174
#	b = 3.112
# 	c = 305.701

# ET9214 Fit:
#	a = 797.049
#	b = 0.706
# 	c = 72.451
