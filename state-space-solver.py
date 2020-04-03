def recursive_backtrack(varset: {'var': None}, constrains: 'lambda(varset): bool', domains: {'var'}):
	"""
	A recursive backtrack searching algorithm
	perform search in state (domain) space
	return: varset (with assigned value that satisfies constrains)
	"""
	# 1.return varset if every var have assignment
	if all([i is not None for i in varset.values()]):
		return varset
	# 2.select next-unassigned-var
	var = None
	for i in varset:
		if varset[i] == None:
			var = i
	# 3.for each value in domains
	for value in domains:
		# assign next order-domain-value
		varset[var] = value
		# if constraint is satisfied
		if (constrains(varset)):
			result = recursive_backtrack(varset.copy(), constrains, domains)
			if result is not False:
				return result
			# all childrens of this node is deadend
			# remove assignment
			varset[var] = None
	return False

# australia map coloring
#def australia_map_constraint(varset):
#	australia = {'WA':{'NT','SA'},
#				'NT':{'WA','SA','Q'},
#				'SA':{'WA','NT','Q','NSW','V'},
#				'Q':{'NT','SA','NSW'},
#				'NSW':{'V','SA','Q'},
#				'V':{'SA','NSW'},
#				'T':{}
#	}
#	for k, v in varset.items():
#		if v is None:
#			continue
#		for neighbor in australia[k]:
#			if varset[neighbor] == v:
#				return False # same color as neighbouring state
#	return True # all good, no constraint violation
#res = recursive_backtrack(
#	varset={
#		'WA':None, 'NT':None, 'SA':None, 
#		'Q':None, 'NSW':None, 'V':None, 'T':None
#	},
#	constrains=australia_map_constraint,
#	domains={'Red', 'Green', 'Blue'}
#)

# a college student request
#		 S   E   N   D
# +   	 M   O   R   E
# =  M   O   N   E   Y
#
#varset = {i : None for i in ['S','E','N','D','M','O','R','Y']}
#def constraint(varset):
#	if all([i != None for i in varset.values()]):
#		return\
#		varset['S'] * 1000 + varset['E'] * 100 + varset['N'] * 10 + varset['D'] +\
#		varset['M'] * 1000 + varset['O'] * 100 + varset['R'] * 10 + varset['E']\
#		== varset['M'] * 10000 + varset['O'] * 1000 + varset['N'] * 100 + varset['E'] * 10 + varset['Y']\
#		and varset['S'] != 0 and varset['M'] != 0
#	return True
#domain = {0,1,2,3,4,5,6,7,8,9}
#res = recursive_backtrack(varset, constraint, domain)
#print(res)