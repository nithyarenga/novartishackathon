from bottle import route, run
from bottle import post, get, put, delete
from bottle import response, request
import requests
from json import dumps, loads
import json
import pusher
import random

sample=[{
	"question" : "how many push ups did steve did today?",
	"answer" : ["56"]
},
{
    "question" : "how many calories did you burn last week?",
	"answer" : ["2000"]

}]

result={
	"goals" : ["Steve is 20% to his goal" , "Mark completed his goal of 200 push ups"]
}



@get('/hello')
def hello():
    return "Hello World!"

@get('/questions/<memberId>')
def questions(memberId):
    print memberId
    val = random.randint(0,1)
    print val
    return sample[val]

@get('/goals')
def goals():
    return result


run(host='localhost', port=8089, debug=True)
#run(host='172.30.0.165', port=8089, debug=True)