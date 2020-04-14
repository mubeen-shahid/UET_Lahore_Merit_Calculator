# Developer:    Mubeen Shahid
# Email:        contact@mubeen.info 
# ebsite:       www.mubeen.info 
# Date:         14.04.2020
# Purpose:      A Python/Tkinter based GUI for calculating 
#               Entry Test marks required against UET Lahore Merit.
# -------
from Tkinter import *
import ttk
import json

from functools import partial
from tkMessageBox import showerror, showinfo
tables = []

class calculate():
	def __init__(self, matric, SSCTotal, fsc, HSSCTotal):
		self.matric = float(matric)
		self.fsc = float(fsc)
		self.SSCTotal = float(SSCTotal)
		self.HSSCTotal = float(HSSCTotal)
		
	def calculateEntryTest(self, target):
		x = float(target) - 0.25*100*self.matric/self.SSCTotal - 0.45 *100*self.fsc/self.HSSCTotal 
		return "%3d"%(int(1.0 + 4*x/0.30))

class merit():
	disciplines =  []
	campuses = []
	categories = []
	meritList = []
	groups = {}
	
	def __init__(self, disp, camp, catg, minAgg):
		self.discipline = str(disp)
		self.campus = str(camp)
		self.category = str(catg)
		self.min_agg = float(minAgg)
		self.target = None 
		merit.disciplines.append(self.discipline)
		merit.campuses.append(self.campus)
		merit.categories.append(self.category)
		merit.meritList.append(self)

	@staticmethod
	def sortByDiscipline():
		merit.meritList.sort(key=lambda m: m.discipline)

	@staticmethod
	def sortByCampus():
		merit.meritList.sort(key=lambda m: m.campus)

	@staticmethod
	def sortByCategory():
		merit.meritList.sort(key=lambda m: m.category)

	@staticmethod
	def sortByAgg():
		merit.meritList.sort(key=lambda m: m.min_agg)
		
	@staticmethod
	def updateMapping():
		def sortedList(l):	return sorted(list(set(l)))
		mapping = { "discipline": sortedList(merit.disciplines),
					"campus":     sortedList(merit.campuses),
					"category":   sortedList(merit.categories),
					"":           sortedList(merit.disciplines) }
		return mapping
	
	@staticmethod
	def groupBy(a, b=None): 
		secSort = False 
		mapping = merit.updateMapping()
		if a in mapping.keys():
			alist = mapping[a]
			if b:
				if b in mapping.keys():
					secSort = True
		else:
			return 0
		for d in alist: # unique list of disciplines, campuses or categories. 
			merit.groups[d] = [] # start with a blank list added to the group dictionary
		for m in merit.meritList:
			merit.groups[getattr(m, a)].append(m) # append the objects to list according to discipline/category/
		if secSort:
			for m in merit.meritList:
				merit.groups[getattr(m, a)].sort(key=lambda x: getattr(x, b))
		else:
			for m in merit.meritList:
				merit.meritList.sort(key=lambda m: m.min_agg)
	
	
	@staticmethod
	def printTable():
		s="%-40s\t%-5s\t%-5s\t%-10s\n"%("DISCIPLINE", "CATGR", "CAMPUS", "AGGREGATE")
		for m in merit.meritList:
			d, cg, ca, agg = m.discipline, m.category, m.campus, m.min_agg
			s += "%-40s\t%-5s\t%-6s\t%-3.3f\n"%(d, cg, ca, agg)
		print s
	
	
