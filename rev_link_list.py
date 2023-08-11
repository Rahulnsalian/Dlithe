class node:
    def __init__(self,data):
        self.data=data
        self.next=None
print("enter")
b=int(input())    
head=node(b)
cur=head
for i in range(1,5):
    a=int(input())
    newnode=node(a)
    cur.next=newnode
    cur=cur.next
cur=head
prev=None
while cur:
    nextnode=cur.next
    cur.next=prev
    prev=cur
    cur=nextnode

run=prev
while run:
    print(run.data)
    run=run.next