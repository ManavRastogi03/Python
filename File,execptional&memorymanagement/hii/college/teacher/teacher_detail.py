#why do we need of creating diff script for the student and teacher
#to aintain code ,to improve to understand of the code
#the best practice is to keep diff component it different scripts

#module is the single file (with.py ) extension
#Inside the module function,class ,variable and some other code 
# ex:stu_detail.py and the teacher_detail.py
# 
# Package is the collection of the module orgainzed in directorioes 
# each directories can hove multiple package and python script
#  ex : student and teacher folder is package 
# version 3.3 to amje the package 
# __init__.py in the package(to initilized the pacakge and expose require to the modules )


#library >> pre -written code to perform common task >>collection of multiple pakage
#PANDAS , NUMPY

#importing teacher_detail module fro the teacher package
#from teacher import teacher_detail
import os,sys #provides functionallity to interact with the operarting system
#sys >> provide acess to the system

#__file__ gives you the path to the current script teacher_detailc:\Users\91983\Desktop\Python\File,execptional&memorymanagement\hii\college\teacher\teacher_detail.py
#join >>join two or more path inserting '/' as needed

from os.path import dirname, join, abspath

parent_dir= abspath(join(dirname(__file__), ".."))
sys.path.insert(0,parent_dir)
#set the 0 index add this directory to the begginning of the module search/system path
# it allow to search the module and package 


from student import stu_detail
def teacher():
    print("This is the teacher details")
stu_detail.student()
