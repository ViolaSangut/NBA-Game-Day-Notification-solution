# DAY 2 DevOps Challange 
# NBA Game Day Notification System

## **Project Overview**
This is a NBA game notification system that allows users to allows users to subscribe to daily game updates. 

## Tools used
1. **Amazon SNS** - This is where we will create a subscription topic where users will subscribe to.
2. **AWS Lambda** - We will create two lambda functions in Python to send game notifications and another to subscribe our users
3. **Amazon EvenBridge** - Help us schedule our game notifications. We will create schedule rules that will trigger our lambda function to send the notifications.
4. **NBA APIs (SportsData.io)** - This will help us pull the games data from the NBA Systems.
5. **API Gateway** - Helps us build an API to expose our backend service to users.
6. **HTML/CSS/JAVASCRIPT** - For the web interface where users enter their email.
   
---



## PART 1: CREATING THE BACKEND SERVICE
1. Create AWS SNS topic in the AWS SNS service.
2. Add an Email subscription to the topic created. A confirmation email will be sent to the email used in the subscription. 
3. Next we need to create a python lambda function that will interract with the NBA API to collect the NBA data, format it, and send it to the subscribed emails in the SNS service.
4. Create an SNS Publish Policy that will allow us to publish to the SNS topic. Copy the gb_sns_policy.json from the repos and use it to create the policy. Set your topic ARN as the resource.
   
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "YOUR SNS TOPIC ARN"
        }
    ]
}
5. Create am AWS IAM role for the lambda function to allow the function to publish to the SNS topic. Attach the previuosly creeated publishing policy and the AWSLambdaBasicExecutionRole policy to the role created. 
6. Create a Free account with subscription at [sportsdata.io](https://sportsdata.io/) and get your API key.
7. Create Environment variables for your Lambda function and add the NBA API key and SNS TOPIC ARN.
  - NBA_API_KEY: your NBA API key.
  - SNS_TOPIC_ARN: SNS TOPIC ARN
8. Create a Schedule rule by navigating to the EventBridge service. Set A CRON Job Schedule for how frequent you want the game updates. Attach the Lambda Function to the schedule rule. 
9. 




## PART 2: CREATING THE FRONTEND WEB UI TO EXPOSE OUR BACKEND TO USERS




## **Technical Architecture**
![nba_API](https://github.com/user-attachments/assets/5e19635e-0685-4c07-9601-330f7d1231f9)



## **Project Structure**
```bash
game-day-notifications/
├── src/
│   ├── gd_notifications.py          # Main Lambda function code
├── policies/
│   ├── gb_sns_policy.json           # SNS publishing permissions
│   ├── gd_eventbridge_policy.json   # EventBridge to Lambda permissions
│   └── gd_lambda_policy.json        # Lambda execution role permissions
├── .gitignore
└── README.md                        # Project documentation
```



### **Deploy the Lambda Function**
1. Open the AWS Management Console and navigate to the Lambda service.
2. Click Create Function.
3. Select Author from Scratch.
4. Enter a function name (e.g., gd_notifications).
5. Choose Python 3.x as the runtime.
6. Assign the IAM role created earlier (gd_role) to the function.
7. Under the Function Code section:
- Copy the content of the src/gd_notifications.py file from the repository.
- Paste it into the inline code editor.
8. Under the Environment Variables section, add the following:

9. Click Create Function.





### **Test the System**
1. Open the Lambda function in the AWS Management Console.
2. Create a test event to simulate execution.
3. Run the function and check CloudWatch Logs for errors.
4. Verify that SMS notifications are sent to the subscribed users.


### **What We Learned**
1. Designing a notification system with AWS SNS and Lambda.
2. Securing AWS services with least privilege IAM policies.
3. Automating workflows using EventBridge.
4. Integrating external APIs into cloud-based workflows.


### **Future Enhancements**
1. Add NFL score alerts for extended functionality.
2. Store user preferences (teams, game types) in DynamoDB for personalized alerts.
3. Implement a web UI