merits = """
Discipline	Campus	Category	Minimum Aggregate
Bio-Medical Engineering	KSK	A1	77.525
Mechanical Engineering	LHR	L	76.8113636363636
Mechanical Engineering	LHR	A1	76.5113636363636
Electrical Engineering	LHR	L	76.2431818181818
Electrical Engineering	LHR	A1	74.3454545454545
Civil Engineering	LHR	A1	74.2181818181818
Computer Engineering	LHR	A1	73.75
Electrical Engineering	LHR	N	72.8022727272727
Electrical Engineering	LHR	R	72.7068181818182
Electrical Engineering	LHR	I	72.4757042253521
Civil Engineering	LHR	N	72.3272727272727
Architectural Engineering	LHR	A1	72.1045454545455
Chemical Engineering	LHR	A1	71.9022727272727
Mechanical Engineering	LHR	I	71.6555555555556
Bio-Medical Engineering	KSK	A2	71.5772727272727
Petroleum & Gas Engineering	LHR	A1	71.5522727272727
Mechatronics & Control Engg	LHR	A1	71.5340909090909
Mechanical Engineering	KSK	I	71.4442028985507
Bio-Medical Engineering	NWL	A1	71.1795454545454
Electrical Engineering	KSK	I	71.0679577464789
Electrical Engineering	FSD	I	70.9669014084507
Mechanical Engineering	KSK	A1	70.7
Architecture	LHR	A1	70.5181818181818
Computer Science	LHR	A1	70.4068181818182
Civil Engineering	LHR	I	70.365
Architecture	LHR	N	70.2931818181818
Mechanical Engineering	RCET	I	70.1521739130435
Mechatronics & Control Engg	LHR	I	69.9608638743455
Mechanical Engineering	NWL	I	69.5549295774648
Industrial & Manufacturing Engg	RCET	I	69.5549295774648
Mechatronics & Control Engg	FSD	I	69.4057971014493
Automotive Engineering	LHR	I	69.3760869565217
Chemical Engineering	LHR	I	69.2514705882353
Architectural Engineering	LHR	I	69.185
Electrical Engineering	RCET	I	69.1795774647887
Computer Engineering	LHR	I	69.1300896286812
Architecture	LHR	I	69.125
Transportation Engineering	LHR	I	69.125
Electrical Engineering	NWL	I	69.0989436619718
Industrial & Manufacturing Engg	LHR	I	69.0855072463768
Product & Industrial Design	LHR	I	69.0855072463768
Metallurgical & Materials Engg	LHR	I	68.8061594202898
City & Regional Planning	LHR	A1	68.6022727272727
Electrical Engineering	KSK	A1	68.5545454545455
Industrial & Manufacturing Engg	LHR	A1	68.5068181818182
Automotive Engineering	LHR	A1	68.2181818181818
Metallurgical & Materials Engg	LHR	A1	68.0727272727273
City & Regional Planning	LHR	N	68.025
Computer Engineering	LHR	A2	67.675
Bio-Medical Engineering	KSK	I	67.6359154929578
Chemical Engineering	KSK	I	67.5789855072464
Petroleum & Gas Engineering	LHR	I	67.4544117647059
Polymer Engineering	LHR	I	67.4191176470588
Chemical Engineering	FSD	I	67.0557486631016
Civil Engineering	LHR	A2	67.0159090909091
Mechanical Engineering	LHR	A2	66.7068181818182
Civil Engineering	NWL	A1	66.4795454545455
Chemical Engineering	KSK	A1	66.4113636363636
Mechanical Engineering	LHR	N	66.3681818181818
Environmental Engineering	LHR	A1	66.2340909090909
Computer Science	LHR	I	66.2166666666667
Computer Science	KSK	I	66.0638888888889
Product & Industrial Design	LHR	A1	66.0636363636364
Computer Science	KSK	A1	65.9909090909091
Bio-Medical Engineering	NWL	I	65.7025362318841
Computer Science	NWL	I	65.6478873239437
Transportation Engineering	LHR	A1	65.4522727272727
Mechanical Engineering	LHR	O	65.3227272727273
Polymer Engineering	LHR	A1	65.2613636363636
Mining Engineering	LHR	A1	65.0772727272727
Petroleum & Gas Engineering	LHR	A2	65.0431818181818
Electrical Engineering	LHR	O	64.575
Mechanical Engineering	RCET	A1	64.5113636363636
Architectural Engineering	LHR	A2	64.2340909090909
Mechanical Engineering	NWL	A1	64.1454545454546
Chemical Engineering	LHR	A2	63.9545454545454
Mechatronics & Control Engg	FSD	SI	63.8677536231884
Textile Engineering	FSD	I	63.4545774647887
Geological Engineering	LHR	A1	63.2136363636364
Chemical Engineering	FSD	A1	63.1431818181818
Electrical Engineering	LHR	A2	63.1204545454545
Mechatronics & Control Engg	LHR	A2	62.7909090909091
Mechanical Engineering	KSK	A2	62.7409090909091
Mechanical Engineering	RCET	A2	62.2681818181818
Electrical Engineering	FSD	A1	62.0136363636364
Industrial & Manufacturing Engg	LHR	A2	61.15
Civil Engineering	LHR	P	60.51
Computer Science	LHR	A2	60.0727272727273
Electrical Engineering	RCET	A1	59.6909090909091
Architecture	LHR	A2	59.5204545454545
Electrical Engineering	RCET	A2	59.5159090909091
Electrical Engineering	LHR	S	59.2727272727273
Metallurgical & Materials Engg	LHR	A2	58.8840909090909
Petroleum & Gas Engineering	LHR	SI	58.6985294117647
Mining Engineering	LHR	N	58.6818181818182
Industrial & Manufacturing Engg	RCET	A2	58.2727272727273
Mechatronics & Control Engg	FSD	A1	58.1340909090909
Electrical Engineering	LHR	P	57.993
Mechatronics & Control Engg	LHR	S	57.9340909090909
Computer Science	RCET	A1	57.6931818181818
Electrical Engineering	FSD	P	57.473
City & Regional Planning	LHR	A2	57.2954545454545
Metallurgical & Materials Engg	LHR	N	56.6886363636364
Electrical Engineering	NWL	A1	56.1886363636364
Architecture	LHR	T	55.8795454545455
Electrical Engineering	KSK	A2	55.4613636363636
Geological Engineering	LHR	A2	55.4613636363636
Chemical Engineering	KSK	S	55.3886363636364
Electrical Engineering	KSK	S	55.2136363636364
Computer Science	NWL	A1	55.1386363636364
Civil Engineering	NWL	S	54.8204545454546
Mechanical Engineering	KSK	SI	54.6283582089552
Mechanical Engineering	LHR	P	54.561
Mechanical Engineering	LHR	S	54.2636363636364
Mining Engineering	LHR	I	53.575
Industrial & Manufacturing Engg	LHR	S	53.5613636363636
Mining Engineering	LHR	A2	53.4840909090909
Chemical Engineering	LHR	S	53.3681818181818
Chemical Engineering	LHR	N	52.8977272727273
Petroleum & Gas Engineering	LHR	N	52.8977272727273
Polymer Engineering	LHR	A2	52.75
Automotive Engineering	LHR	A2	52.7318181818182
Architecture	LHR	S	52.6681818181818
Petroleum & Gas Engineering	LHR	S	52.5909090909091
Architectural Engineering	LHR	S	52.5795454545455
Civil Engineering	LHR	S	52.5795454545455
Product & Industrial Design	LHR	A2	52.4818181818182
Chemical Engineering	FSD	A2	52.2068181818182
Mechanical Engineering	KSK	S	52.0818181818182
Civil Engineering	NWL	SI	51.86
Industrial & Manufacturing Engg	RCET	A1	51.8522727272727
Computer Science	KSK	A2	51.8409090909091
Environmental Engineering	LHR	A2	51.6431818181818
Chemical Engineering	FSD	S	51.5704545454545
Electrical Engineering	FSD	A2	50.85
Computer Science	RCET	A2	50.8409090909091
Textile Engineering	FSD	A1	50.8113636363636
Mechatronics & Control Engg	FSD	A2	50.7568181818182
Chemical Engineering	KSK	A2	50.5795454545455
Textile Engineering	FSD	A2	50.4954545454545
Transportation Engineering	LHR	A2	50.3727272727273
"""
lines = [l.split("\t") for l in merits.splitlines()]
for line in lines[2:]:
	if len(line)>3:
		disp, camp, catg, minAgg = line
		m = merit(disp, camp, catg, minAgg)
