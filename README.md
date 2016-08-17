# python-scripts

1) TidyUp.py - This script moves the files in a folder to new folders based on their extension. Example:
               Suppose a folder 'example' consists of the following files - file1.txt, file2.txt, file3.txt, file4.py, file5.py, file6.py,
               file7.py, file8.mp3, file9.mp3.
               
               Running the script in this folder will result in the creation of three new folders, txt, py and mp3, inisde
               the example folder. The files will be moved inside the respective folders.
               
2) TrendsBot.py - This script gets the list of trending topics on twitter based on place and time. This can get the list for
                  the last 23 hours. To run the script type - 
                  
                  python TrendsBot.py <place> <time>
                  time should be an integer between 0 and 23.
                  
                  "0" gives the current trends and "23" gives the trends from 23 hours back.
                  
                  "place" and "time" are optional. Running the script without "place" and "time" would return the current 
                  worldwide trends.
                  
                  For example, to get the trends from 6 hours back from India, type:
                  
                  python TrendsBot.py India 6
        
