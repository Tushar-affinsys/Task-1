# Task-1

To start with, an user can pass the API request to get the topics in which he might be interested. After choosing the area of interest user can pass the id of the topic as a parameter in the API call.
Moving on, one can select the sub-topic for the queries and pass the id again as a parameter in the request and the user will be shown question.
Further on user can choose from the list of questions presented and select the id of the particular question he wants the answer for and go with the id as a parameter again in the request. Finally user can get the answer for his query. 

Similarly we have other topics as well, like “failed transfer” and “pin blocked”. 

After that we have question under each sub-topic and for each question we have answer mentioned. 

Somehow if the topic he wants to look for is not in the list he can choose the option “Any other” (id = 6), where user can post the question and if there is an existing question same as the user asked then he will be provided with the answer, otherwise that question will be added to our database table and answer has to be added manually, so if someone else asks that or the same usewr asks that again the answer can be provided.
