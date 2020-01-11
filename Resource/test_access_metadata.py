import nbformat as nbf 

ntbk = nbf.read("../Reading_1/Reading_1.ipynb", nbf.NO_CONVERT) 

for cell in ntbk.cells:
	if hasattr(cell.metadata, 'resourcetopic'):
		print(cell.metadata.resourcetopic)
	else:
		print("this cell is not a resource cell")