#


class frame_data():
    # ms: wrapper class to add meta data to parent-widget
    def __init__(self, parent, xitem):
        self.parent = parent
        self._type = xitem
        self._data={}
    def set_val(self, k, v):
        self._data[k]= v 
        return True
    def get_val(self,k):
        return self._data.get(k)
#
def printVar(s):
	print "Selection: ", s.get()
	menu1.set("")
#
def run_code(gui_data):
	data={}
	for k,v in gui_data.iteritems():
		data[k]=v.get()
	print json.dumps(data, indent = 8)
	for k, v in data.iteritems():
		if not v:
			print "--- ERROR: One of the required value in GUI not specified." 
			showerror("ERROR", "The required value of '%s : %s' in GUI not is not specified"%(k,str(v)))
			break 
	
	try:
		if len(tables)>0:
			for table_frame in tables:
				table_frame.grid_remove()
	except:
		print "no existing table found"
	
	table_frame = ttk.LabelFrame(frame_content, borderwidth=5, relief="groove",
				  width=250, height=100, text="  Overview of Merit Requirements  ",
				  labelanchor="n", padding=4)
	tables.append(table_frame)
	merit.groupBy(data["selection"])
	mlist = merit.groups[data["menuItem"]]
	calc = calculate(data["ob_matric"], data["max_matric"], data["ob_fsc"] , data["max_fsc"])
	for m in mlist:
		m.target = calc.calculateEntryTest(m.min_agg)
	# create entries in the frame.
	g = ["discipline","campus","category","min_agg", "target"]
	g.remove(data["selection"])
	table_frame.grid(column=0, row=15, columnspan=4)
	mlist = [m for m in mlist if float(m.target)>0.0]
	mlist.sort(key=lambda m: m.target)
	mlist.reverse()
	for j, y in enumerate(g):
		e = ttk.Entry(table_frame, width=20, font=('Arial', 9, 'bold'))
		e.insert(0, y.upper())
		e.grid(row=0, column=j, columnspan=1)
		e["state"]="readonly"
	for i, m in enumerate(mlist, 1):
		for j, y in enumerate(g):
			v = getattr(m, y)
			e = Entry(table_frame, width=20)
			e.insert(0, v)
			e.grid(row=i, column=j, columnspan=1)
			e["state"]="readonly"
	

