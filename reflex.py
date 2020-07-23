f = open("input.txt", "r")
list=f.readlines()
f.close()
list1=[]
for x in list:
      if ',' in x:
        location,status=x.split(",")
        location=location.upper()
        status=status.upper().strip()
        if status == "DIRTY":
          #f1.write("Suck\n")
          list1.append("Suck")
        elif location=="A" :
          #f1.write("Right\n")
          list1.append("Right")
        elif location=="B" :
          #f1.write("Left\n") 
          list1.append("Left")
f1 = open("output.txt","w")    
f1.writelines(["%s\n" % item  for item in list1])   
f1.close()
 
  
