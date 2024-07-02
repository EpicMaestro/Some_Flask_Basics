import mod1
import app
print(f"Running mod2 -( {__name__}) ")

# Every python module is given the inbuilt variable "__name__" . 
# A) When a module is run directly , __name__ variable is given the value "__main__".
# B) When a module is imported into another file , the __name__ variable is given the module name as the value ( mod1 in this case )

#Hence, all the code inside the module that we don't want to be executed when imported in other files are written under :
#     if __name__=="__main__": conditional statement .

# As an example , we import app module to use some of its classes, but in absence of above stmt , the app too would start running which is undesirable . 
