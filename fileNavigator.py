import os


#lists just the directories in your cwd
def list_directories():
    home = os.getcwd()
    files = os.listdir(home)
    
    dirs =[entry for entry in files if os.path.isdir(entry)]
    
    return dirs

#change directories
def nav_dir(dir_list,target):
    home = os.getcwd()
    
    #print 'available directories: ',dir_list
    if target.lower()== 'back':
        target = ".."
    else:
        while target not in dir_list:
            target = raw_input(' Please enter a valid directory name to navigate\n> ')
    new_dir = home+'/'+target
    os.chdir(new_dir)
    print 'directory changed from',home, '\nto', new_dir,"\n\n"+"---"*20


    
#list file in the cwd
def list_files():
    home = os.getcwd()
    files = os.listdir(home)
    
    files_list = [entry for entry in files if os.path.isfile(entry)]

    return files_list
            
#open file and display content    
def open_file(target):
    print 'Opening file ',target+'\n'
    file_contents=[line for line in open(target,'r')]
    return file_contents

def write_file():
    file_name = raw_input("What file name would you like to write? ")
    write_file=open(file_name,'w')
    lines= raw_input("Write what to a file? ")
    while lines.lower() != 'stop':
        write_file.write(lines)
        lines= raw_input("Write what to a file? OR 'stop' to stop writing: \n> ")
    write_file.close()
    print "Write complete"

    

#main
cmd = ''
print 'Welcome to File Nav.'
print '\n'+'--'*20
count = 0
#create loop
while True:
    home = os.getcwd()
    print 'Your CWD:',home,'\n'+'--'*20
    
    avail_dir = list_directories()
    print 'Directories:',avail_dir,'\n'+'--'*20

    current_files = list_files()
    print 'Current Files:', current_files,"\n"+'--'*20

    #end loop if stop
    cmd = raw_input('Please enter a command (stop, back, write, directory name, or file to open)\n> ')
    count += 1
    if cmd.lower() == 'stop':
        break
    
    #navigation through directories
    if cmd in  avail_dir or cmd == 'back':
        nav_dir(avail_dir,cmd)
    #open files
    elif cmd in current_files:
        text_str = open_file(cmd)
        print text_str,"\n"+"--"*20
    #write to a file
    elif cmd.lower() == 'write':
        write_file()
    #handle bad input...
    else:
        print "invalid choice"
        
    
    
    

#confirm exiting the loop

print "thanks for using file NAV"
print "you entered", count, "commands"   

