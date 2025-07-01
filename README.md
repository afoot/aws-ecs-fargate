###Deploy a Microservices Application

## Overview
This advanced lab demonstrates deploying a real-world microservices-based application on AWS using Terraform. The application consists of two microservices: a **frontend** (Node.js) serving a web interface and a **backend** (Python) interacting with DynamoDB for data storage. The microservices run on Amazon ECS with Fargate, are load-balanced using an Application Load Balancer (ALB), and use Amazon ECR for container storage. CloudWatch is integrated for logging.
**Objective**: Deploy a scalable microservices application with ECS Fargate, ALB, and DynamoDB, simulating a production-grade architecture.
**AWS Services Used**: ECS (Fargate), ALB, DynamoDB, ECR, IAM, CloudWatch  
**Difficulty**: Advanced  
**Duration**: ~90 minutes  
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
