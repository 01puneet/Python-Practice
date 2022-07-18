class length:#Declaring a class
    def __init__(self,list):#Creating a magical method used to provide memory to your objects.
        self.list=list #making the list global-->Referencing 
    def lengthoflist(self):#Creating the method to count length. 
        count=0  #initial count of list is 0
        for i in self.list: #looping the list
            count +=1 #incrementing the list by 1
        print("length of list=",count) #printing the total length
list=[22,33,44,55,66,77] #Declaring a list.
l1=length(list)#creating an object of length class & passing list as argument.
l1.lengthoflist()#calling the method to get the length of list.




