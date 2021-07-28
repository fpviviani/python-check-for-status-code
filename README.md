# python-check-for-status-code
Python3 script that gets a URL list and check for it's status code.

# Usage infos:
Urls will be read by deafault from 'urls.txt' file. You may change origin file by altering line 6.
Put one url in each line, without comma. Just like the examples already inside the file.

Response codes will be written into 'response.txt' file. You may change origin file by altering line 29.
Response are appended in the end of response file, so, if there is already a content in there, it WON'T be overwritten. 
If you want a clean file for current execution, erase all content from 'response.txt'