#===============================================================================
## ROOT, the Tkinter object
root = Tk()
root.title("UET Merit 2020 Calculation Tool") 
#===============================================================================
## FRAME, the widgets container.
frame_content = ttk.Frame(root,padding="3 3 12 12")

w= ttk.Label(frame_content, text="Python Tkinter based code \nby Mubeen Shahid (contact@mubeen.info)\n")

#===========__MeritCalculation__===============
Aggregate = ttk.LabelFrame(frame_content, borderwidth=5, relief="groove",
                      width=250, height=100, text="  Calculate Aggregate Percentage  ",
                      labelanchor="n", padding=4)

meta_Aggregate = frame_data(Aggregate, "aggregate") 

Label_MaxMarks = ttk.Label(Aggregate, text="Max./Total Marks", foreground='blue', padding=3)
Label_Blank01 = ttk.Label(Aggregate)

Label_FSc = ttk.Label(Aggregate, text="HSSC/FSc part-1:", anchor=E, padding=3)
maxFSc = StringVar()
max_fsc = Entry(Aggregate, textvariable=maxFSc, borderwidth=3, relief=FLAT)
Label_Matric = ttk.Label(Aggregate, text="SSC/Matric:", anchor=E, padding=3)
maxMatric = StringVar()
max_matric = Entry(Aggregate, textvariable=maxMatric, borderwidth=3, relief=FLAT)
x1= ttk.Label(Aggregate)

