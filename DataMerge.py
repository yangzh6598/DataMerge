#Name:yang zhang
#sectin:A1
#GT email:yzhang3026@gatech.edu
#I work on the homework assignment alone,using this semester"s course materials

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class point:
      def __init__(self,master):
          self.frame1=Frame(root)
          self.frame1.pack()
          

          b1=Button(self.frame1,width=55,text='Load Input CSV File',command=self.loadCSVclicked)
          b1.grid(row=1,column=0,columnspan=2)



          h2=Label(self.frame1,text='File Path')
          h2.grid(row=2,column=1)
          
      
          self.a=Label(self.frame1,text="Input CSV File:")
          self.a.grid(row=3,column=0)

          self.v2=StringVar()
          
          self.a1=Entry(self.frame1,width=50,state='readonly',textvariable=self.v2).grid(row=3,column=1)
          
          self.b=Label(self.frame1,text="Website URL")
          self.b.grid(row=4,column=0)

          self.v3=StringVar()
          
          self.b1=Entry(self.frame1,width=50,textvariable=self.v3).grid(row=4,column=1)
          
          self.c=Label(self.frame1,text="Output CSV File")
          self.c.grid(row=5,column=0)

          self.v4=StringVar()

          self.c1=Entry(self.frame1,width=50,state='readonly',textvariable=self.v4).grid(row=5,column=1)


          h3=Label(self.frame1,text='Number of Animals per exhibit:')
          h3.grid(row=0,column=2)
          
          t1=Label(self.frame1,text='Aquatic')
          t1.grid(row=1,column=2)
          t2=Label(self.frame1,text='Arctic')
          t2.grid(row=2,column=2)
          t3=Label(self.frame1,text='Birds')
          t3.grid(row=3,column=2)
          t4=Label(self.frame1,text='Insects')
          t4.grid(row=4,column=2)
          t5=Label(self.frame1,text='Petting Zoo')
          t5.grid(row=5,column=2)
          t6=Label(self.frame1,text='Rain Forest')
          t6.grid(row=6,column=2)
          t7=Label(self.frame1,text='Reptiles')
          t7.grid(row=7,column=2)
          t8=Label(self.frame1,text='Wonders of Plains')
          t8.grid(row=8,column=2)
          t9=Label(self.frame1,text='Total Number of Animals')
          t9.grid(row=9,column=2)

          for m in range(9):
                Label(self.frame1,text='-').grid(row=m+1,column=3)


  

          self.v1=StringVar()

          self.e1=Entry(self.frame1,width=65,state='readonly',textvariable=self.v1)
          self.e1.grid(row=6,column=0,columnspan=2)
          self.v1.set('Process Data')
          self.e1.config(fg='grey')
      def loadCSVclicked(self):
            self.filename=filedialog.askopenfilename()
            self.v2.set(self.filename)
            
            
            if self.filename[-4:]!='.csv':
                  messagebox.showerror('Exceuse me!','Invalid file!')
                  self.loadCSVclicked()
            else:
                  self.loadCSVfile()
                  b2=Button(self.frame1,text='Process Data',width=55,command=self.PDclicked)
                  b2.grid(row=6,column=0,columnspan=2)
            

            
      def loadCSVfile(self):
          
            import csv
            file=open(self.filename,'r')
            fileread=csv.reader(file)

            
            fileread2=fileread
            self.alist=[]
            for row in fileread:
                  self.alist.append(row)

            del self.alist[0]

                  


      def PDclicked(self):
            
            self.downloadData()
            self.convertHTMLtoCSVFormat()
            self.saveData()
            self.calculate()
      def downloadData(self):
            self.urlin=self.v3.get()
            try:

                  import urllib.request
                  from re import findall
                  response=urllib.request.urlopen(self.urlin)
                  html=response.read()
                  text=html.decode()
                  self.data1=findall("<li>([a-zA-Z '-]+)<br/>([a-zA-Z '-]+)<br/>([a-zA-Z '-]+)</li>",text)
            except:
                  messagebox.showerror('Exceuse me!','Invalid URL!')
                  import sys
                  sys.exit()
                  self.downloadData()
                  
                  
           
      def convertHTMLtoCSVFormat(self):
            self.htlist=[]
            for i in range(len(self.data1)):
                  name=self.data1[i][0]
                  spaceposition=name.find(' ')
                  firstname=name[0:spaceposition]
                  lastname=name[spaceposition+1:]

                  llist=[lastname,firstname,self.data1[i][1],self.data1[i][2]]
                  
                  self.htlist.append(llist)
            self.mergeData() 

         
            

      def mergeData(self):
            for x in range(len(self.htlist)):
                  if self.htlist[x][-1]=='Australian Plains' or self.htlist[x][-1]=='African Plains':
                        self.htlist[x][-1]='The Wonders of the Plains'
                                  
        

            self.datadict={}
            for j in range(len(self.htlist)):
                  fullname=(self.htlist[j][0],self.htlist[j][1])
                  spexh=['-',self.htlist[j][2],self.htlist[j][3]]
                  self.datadict[fullname]=spexh


            #print(self.alist)
            #print(self.htlist)
            for y in range(len(self.alist)):
                  if self.alist[y]==[]:
                        del self.alist[y]


       

            for p in range(len(self.alist)):
                  t=0

                  for y in range(len(self.htlist)):
                  
                        if self.alist[p][0]==self.htlist[y][0] and self.alist[p][1]==self.htlist[y][1]:
                              self.datadict[(self.htlist[y][0],self.htlist[y][1])]=[self.alist[p][2],self.htlist[y][2],self.htlist[y][3]]
                              t=t+1

                  if t==0:
                        self.datadict[(self.alist[p][0],self.alist[p][1])]=[self.alist[p][2],'-','-']

            

      def saveData(self):
            
            
            filename = filedialog.asksaveasfilename()
            #defaultextension=".csv", filetypes=(("ecsv file", "*.csv"),("All Files", "*.*"))

            self.v4.set(filename)

            nameslist=list(self.datadict.keys())
            wholelist=[]

            for g in range(len(nameslist)):
                  costSpacExhi=self.datadict[nameslist[g]]
                  list2=[nameslist[g][0]]+[nameslist[g][1]]+costSpacExhi

                  wholelist.append(list2)


           
        

            for g in range(len(wholelist)):
                  if wholelist[g][-1]=='Australian Plains' or wholelist[g][-1]=='African Plains':
                        wholelist[g][-1]='The Wonders of the Plains'
                        

            
            #wholelist.sort(key=lambda s:(s[-1][0],s[-2][0],s[0],[1]))
            wholelist.sort(key=lambda s:(s[-1],s[-2],s[0],s[1]),reverse=False)
            #print(wholelist)
           

            myfile=open(filename,'w')
            myfile.write('Name,Yearly Cost,Species,Exhibit')
            myfile.write('\n')
            for c in range(len(wholelist)):
                  wholelist2='"'+wholelist[c][0]+','+wholelist[c][1]+'"'+','+wholelist[c][2]+','+wholelist[c][3]+','+wholelist[c][4]
                  myfile.write(wholelist2)
                  myfile.write('\n')
            myfile.close()


      def calculate(self):
           
            totnum=len(list(self.datadict.keys()))
            Label(self.frame1,text=totnum).grid(row=9,column=3)

            dicvalues=list(self.datadict.values())
            a1=0
            a2=0
            a3=0
            a4=0
            a5=0
            a6=0
            a7=0
            a8=0

            for v in range(len(dicvalues)):
                  if dicvalues[v][-1]=='Aquatic':
                        a1=a1+1
                        
                  if dicvalues[v][-1]=='Arctic':
                        a2=a2+1
                        
                  if dicvalues[v][-1]=='Birds':
                        a3=a3+1
                        
                  if dicvalues[v][-1]=='Insects':
                        a4=a4+1
                        
                  if dicvalues[v][-1]=='Petting Zoo':
                        a5=a5+1
                        
                  if dicvalues[v][-1]=='Rain Forest':
                        a6=a6+1
                        
                  if dicvalues[v][-1]=='Reptiles':
                        a7=a7+1
                        
                  if dicvalues[v][-1]=='The Wonders of the Plains':
                        a8=a8+1
                        
                        
            Label(self.frame1,text=a1).grid(row=1,column=3)
            Label(self.frame1,text=a2).grid(row=2,column=3)
            Label(self.frame1,text=a3).grid(row=3,column=3)
            Label(self.frame1,text=a4).grid(row=4,column=3)
            Label(self.frame1,text=a5).grid(row=5,column=3)
            Label(self.frame1,text=a6).grid(row=6,column=3)
            Label(self.frame1,text=a7).grid(row=7,column=3)
            Label(self.frame1,text=a8).grid(row=8,column=3)
 


root=Tk()
p=point(root)
root.mainloop()  
