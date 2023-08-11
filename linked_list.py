class node:
    def __init__(self, data):
        self.data=data
        self.next=None
print("insert value  to list node 1")
n=int(input())
head1=node(n)
cur=head1
for i in range(0,3):
    newnode=node(int(input()))
    cur.next=newnode
    cur=cur.next
print("insert value  to list node 2")
n=int(input())
head2=node(n)
cur=head2
for i in range(0,3):
    newnode=node(int(input()))
    cur.next=newnode
    cur=cur.next
str1=''
cur=head1
while cur:
    str1+=str(cur.data)
    cur=cur.next
str2=''
cur=head2
while cur:
    str2+=str(cur.data)
    cur=cur.next
sum_val=int(str1)+int(str2)

final_ans=str(sum_val)
    
result=node(int(final_ans[0]))
cur=result
for i in range(1,len(final_ans)):
    node1=node(int(final_ans[i]))
    cur.next=node1
    cur=cur.next
cur=result
while cur:
    print(cur.data)
    cur=cur.next