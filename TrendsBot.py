# This script gets the trending topics from twitter for the past 23 hours. 


import bs4, requests, sys, time    #Import the required modules

def get_trends(url): 		  #Define a function to get the trends
	res=requests.get(url)	  #Download the webpage
	soup=bs4.BeautifulSoup(res.text,"lxml") #Create a BeautifulSoup Object

	lists=soup.find_all("ol",{"class":"trend-card__list"}) #Find all the elements inside the ol tag
	if 'hours' in globals():  #Check whether the variable hours exists
		i=1
		for item in lists[int(hours)].find_all("li"): #Find all elements inside the li tag
			print str(i)+". "+item.text #Print each line inside the li tag
			i=i+1
	else:    					#If hours doesn't exists, then repeat the above
		i=1
		for item in lists[0].find_all("li"): 
			print str(i)+". "+item.text
			i=i+1


print 'Getting trends....\n'

if (len(sys.argv)==2 and sys.argv[1].isdigit()): #Get worldwide trends only based on time
	url="http://trends24.in/"
	hours=sys.argv[1]
	get_trends(url)
elif (len(sys.argv)==1):						#Get current worldwide trends
	url="http://trends24.in"
	get_trends(url)
elif (not sys.argv[-1].isdigit()):				#Get current trends of a place
	url="http://trends24.in/"+'-'.join(sys.argv[1:])
	get_trends(url)
else:											#Get trends of a place based on time
	url="http://trends24.in/"+'-'.join(sys.argv[1:-1])
	hours=sys.argv[-1]
	get_trends(url)









