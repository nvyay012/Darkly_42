import os

host='10.13.250.217'

os.system(f'wget -r -e robots=off http://{host}/.hidden/')

for root, dirs, files in os.walk(f"./{host}", topdown=False):
   file = open("Big_readme.txt", "a")
   for name in files:
      if name == "README":
         f = open(root+"/"+name, 'r')
         #print(f.read())
         file.write(f.read()+"\n")
         f.close()
   file.close()
