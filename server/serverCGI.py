import cgi
import json

from topicDependency import generateTDM
from topicDependency import createGraph
from dataGenerator import createDataset

# Send Headers
print ("Content-Type: application/json")
print ("Access-Control-Allow-Origin", "*")
print ("") # Print newline to signify end of headers

inputParams = cgi.FieldStorage()
# inputParams.studentNumber <int>
# inputParams.studentDiversity <int>
# inputParams.questionDifficulty <int>
# inputParams.competencyValue <int>
# inputParams.modelClass <"dynamic" | "static">

# SQA has sid, qid, score
# QT has qid and list of associated topics
SQA, QT =  createDataset(inputParams)
individualData = {
    "name": "Taylor's Data",
    "data": createGraph(inputParams)
}
compareAgainstData = {
    "name": "Class Average",
    "data":  generateTDM(SQA, QT)
}
print json.dumps([individualData, compareAgainstData])