Label_ObMarks = ttk.Label(Aggregate, text="Obtained Marks", foreground='olive', padding=3)
FSc = StringVar()
ob_fsc = Entry(Aggregate, textvariable=FSc, borderwidth=3, relief=FLAT)
matric = StringVar()
ob_matric = Entry(Aggregate, textvariable=matric, borderwidth=3, relief=FLAT)

Label_Slash00 =  ttk.Label(Aggregate, text=" / ")
Label_Slash01 =  ttk.Label(Aggregate, text=" / ")
Label_Slash02 =  ttk.Label(Aggregate, text=" / ")

x1= ttk.Label(Aggregate)
#===========__Selection__===============
Selection = ttk.LabelFrame(frame_content, borderwidth=5, relief="groove",
                      width=250, height=100, text="  Select Criteria  ",
                      labelanchor="n", padding=4)
selected = StringVar()
meta_Selection = frame_data(Selection, "selection") 
radio1 = ttk.Radiobutton(Selection, text="Discipline", variable=selected, value="discipline", command=partial(printVar, selected))
radio2 = ttk.Radiobutton(Selection, text="Category",   variable=selected, value="category"  , command=partial(printVar, selected))
radio3 = ttk.Radiobutton(Selection, text="Campus",     variable=selected, value="campus"    , command=partial(printVar, selected))

# Populate the pulldown menus
mapping = merit.updateMapping()
label1 = ttk.Label(Selection, text="Select: ")
menu1 = ttk.Combobox(Selection, state="readonly", width=30, values=mapping[selected.get()], postcommand=lambda: menu1.configure(values=mapping[selected.get()]) )

meta_Selection.set_val("textvariable", selected)

x2 = ttk.Label(Selection)

#=======================================
# OK/Cancel Buttons
gui_segments = {
"max_fsc":    maxFSc,
"max_matric": maxMatric,
"ob_fsc":     ob_fsc,
"ob_matric":  ob_matric,
"selection": selected,
"menuItem": menu1
}
RunCancel = ttk.LabelFrame(frame_content, borderwidth=5, relief="groove",
                      width=250, height=50, labelanchor="n", padding=4)
ok     = ttk.Button(RunCancel, text="Calculate", command=partial(run_code, gui_segments))
cancel = ttk.Button(RunCancel, text="Close", command=root.destroy)

#===============WIDGETs Positioning===============
frame_content.grid(column=0, row=0)
w.grid(column=0, row=0)

Aggregate.grid(column=0, row=1, columnspan=6, rowspan=3, sticky=(W, E))

Label_ObMarks.grid( column=1, row=1, columnspan=1)
Label_MaxMarks.grid(column=3, row=1, columnspan=1)

Label_FSc.grid(     column=0, row=3, columnspan=1)
ob_fsc.grid(        column=1, row=3, columnspan=1)
Label_Slash01.grid( column=2, row=3, columnspan=1)
max_fsc.grid(       column=3, row=3, columnspan=1)
Label_Matric.grid(  column=0, row=4, columnspan=1)
ob_matric.grid(     column=1, row=4, columnspan=1)
Label_Slash02.grid( column=2, row=4, columnspan=1)
max_matric.grid(    column=3, row=4, columnspan=1)

x1.grid(column=0, row=5, columnspan=1)

Selection.grid(column=0, row=4, columnspan=6, rowspan=3, sticky=(W, E))
radio1.grid(column=0, row=0, columnspan=1)
radio2.grid(column=1,  row=0, columnspan=1)
radio3.grid(column=2,  row=0, columnspan=1)
x2.grid(column=0, row=1)
label1.grid(column=0, row=2)
menu1.grid(column=1, row=2, columnspan=3)

RunCancel.grid(column=0, row=9, columnspan=6, rowspan=3, sticky=(W, E))
ttk.Label(RunCancel, width=8).grid(column=0, row=2)
ttk.Label(RunCancel, width=8).grid(column=1, row=2)
ok.grid(column=2, row=2)
ttk.Label(RunCancel, width=8).grid(column=3, row=2)
ttk.Label(RunCancel, width=8).grid(column=4, row=2)
cancel.grid(column=5, row=2)
root.mainloop()
