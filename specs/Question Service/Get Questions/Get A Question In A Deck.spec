Get A Question using Question Service Specification
===================================================
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_a_question



Get a question using a valid existing cardId
--------------------------------------------
* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Get a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |questionId     |y                  |scenario       |questionId              |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
     |JSON Path                           |Is Data Store Used?|Data Store Type|Data Store Variable Name    |Value                                              |
     |------------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------|
     |$.question.media                    |n                  |               |                            |TEXT                                               |
     |$.question.prompt                   |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _       |
     |$.question.imageUrl                 |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |$.question.promptType               |n                  |               |                            |TEXT                                               |
     |$.kind                              |n                  |               |                            |SHORT_ANSWER                                       |
     |$.learningObjectives[0]             |n                  |               |                            |                                                   |
     |$.tags[0]                           |n                  |               |                            |MaxSoft                                            |
     |$.creatorId                         |n                  |               |                            |osanda12                                           |
     |$.deckId                            |y                  |scenario       |deckId                      |5a603af62e02d86561172dac                           |
     |$.creatoredType                     |n                  |               |                            |Manual                                             |
     |$.creatorPlatform                   |n                  |               |                            |Web                                                |
     |$.creatoredSource                   |n                  |               |                            |App                                                |
     |$.answers.[0].value                 |n                  |               |                            |Osanda Deshan                                      |
     |$.answers.[0].caseSensitive         |n                  |               |                            |false                                              |
     |$.answers.[0].type                  |n                  |               |                            |TEXT                                               |



Get a question using an already deleted cardId
----------------------------------------------
* Given that a user needs to invoke "Get a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |5a0a7bce5ed274e204b95568 |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                             |
     |---------------------------|------------------------------------------------------------------|
     |$.message                  |Couldn't find question with id : 5a0a7bce5ed274e204b95568         |
     |$.description              |null                                                              |
     |$.fieldErrors              |null                                                              |



Get a question using an invalid cardId
--------------------------------------
* Given that a user needs to invoke "Get a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |sfsgsgfsgfsgsgsgfsgfsfgs |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                             |
     |---------------------------|------------------------------------------------------------------|
     |$.message                  |Couldn't find question with id : sfsgsgfsgfsgsgsgfsgfsfgs         |
     |$.description              |null                                                              |
     |$.fieldErrors              |null                                                              |



Get a question using the cardId as empty
----------------------------------------
* Given that a user needs to invoke "Get a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |                         |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |Required String parameter 'deckId' is not present          |
     |$.error                    |Bad Request                                                |
     |$.path                     |/api/questions/                                            |



Get a question without cardId path parameter
--------------------------------------------
* Given that a user needs to invoke "Get a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |Required String parameter 'deckId' is not present          |
     |$.error                    |Bad Request                                                |
     |$.path                     |/api/questions                                             |