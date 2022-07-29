def main():
    outfile=open('data.txt','w')
class student:
    def getstudentdetails(self):
        self.name=input("Enter name: ")
        self.rollno=input("Enter roll no: ")
        self.physics=int(input("Enter number in physics: "))
        self.chemistry=int(input("Enter number in chemistry: "))
        self.math=int(input("Enter number in math: "))
        print("Total number out of 300 is: ",self.physics+self.chemistry+self.math)
        def printdetails(self):
            print(self.name,self.rollno,self.physics,self.chemistry,self.math)
s1=student()
s1.getstudentdetails()
    
