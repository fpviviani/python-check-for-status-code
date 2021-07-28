import requests
from http.client import responses

def main():
    # Read urls to check for code in .txt file
    urlFile = open('urls.txt', 'r')
    # Goes through each url
    for line in urlFile:
        try:
            url = line.strip()
            # Send request to url
            request = requests.get(url)
            responseCode = request.status_code
            responseUrl = request.url
            # Sometimes the website may redirect you to a 404 response page, in this case, request status code will be 200 (cause the redirect went well). 
            # This check for the redirect url to check if it's a 404 page and change it's response code
            if '404' in responseUrl or ('not' in responseUrl and 'found' in responseUrl):
                responseCode = 404
            message = ("{}:\t\t{}\t\t{}\t\tRedirected to:{}\n".format(url, responseCode, responses[responseCode], responseUrl))
            log(message)
        except Exception as e:
            message = ("Error with {}:\t\t{}\n".format(url, e))
            log(message)
    urlFile.close()

# Append message in log file
def log(message):
    # Open log
    log = open('response.txt', 'a')
    log.write(message)
    # Close the log file
    log.close()

if __name__ == '__main__':
    main()
