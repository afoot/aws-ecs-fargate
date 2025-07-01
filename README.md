### Deploy a Microservices Application

## Overview
This lab demonstrates deploying a microservices-based application on AWS using Terraform. The application consists of two microservices: a **frontend** (Node.js) serving a web interface and a **backend** (Python) interacting with DynamoDB for data storage. The microservices run on Amazon ECS with Fargate, are load-balanced using an Application Load Balancer (ALB), and use Amazon ECR for container storage. CloudWatch is integrated for logging.
**Objective**: Deploy a scalable microservices application with ECS Fargate, ALB, and DynamoDB, simulating a production-grade architecture.
**AWS Services Used**: ECS (Fargate), ALB, DynamoDB, ECR, IAM, CloudWatch  
**Prerequisites**:
- AWS account (preferably with Free Tier eligibility)
- Terraform installed
- AWS CLI configured with access keys
- Docker installed
- Basic knowledge of Node.js and Python
## Application Architecture
- **Frontend Microservice**: A Node.js application running on port 3000, serving a simple web page.
- **Backend Microservice**: A Python Flask application running on port 8080, interacting with a DynamoDB table to retrieve order data.
- **ALB**: Routes traffic to the frontend (`/`) and backend (`/api/*`).
- **DynamoDB**: Stores order data for the backend.
- **ECR**: Hosts container images for both microservices.
- **ECS Fargate**: Runs the containerized microservices.
- **CloudWatch**: Collects logs from both services.

## Step-by-Stem Guied
1.  Set Up Environment:
-  Install Terraform: Download from terraform.io.
-  Configure AWS CLI: Run aws configure with your AWS Access Key ID, Secret Access Key, and region (us-east-1).
-  Install Docker for building container images.
2.  Build and Push Container Images:
-  Authenticate Docker to Amazon ECR:
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
```
-  BuilD and push frontend:
```
cd frontend
docker build -t microservices-frontend .
docker tag microservices-frontend:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/microservices-frontend:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/microservices-frontend:latest
```

- Build and push backend:
```
cd frontend
docker build -t microservices-frontend .
docker tag microservices-frontend:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/microservices-frontend:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/microservices-frontend:latest
```

- Replace <account-id> with your AWS account ID.

3. Deploy infractructure:
```
terraform init
terraform plan
terraform apply
```
4. Test the Application:

- Open terraform outputs http://<alb_dns_name> in a browser to see "Hello from Frontend Microservice!"
- Access http://<alb_dns_name>/api/order/1 to test the backend (returns empty initially)
- Populate the DynameDB table with simple data using the AWS CLI:
```
aws dynamodb put-item --table-name Orders --item '{"OrderID: {"S": "1"}, "Product": {"S": "Laptop"}}' --region us-east-1
```
- Retest the backend endpoint to verify the data

5. Monitor Logs:
- Go to Cloudwatch > Log Groups > /ecs/frontend and /ecs/backend to view service logs

6. Clean UP
