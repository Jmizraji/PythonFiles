# R/W Group Work

class Writer(object):
    def __init__(self,file_name):
        self.file_name = file_name

    def add_text(self,text):
        text_file = open(self.file_name,"a")
        text_file.write(text + "\n") 
        text_file.close()
    
    
class Reader(object):
    def read_text(self,writer):
        try:
            file_name = open(writer.file_name,"r")
        except(IOError):
            print "Cannot open file"
        else:
            print "Reader: Data Found, contents -->"
            contents = file_name.readlines()
            if contents:
                
                for line in contents:
                    print line
                file_name.close()
                file_name = open(writer.file_name,"w")
                file_name.close()
                print "Reader: All data cleared"
            else:
                print "Reader: No Data Found" 
            
            
                
            
        
        





#main
write = Writer("test_file.txt")
read = Reader()

write.add_text("Novel")
write.add_text("Short Story")
read.read_text(write)
read.read_text(write) 
