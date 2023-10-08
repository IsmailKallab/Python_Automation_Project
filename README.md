# Multi-Tier Web Application Deployment

This project, designed by Eng. Ahmad Jalal and produced by Eng. Ismael, outlines the steps to deploy a multi-tier web application within a custom Virtual Private Cloud (VPC) on AWS.

### Requirements

To complete this project, follow the steps below:

### Step 1: Create a Custom VPC

- Create a custom VPC with the CIDR block 10.0.0.0/16.
- Set up 2 public subnets in different availability zones (US-east-1a and US-east-1b) within the US-east-1 region.
  - Subnet ranges: 10.0.10.0/24 and 10.0.20.0/24.
- Ensure that public IP addresses are automatically assigned to EC2 instances in these public subnets.

### Step 2: Configure Private Subnets

- Create 2 private subnets in the same availability zones as above (US-east-1a and US-east-1b).
  - Subnet ranges: 10.0.100.0/24 and 10.0.200.0/24.
- Create separate route tables for the private subnets.

### Step 3: Launch EC2 Instances

- Launch two EBS-backed EC2 instances, one in each of the private subnets created in Step 2 (10.0.100.0/24 and 10.0.200.0/24).
- These instances will serve as the web and application tiers.
- Ensure that EBS volumes of these instances are encrypted at rest.
- Use the provided user data script for instance configuration.

### Step 4: Set Up NAT Gateways

- Launch a NAT gateway in each of the two availability zones (US-east-1a and US-east-1b) to enable the instances to access the internet for updates.
- Adjust the private subnet route tables to route updated traffic through the NAT Gateway.
- Assign a security group named `webSG` to the instances, allowing inbound traffic on ports:
  - SSH (22)
  - HTTP (80)
  - HTTPS (443)

### Step 5: Create Target Group and Auto-Scaling Group

- Create a target group named `webTG` and add the two application instances as targets.
  - Configure the target group to use port 80 (HTTP) for traffic forwarding and health checks.
- Launch an Application Load Balancer (ALB) and enable it in the two public subnets configured in Step 1.
- Adjust the security group of the web/app instances (`webSG`) to allow inbound traffic only from the Application Load Balancer security group (`ALBSG`) as a source.
- Configure the `ALBSG` to:
  - Allow outbound HTTP traffic to `webSG`.
  - Allow inbound traffic from the internet on port HTTP (80).

### Step 6: Configure Auto-Scaling

- Configure a target tracking auto-scaling group for the web/app instances to ensure elasticity and cost-effectiveness.
- The Auto Scaling group should monitor the two instances and be able to add instances on-demand and replace failed instances.

### Step 7: Launch Multi-AZ RDS Database

- Launch a Multi-AZ RDS database and configure its security group to allow access only from the web/app tier security group (`webSG`).

### Step 8: Test Your Deployment

- Test to ensure that you can access the `index.html` message on the instances through the load balancer.
- If everything works as expected, congratulations on completing this amazing AWS project!
