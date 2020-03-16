#!/usr/bin/env python
import os
import sys
import time
import random
import multiprocessing  # the module we will be using for multiprocessing


start_time = time.time()

def work(Run):
	
	WORKING_DIRECTORY=os.getcwd()
	os.system("./SCXM "+str(Run)+" 0")
	print ("Unit of work number %d" % Run ) # simply print the worker's number


answer = input('Do you wish to overwrite the previous data? y or n:')

if answer == 'y':
	if __name__ == "__main__":  # Allows for the safe importing of the main module
		print("There are %d CPUs on this machine" % multiprocessing.cpu_count())
		number_processes = multiprocessing.cpu_count()-1
		pool = multiprocessing.Pool(number_processes)
		total_tasks = 24000
		tasks = range(total_tasks)
		results = pool.map_async(work, tasks)
		pool.close()
		pool.join()
	
	
	final_time = time.time() - start_time
	hour_conversion = 3600

	print('--- ' + str(final_time / hour_conversion) +' hours ---')
		
		
		
elif answer == 'n':
	sys.exit
	print ('Action aborted')
	
else: print('Please enter y or n')
	


