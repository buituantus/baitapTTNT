import Tree_and_stack 
tree=Tree_and_stack.tree_IDS("A")

def ds_tree(tree):
	# Tree_and_stack.insert_child(cây, node trước của cây cần chèn, node cần chèn)
	Tree_and_stack.insert_child(tree,"A","B")
	Tree_and_stack.insert_next(tree,"B", "C")
	Tree_and_stack.insert_next(tree,"C", "D")

	Tree_and_stack.insert_child(tree,"B", "E")
	Tree_and_stack.insert_next(tree,"E", "F")
	Tree_and_stack.insert_child(tree,"C", "G")
	Tree_and_stack.insert_child(tree,"D", "H")
	Tree_and_stack.insert_next(tree,"H", "I")

	Tree_and_stack.insert_child(tree,"E", "J")
	Tree_and_stack.insert_next(tree,"J", "K")
	Tree_and_stack.insert_child(tree,"F", "L")
	Tree_and_stack.insert_next(tree,"L", "M")
	Tree_and_stack.insert_child(tree,"H", "N")
	Tree_and_stack.insert_next(tree,"N", "O")

	Tree_and_stack.insert_child(tree,"K", "P")
	Tree_and_stack.insert_next(tree,"P", "Q")
	Tree_and_stack.insert_child(tree,"M", "R")
	Tree_and_stack.insert_next(tree,"R", "S")
	
	return tree

tree=ds_tree(tree)
def search_IDS(tree, deep: int, value ):
	quaTrinhDuyet=[]
	cap_CanhKe=dict()
	open_stack=Tree_and_stack.stack()
	open_stack=Tree_and_stack.push_stack(open_stack, tree)
	while open_stack.size!=0:
		open_stack, node_tree=Tree_and_stack.pop_stack(open_stack)
		quaTrinhDuyet.append(node_tree.data)
		tmp=node_tree.data
		if(node_tree.data==value):
			cap_CanhKe[value]=[]
			return value, quaTrinhDuyet, cap_CanhKe
		canh_ke=[]
		if(open_stack.getData().deep<deep):
			node_tree=node_tree.child
			
			while(node_tree!=None):
				open_stack=Tree_and_stack.push_stack(open_stack, node_tree)
				canh_ke.append(node_tree.data)
				node_tree=node_tree.next
		cap_CanhKe[tmp]=canh_ke
	return None, None, None

def duyet(a):
	if(a==None):
		return
	if(a.next==None):
		print(a.data)
	else:
		print(a.data, end=" ")
	duyet(a.next)
	duyet(a.child)
def find_duongdi(quaTrinhDuyet, cap_CanhKe, dich):
	tmp=dich
	duong_di=[]
	duong_di.append(dich)
	for i in quaTrinhDuyet:
		if(tmp in cap_CanhKe[i]):
			tmp=i
			duong_di.append(tmp)
	return duong_di[::-1]

deep=int(input("Nhap do sau can tim: "))
dich=input("Nhap dich: ")

for i in range(deep+1):
	check, quaTrinhDuyet, cap_CanhKe =search_IDS(tree, i, dich)
	if(check!=None):
		break

print("quá trình duyệt là:",quaTrinhDuyet)
print(cap_CanhKe)
# print(cap_CanhKe[dich])
print("đường đi:",find_duongdi(quaTrinhDuyet[::-1], cap_CanhKe, dich) )



	

