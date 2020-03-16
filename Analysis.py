import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


# Merge all Run_files into one main_file

## detect the current working directory
path = os.getcwd()

## read the entries
filenames = []
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if 'PrimaryProcesses_Run_' in entry.name:
            #print(entry.name) ## check what files are being read
            filenames.append(entry.name)       

## Merge single files into a main "raw" file
with open('All_Runs_Raw.dat', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
               

## Clear the Words in the main file (except the header because it will be useful for plots)
                
##this program will search and remove specific lines
                
infile = "All_Runs_Raw.dat"
outfile = "All_Runs.dat"

delete_list = ["Processo, RunID, eventID, Energy(MeV), Theta(degree), X(mm), Y(mm), Z(mm), Region \n"]
fin = open(infile)
fout = open(outfile, "w+")
for i, line in enumerate(fin):
    if i>0:                             #does not apply the code in the first line (line 0)
        for word in delete_list:
            line = line.replace(word, '')
    fout.write(line)
fin.close()
fout.close()


##this program will search and remove ALL duplicate lines
                
##lines_seen = set()  # holds lines already seen
##infile = open('All_Runs.dat', "r")
##outfile = open('cleaned_file.dat', "w")
##
##for line in infile:
##    if line not in lines_seen:  # not a duplicate
##        outfile.write(line)
##        lines_seen.add(line)
##outfile.close()



# import data

data = pd.read_csv('All_Runs.dat', sep=",", skipinitialspace=True)
nentries = len(data) # number of entries
#~ data1 = pd.read_csv('PrimaryProcesses_Run_0.dat', sep=",", skipinitialspace=True)
##print data    
Nbins = input("How many bins?")


#plot data

fig = plt.figure(figsize=(5, 5))

plt.figure(1)
plt.polar(data["Theta(degree)"], 'ro')
plt.title('All Runs combined')
#~ plt.legend(['Nentries= '+str(nentries)], loc=0)

plt.figure(2)

plt.hist(data["Theta(degree)"], bins=int(Nbins))
plt.title('All Runs combined')
plt.xlabel('scattering angle, \u03B8 \u00B0')
plt.legend(['Nentries= '+str(nentries)+ '\n' 'Nbins='+str(Nbins)], loc=0)


plt.show()





