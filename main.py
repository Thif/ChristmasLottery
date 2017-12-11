#!/usr/bin/python

import random

Families={'Forest':['Emeline','Thibaut'],'TroisFontaine':['Marine','Francois'],'Forest2':['Michel','Nathalie'],'Forest3':['Philippine'],'Forest4':['Maxence','Alix']
,'Delforges':['Mamou'],'Forest5':['Bonne Maman']}


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
	import numpy as np
	import matplotlib.pyplot as plt
	import networkx as nx

	# prepare a random graph with n nodes and m edges
	n = 16
	m = 60
	G = nx.gnm_random_graph(n, m)
	# prepare a circular layout of nodes
	pos = nx.circular_layout(G)
	# define the color to select from the color map
	# as n numbers evenly spaced between color map limits
	node_color = map(int, np.linspace(0, 255, n))
	# draw the nodes, specifying the color map and the list of color
	nx.draw_networkx_nodes(G, pos,
                       node_color=node_color, cmap=plt.cm.hsv)
	# add the labels inside the nodes
	nx.draw_networkx_labels(G, pos)
	# draw the edges, using alpha parameter to make them lighter
	nx.draw_networkx_edges(G, pos, alpha=0.4)
	# turn off axis elements
	plt.axis('off')
	plt.show()






Families_list=dict_to_list(Families)
Families_receive=Families.copy()
Families_give=Families.copy()

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

	print Random_person_receive,"will reveive from",Random_person_give

#Plot_connections()
