class tree_IDS:
	def __init__(self,data=None):
		self.data=data
		self.deep=0
		self.next=None
		self.child=None
		self.left=None
		self.right=None
def insert_child(self, last, data):
		if(self==None):
			return
		if(self.data==last):
			new_node=tree_IDS(data)
			self.child=new_node
			new_node.deep=self.deep+1
			return
		insert_child(self.next,last,data)
		insert_child(self.child, last, data)
def insert_next(self, last, data):
		if(self==None):
			return
		if(self.data==last):
			new_node=tree_IDS(data)
			self.next=new_node
			new_node.deep=self.deep
			return
		insert_next(self.next,last,data)
		insert_next(self.child, last, data)

# tree=tree_IDS("A")

class stack:
	def __init__(self,data=None):
		# self=None
		self.size=0
		self.data=data
		self.next=None	
	def empty(self):
		return self.size==0
	def getData(self): # lấy giá trị trong stack
		return self.data
def pop_stack(st: stack): #trả về con trỏ stack bị đẩy ra
	if(st.size<=1):
		st.size=0
		return st, st.data
	tmp=st
	st=st.next
	# st.size=tmp.size-1
	return st, tmp.data
def push_stack(st, data): # trả về con trỏ stack mới liên
	new_node=stack(data)	#kết với con trỏ next 
	if(st.size==0):
		st=new_node
		st.size+=1
	else:
		new_node.next=st
		new_node.size=st.size+1
		st=new_node
	return st
