#program for writing data into the file
#opening file for write operation
filev=open("firstfile.txt","w")
#writing five sentences into the file
print("enter any five sentence:")
for x in range(5):
  #input of data from user
  sentence=input()
  #writing  sentences into the file
  filev.write(sentence)
  print("--------------------")
  print("data successfully written")
  #closing the file
  filev.close()
