#!/usr/bin/python
#Example for GET,POST,PUT request
#Step 1. importing the requests library make sure it is installed in your python enviornment or
# else pip install requests before importing it
#Step 2 Defining  API end point (for POST and PUT) and url (for GET from GIT)
#Step 3 Defining task,task to update to be send to the api
#Step 4 Sending post request  to endpoint 'https://httpbin.org/post'
#Step 5 Sending POST request to rename practice repo to practice_python of GitHub repo
#Step 6 Sending PUT request endpoint to https://httpbin.org/post end point
import requests
import json
API_ENDPOINT = 'https://httpbin.org/post'
API_ENDPOINT_PUT = 'https://httpbin.org/put'
url = 'https://api.github.com/repos/mayababuji/practice'
task = {
  "body": "Great stuff",
  "path": "file1.txt",
  "position": 4,
  "line": None
}
task_updated = {
  "body": "Not Great stuff",
  "path": "file1.txt",
  "position": 4,
  "line": None
}

data = json.dumps({'name':'practice_python', 'description':'all python practice'})

#GET request samples
resp_get = requests.get(url)
text_response = resp_get.text
print("The GET response json value  is {0}".format(json.loads(text_response)))

#POST request samples to https://httpbin.org/post end point
resp_post = requests.post(url=API_ENDPOINT, json=task)
print("The POST response in text format is {0}".format(resp_post.text))
print("The POST response in json format is {0}".format(resp_post.json()))

#POST request sample to rename practice repo to practice_python of GitHub repo
resp_post_git = requests.post(url, data, auth=('user-name','password'))
print(resp_post_git.status_code)

#PUT sample to https://httpbin.org/post end point
resp_put = requests.put(url=API_ENDPOINT_PUT, data=task_updated)
print("The PUT response in json format is {0}".format(resp_put.json()))


