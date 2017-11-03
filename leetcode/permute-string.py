def permute(s):
	lst = []
	_permute(lst, s, "")
	return lst

def _permute(lst, choices, chosen):
	if not choices:
		lst.append(chosen)
	else:
		for i in range(len(choices)):
			_permute(lst, choices[:i] + choices[i + 1:], chosen + choices[i])
