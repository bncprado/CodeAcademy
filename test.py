user_name = ":::::::: Eloise :::::::::::"

print(user_name.strip()) #it does not work because ".strip()" removes blank spaces at the beginning or the end, not in the middle. 

print(user_name.strip(":")) #this will remove the ":", but not the spaces 

print(user_name.strip(":").strip()) #now we have a clean name without the colon and the space