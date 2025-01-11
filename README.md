# DAY 2 DevOps Challange 
# NBA Game Day Notification System

## **Project Overview**
This is a NBA game notification system that allows users to allows users to subscribe to daily game updates. 


## Tools used
1. **Amazon SNS** - This is where we will create a subscription topic where users will subscribe to.
2. **AWS Lambda** - We will create two lambda functions in Python to send game notifications and another to subscribe our users
3. **Amazon EventBridge** - Help us schedule our game notifications. We will create schedule rules that will trigger our lambda function to send the notifications.
4. **NBA APIs (SportsData.io)** - This will help us pull the games data from the NBA Systems.
5. **API Gateway** - Helps us build an API to expose our backend service to users.
6. **HTML/CSS/JAVASCRIPT** - For the web interface where users enter their email.
   
---



## PART 1: CREATING THE BACKEND SERVICE
1. Create AWS SNS topic in the AWS SNS service.
2. Add an Email subscription to the topic created. A confirmation email will be sent to the email used in the subscription.
3. Create an SNS Publish Policy that will allow us to publish to the SNS topic. Copy the gb_sns_policy.json from the repos and use it to create the policy. Set your topic ARN as the resource.
   **"Resource": "YOUR SNS TOPIC ARN"**
   
4. Create am AWS IAM role for the lambda function to allow the function to publish to the SNS topic. Attach the previuosly created publishing policy and the AWSLambdaBasicExecutionRole policy to the role created.
5. Next we need to create a python lambda function that will interract with the NBA API to collect the NBA data, format it, and send it to the subscribed emails in the SNS service. Attach the IAM role created Lambda function created.
6. Create a Free account with subscription at [sportsdata.io](https://sportsdata.io/) and get your API key.
7. Create Environment variables for your Lambda function and add the NBA API key and SNS TOPIC ARN.
   - NBA_API_KEY: your NBA API key.
   - SNS_TOPIC_ARN: SNS TOPIC ARN
8.  Deploy the Lambda function.
9. Create a Schedule rule by navigating to the EventBridge service. Set A CRON Job Schedule for how frequent you want the game updates. Attach the Lambda Function to the schedule rule.
10. Test the Lambda function by running it. the subscribed emails should get game updates in their email when the function is triggered.

# **Subscribing users to the SNS Topic.**
 
 <p>We need to create Function that will help us add subscribers to the SNS topic</p>

1. Create an SNS Subscribe policy. Locate the policy in the repository under the policies folder.
2. Create an IAM role and attach the created policy together with the AWSLambdaBasicExecutionRole policy.
3. Create A Lambda function and copy the code from src/sub_func.py. Attach the created role to the lambda function. This role will allow the lambda function to add email subscribers to the SNS topic.
4. Create an Environment Variable to store the sns topic ARN. (the topic we want to subscribe usrs to).
5. Test the function in the test section by entering an email as an endpoint.
   {
    "endpoint": "test@example.com"
   }

7. The email should receive a confirmation email to sub to the SNS Topic.

<p>So Far we have created a backend service to add subsribers to an SNS Service and another push NBA Updates to the subscribes emails. We finally need to expose these services to users using a frontend service.</p>

1. Navigate to the API Gateway and create a REST API.
2. Create a POST route for the API.
3. Enable CORS for the API to Allow our frontend service to interact with the API.
4. Since our frontend will be running on our local host:
   <P>Add **http://localhost:8080** as the **Access-Control-Allow-Origin**.</P>
   <P>Add  **content-type** as the  **Access-Control-Allow-Headers** .</P>
   <P> Add POST as **Access-Control-Allow-Methods**.</P>
   
5.  Deploy the API under your desired stsge ie test, dev or prod.
6.  Obtain the InvokeURL that we will use to invoke the API in our frontend service.
7.  Navigate to the Test section to test the API. Add the json in the below format in the request body section.
   {
    "endpoint": "test@example.com"
   }
8. The email should receive a confrimation email in their inbox.
9. If that works well you can test the API again on postman to make sure you are getting the confirmation email in your inbox.

# PART 2: CREATING THE WEB UI FOR USERS WITH HTML/CSS/JS 
<p>We need to create a form where users can enter their email to subscribe to the game updates.</p>
   
1. In the sub.html file uder the web_ui folder set the invokeURL.
2. Run a  python local server using the following command:python3 -m http.server 8080
3. Go to the browser and search http://localhost:8080/sub.html.
4. You will view the subscription form , enter an email and click on subscribe. If the set up works well, you should receive a confirmation email in the inbox of the entered email and a message that the email has been sent!!

<p>Visit the following blog for a more detailed workthrough of the project.</p>


### **Future Enhancements**
1. Add NFL score alerts for extended functionality.
2. Store user preferences (teams, game types) in DynamoDB for personalized alerts.

