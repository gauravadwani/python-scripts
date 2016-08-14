import os

path = raw_input('Enter the path of the directory you want to tidy up: (Please ensure that the path ends with a /) ' )

for files in os.listdir(path):
	if os.path.isdir(path+files):
		continue
	else:
		fn,fe=os.path.splitext(files)
		if fe=='':
			if os.path.exists(path+'unknown'):
				os.rename(path+files,path+'unknown/'+files)
			else:
				os.mkdir(path+'unknown')
				os.rename(path+files,path+'unknown/'+files)
		else:
			if os.path.exists(path+fe[1:]):
				os.rename(path+files,path+fe[1:]+'/'+files)
			else:
				os.mkdir(path+fe[1:])
				os.rename(path+files,path+fe[1:]+'/'+files)

print 'Done'

