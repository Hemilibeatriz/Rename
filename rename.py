import os

def rename(dir):
    count=1
    for file in os.listdir(dir):
        old_path= os.path.join(dir,file)
        new_names= f"folder({count})"
        new_path= os.path.join(dir,new_names)
        os.rename(old_path,new_path)
        count+=1