import boto3
from pprint import pprint

session = boto3.session.Session(profile_name="Python-AWS")  ##refered to your user on aws 
cli_obj = session.client(service_name="ec2", region_name="us-east-1")
ec2_service_re = session.resource(service_name='ec2', region_name='us-east-1')
elb_client = boto3.client(service_name='elbv2', region_name='us-east-1')
AS_client = boto3.client(service_name='autoscaling', region_name='us-east-1')
iam_client = boto3.client(service_name='iam', region_name='us-east-1')
RDS_client = boto3.client(service_name='rds', region_name='us-east-1')

'''Creating a VPC using Client Object'''
# New_VPC = cli_obj.create_vpc(CidrBlock='10.0.0.0/16')
# pprint(f"New VPC has been created successfully with id vpc-{New_VPC}")
'''lis Vpc information VPC_ID'''
# existing_VPCs = cli_obj.describe_vpcs()['Vpcs']
# for vpc in existing_VPCs:
#     print(vpc['CidrBlock'],vpc['VpcId'])
''' 1 - list specific VPC-ID'''
response = cli_obj.describe_vpcs(
    VpcIds=[
        'vpc-032bcd0a0a4abb57c',
    ],
)['Vpcs']
''' to iterate on the list to pick a specific data'''
for vpc_id in response:
    print(f"New VPC has been created successfully with id {vpc_id['VpcId']}")
''' detach internet gateway'''
# ''' To delete specific VpcIds'''
# response = cli_obj.delete_vpc(
#     VpcId='vpc-089b06ddbf6818517',  # insert your VPC ID
# )
# print(response)
''' create  subnet in us-east-1a for existing VpcId'''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='10.0.10.0/24',
#     VpcId='vpc-032bcd0a0a4abb57c',
#
#
# )
''' Create  subnet in us-east-1b for existing VpcId'''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1b',
# CidrBlock='10.0.20.0/24',
#     VpcId='vpc-032bcd0a0a4abb57c',
#
# )
''' 2- Describe subnets for specific VpcId '''
# subnet = cli_obj.describe_subnets(
#     Filters=[
#         {
#             'Name': 'vpc-id',
#             'Values': [
#                 'vpc-032bcd0a0a4abb57c',
#             ],
#         },
#     ],
# )['Subnets']
''' save public subnet 1 us-east-1a'''
response = cli_obj.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                'vpc-032bcd0a0a4abb57c',
            ]
        },
    ],
    SubnetIds=[
        'subnet-0d1a3b71bc9877227',
    ],

)['Subnets']
for i_1 in response:
    public_subnet1 = i_1['SubnetId']
''' save public subnet 2 us-east-1b'''
response = cli_obj.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                'vpc-032bcd0a0a4abb57c',
            ]
        },
    ],
    SubnetIds=[
        'subnet-09ecc2de887e16a54',
    ],

)['Subnets']
for i_2 in response:
    public_subnet2 = i_2['SubnetId']
print(f"Public Subnets have been created successfully , their ids are {public_subnet1}] and {public_subnet2}")
# for subnet_id in subnet:
#     print(f"Public Subnets have been created successfully , their ids are {subnet_id['SubnetId']}")

''' 3- Enable Auto-Assign PublicIp for subnet 1 us-east-1a '''
# response = cli_obj.modify_subnet_attribute(
#     MapPublicIpOnLaunch={
#         'Value': True,
#     },
#     SubnetId='subnet-0d1a3b71bc9877227',
# )
#
# print(response)
''' 3- Enable Auto-Assign PublicIp for subnet 2  us-east-1b '''
# response = cli_obj.modify_subnet_attribute(
#     MapPublicIpOnLaunch={
#         'Value': True,
#     },
#     SubnetId='subnet-09ecc2de887e16a54',
# )
#
# print(response)
''' 4- Create private subnets us-east-1a '''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='10.0.100.0/24',
#     VpcId='vpc-032bcd0a0a4abb57c',
#
#
# )
# pprint(response)
''' 4- Create private subnets us-east-1b '''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1b',
#     CidrBlock='10.0.200.0/24',
#     VpcId='vpc-032bcd0a0a4abb57c',
#
#
# )
# pprint(response['SubnetId'])

''' 4- Describe Private subnets private-us-east-1a for specific VpcId '''
''' save private subnet 1 us-east-1a'''
response = cli_obj.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                'vpc-032bcd0a0a4abb57c',
            ]
        },
    ],
    SubnetIds=[
        'subnet-007039bde17cfd379',
    ],

)['Subnets']
for i_1 in response:
    private_subnet1 = i_1['SubnetId']
''' save private subnet 2 us-east-1b'''
response = cli_obj.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                'vpc-032bcd0a0a4abb57c',
            ]
        },
    ],
    SubnetIds=[
        'subnet-0aeca56f64528ef89',
    ],

)['Subnets']
for i_1 in response:
    private_subnet2 = i_1['SubnetId']
print(f"Private Subnets have been created successfully , their ids are {private_subnet1}] and {private_subnet2}")
private_subnet_all = [private_subnet1, private_subnet2]
''' 5- Create the Internet Gateway '''
# response = cli_obj.create_internet_gateway()
# pprint(response)
InternetGatewayId = 'igw-05e1ab0bbaf18c0aa'

''' 6- attach the Internet Gateway to the new VPC '''
# response = cli_obj.attach_internet_gateway(
#     InternetGatewayId=InternetGatewayId,
#     VpcId='vpc-032bcd0a0a4abb57c',
# )
#
# pprint(response)
'''  describes the Internet gateway for the specified VPC.'''
response = cli_obj.describe_internet_gateways(
    Filters=[
        {
            'Name': 'attachment.vpc-id',
            'Values': [
                'vpc-032bcd0a0a4abb57c',
            ],
        },
    ],
)['InternetGateways']
for g in response:
    internet_gateway = g['InternetGatewayId']
''' print the internet gateway id for specific VPC'''
print(f'Internet Gateway has been created successfully , its id is {internet_gateway}')

''' 7- Create route table for public subnets to route traffic through Internet Gateway '''
# response = cli_obj.create_route_table(
#     VpcId='vpc-032bcd0a0a4abb57c',
# )
RT_public = 'rtb-05c595f21794a1483'

''' 8 -Associate public subnets us-east-1a to public route table '''
# response = cli_obj.associate_route_table(
#     RouteTableId=RT_public,
#     SubnetId=public_subnet1,
# )
''' 8- Associate public subnets us-east-1b to public route table '''
# response = cli_obj.associate_route_table(
#     RouteTableId=RT_public,
#     SubnetId=public_subnet2,
# )

''' 9 - add the default route in public route table towards Internet Gateway '''
# response = cli_obj.create_route(
#     DestinationCidrBlock='0.0.0.0/0',
#     GatewayId=internet_gateway,
#     RouteTableId=RT_public,
# )
# pprint(response)
print(f"The New Route Table for public subnets have been created successfully with id {RT_public}")

''' 10- Create NAT Gateway for private subnets '''
my_vpc = 'vpc-032bcd0a0a4abb57c'
''' allocate elastic ip for private subnet us-east-1a '''
# for i in range(1):
#     response = cli_obj.allocate_address(
#         Domain='vpc',
# )['AllocationId']
# Elastic_ip1=response
# print(Elastic_ip1)

''' create NatGateway for public subnet us-east-1a'''
# response = cli_obj.create_nat_gateway(
#     AllocationId=Elastic_ip1,
#     SubnetId=public_subnet1,
# )
'''describe NatGateway for public subnet us-east-1a'''
# response = cli_obj.describe_nat_gateways(
#
#     Filters=[
#         {
#             'Name': 'subnet-id',
#             'Values': [
#                 public_subnet1,
#             ]
#         },
#     ],
# )['NatGateways']
# for i in response:
#     NatGateWay1 = i['NatGatewayId']

''' allocate elastic ip2'''
# for i in range(1):
#     response = cli_obj.allocate_address(
#         Domain='vpc',
#     )['AllocationId']
# Elastic_ip2 = response
# print(Elastic_ip2)

''' create NatGateway for public subnet us-east-1b'''
# response = cli_obj.create_nat_gateway(
#     AllocationId=Elastic_ip2,
#     SubnetId=public_subnet2,
# )
'''describe NatGateway for public subnet us-east-1a'''
# response = cli_obj.describe_nat_gateways(
#
#     Filters=[
#         {
#             'Name': 'subnet-id',
#             'Values': [
#                 public_subnet2,
#             ]
#         },
#     ],
# )['NatGateways']
# for i in response:
#     NatGateWay2 = i['NatGatewayId']
# print(f"Gateways have been created successfully , their ids are {NatGateWay1} and {NatGateWay2} ")

''' 11- Create route table for private subnets to route traffic through NAT Gateway '''
''' for private subnet us-east-1a'''
# response = cli_obj.create_route_table(
#     VpcId=my_vpc,
# )['RouteTable']
#
# rt_pr1=response['RouteTableId']
# print(rt_pr1)
RT_private_subnet_us_east_1a = 'rtb-079a372093bb732d1'
''' for private subnet us-east-1b'''
# response = cli_obj.create_route_table(
#     VpcId=my_vpc,
# )['RouteTable']
#
# rt_pr2=response['RouteTableId']
# print(rt_pr2)
RT_private_subnet_us_east_1b = 'rtb-08b19e91edb3ff437'
''' 12- Associate private subnets to private route table '''
''' associate rt to private -subnet-us-east-1a with Natgateway_id '''
# response = cli_obj.associate_route_table(
#
#     RouteTableId='rtb-079a372093bb732d1',
#     SubnetId='subnet-007039bde17cfd379',
#
# )
''' create Natgateway rout to private us-east-1a'''
# response = cli_obj.create_route(
#     DestinationCidrBlock='0.0.0.0/0',
#     NatGatewayId= NatGateWay1,
#     RouteTableId='rtb-079a372093bb732d1',
#
# )
# pprint(response)
''' 12- Associate private subnets to private route table '''
''' associate rt to private -subnet-us-east-1b with Natgateway_id '''
# response = cli_obj.associate_route_table(
#
#     RouteTableId='rtb-08b19e91edb3ff437',
#     SubnetId='subnet-0aeca56f64528ef89',
#
# )
# pprint(response)
''' create Natgateway rout to private us-east-1b'''
# response = cli_obj.create_route(
#
#     DestinationCidrBlock='0.0.0.0/0',
#     NatGatewayId= NatGateWay2,
#     RouteTableId='rtb-08b19e91edb3ff437',
#
# )
# pprint(response)
print(f"The New Route Tables for Private subnets have been created successfully with ids {RT_private_subnet_us_east_1a}"
      f" and {RT_private_subnet_us_east_1b}")

'''13 - Ensuring NAT Gateway are up and available.'''

# waiter = cli_obj.get_waiter('nat_gateway_available')
# print(" NAT Gateway is being started...... ")
# waiter.wait(NatGatewayIds=[NatGateWay1, ], )
# waiter.wait(NatGatewayIds=[NatGateWay2, ], )
# print("Gateway is now up and available")
''' 14 - add the default route in private route tables towards NAT Gateway '''
''' finished while creating route to private subnet '''
''' 15 - Create the required security group for EC2 instances. '''
# response = cli_obj.create_security_group(
#     Description='Create the required security group for EC2 instances',
#     GroupName='ec2-instance-SG',
#     VpcId=my_vpc,)
# pprint(response)
SG_ec2 = 'sg-02191869363c67b4d'
''' 16- Add security group ingress rules for ports [22,80,443] '''
''' add SG for SSH '''
# response = cli_obj.authorize_security_group_ingress(
#     GroupId=SG_ec2,
#     IpPermissions=[
#         {
#             'FromPort': 22,
#             'IpProtocol': 'tcp',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                     'Description': 'added SSH access from the CidrBlock',
#                 },
#             ],
#             'ToPort': 22,
#         },
#     ],
# )


''' add HTTP for SG '''
# response = cli_obj.authorize_security_group_ingress(
#     GroupId=SG_ec2,
#     IpPermissions=[
#         {
#             'FromPort':80,
#             'IpProtocol': 'tcp',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                     'Description': 'added SSH access from the CidrBlock',
#                 },
#             ],
#             'ToPort': 80,
#         },
#     ],
# )
# pprint(response)
''' add HTTPs for SG '''
# response = cli_obj.authorize_security_group_ingress(
#     GroupId=SG_ec2,
#     IpPermissions=[
#         {
#             'FromPort': 443,
#             'IpProtocol': 'tcp',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                     'Description': 'added SSH access from the CidrBlock',
#                 },
#             ],
#             'ToPort': 443,
#         },
#     ],
# )
# pprint(response)
print(f"Security Group WebSG has been created successfully , its id is {SG_ec2}")

''' 17- add egress rule to the WebSG - allowing traffic for updates and download any required packages. '''
# response = cli_obj.authorize_security_group_egress(
#     GroupId=SG_ec2,
#     IpPermissions=[
#         {
#             'FromPort':-1 ,
#             'IpProtocol': 'icmp',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                 },
#             ],
#             'ToPort': -1,
#         },
#     ],
# )
#
# pprint(response)

''' 18 - Launch EC2 instances in private subnets '''
''' US-EAST-1 in AZ US-EAST-1A'''
userdata_script = '''#!bin/bash

yum update -y

yum install httpd -y

systemctl start httpd# starts httpd service   

systemctl enable httpd# enable httpd to auto-start at system boot

echo " This is server *1* in AWS Region US-EAST-1 in AZ US-EAST-1A " > /var/www/html/index.html'''

instance = cli_obj.run_instances(

    ImageId='ami-05e411cf591b5c9f6',
    InstanceType='t2.micro',
    SecurityGroupIds=[
        'sg-02191869363c67b4d',
    ],

    SubnetId=private_subnet1,
    UserData=userdata_script,
    KeyName='mkN.V',
    MaxCount=1,
    MinCount=1,

)


''' run instance in US-EAST-1 in AZ US-EAST-1B '''
userdata_script = '''#!bin/bash

yum update -y

yum install httpd -y

systemctl start httpd# starts httpd service   

systemctl enable httpd# enable httpd to auto-start at system boot

echo " This is server *2* in AWS Region US-EAST-1 in AZ US-EAST-1B " > /var/www/html/index.html'''

instance = cli_obj.run_instances(

    ImageId='ami-05e411cf591b5c9f6',
    InstanceType='t2.micro',
    SecurityGroupIds=[
        'sg-02191869363c67b4d',
    ],

    SubnetId=private_subnet2,
    UserData=userdata_script,
    KeyName='mkN.V',
    MaxCount=1,
    MinCount=1,

)

''' 19- Ensuring all instances are in running State '''

all_instances = []
response = cli_obj.describe_instances(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                my_vpc,
            ]
        },
    ],

)['Reservations']
'''collecting all available instances '''
for j in response:
    lookfor = j['Instances']
    for l in lookfor:
        all_instances.append(l['InstanceId'])
instance1 = all_instances[0]
instance2 = all_instances[1]
''' print Web and Application instances are being started ...... '''
waiter = cli_obj.get_waiter('instance_running')
print(''' Web and Application instances are being started ...... ''')
waiter.wait(InstanceIds=all_instances)
print("All Instances are running now")
print(f"The new instances for Web and App have been created successfully, their ids are {instance1} and {instance2}")

''' 20 - Create Client Objects for other Services like Load Balancer , Auto Scaling, RDS '''
''' A- Create a client Object for Elastic Load Balancing '''
''' B- Create a client object for Auto Scaling '''
'''  C- Create a client for RDS '''

''' 21 - Create a target group '''

response = elb_client.create_target_group(
    Name='webTG',
    Port=80,
    Protocol='HTTP',
    VpcId=my_vpc,
)['TargetGroups']
for arn in response:
    TG_ARN = arn['TargetGroupArn']
print(f"Target Group has been created successfully , its arn is{TG_ARN}")

''' 22 - Register EC2-targets to the target group '''
response = elb_client.register_targets(
    TargetGroupArn=TG_ARN,
    Targets=[
        {
            'Id': instance1,
        },
        {
            'Id': instance2,
        },
    ],
)
''' 23 - Create an application load balancer  '''
''' A- Create the Load balancer Security Group '''
response = cli_obj.create_security_group(
    Description='My ALB security group',
    GroupName='my-ALB-security-group',
    VpcId=my_vpc,
)
SG_ELB = response['GroupId']
print(f" Security Group ALB_SG for Application Load Balancer has been created successfully , its id is {SG_ELB}")
''' B- add ingress rule to the ALB SG , allowing HTTP Traffic inbound '''
response = cli_obj.authorize_security_group_ingress(
    GroupId=SG_ELB,
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'added HTTP access from the CidrBlock',
                },
            ],
            'ToPort': 80,
        },
    ],
)
''' C- add egress rules to the ALB SG - allowing outbound port 80 towards WebSG security group '''
response = cli_obj.authorize_security_group_egress(
    GroupId=SG_ELB,
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'ToPort': 80,
            'UserIdGroupPairs': [
                {
                    'GroupId': SG_ec2,
                },
            ],
        },
    ],
)
''' D- creating the ALB itself '''
response = elb_client.create_load_balancer(
    Name='ALB',
    Subnets=[public_subnet1,
             public_subnet2, ],

    SecurityGroups=[
        SG_ELB,
    ],
    Scheme='internet-facing',

    Type='application',
    IpAddressType='ipv4',

)['LoadBalancers']
for albarn in response:
    ALB_ARN = albarn['LoadBalancerArn']

''' E- Ensuring Load Balancer is available and up '''
waiter = elb_client.get_waiter('load_balancer_available')
print("Application Load Balancer is being started ......")
waiter.wait(
    LoadBalancerArns=[
        ALB_ARN,
    ], )
print("Load Balancer is up and available now")
print(f"The Application Load Balancer has been created successfully , its arn is {ALB_ARN} ")
''' 24- Create a listener for the load balancer '''
response = elb_client.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': TG_ARN,
            'Type': 'forward',
        },
    ],
    LoadBalancerArn=ALB_ARN,
    Port=80,
    Protocol='HTTP',
)

''' 25- Configure the auto-scaling group '''
'''  A- Create the Launch Configuration '''
# response = AS_client.create_launch_configuration(
#     IamInstanceProfile='arn:aws:iam::790174187069:instance-profile/my_role_asg_ec2',
#     ImageId='ami-06b09bfacae1453cb',
#     InstanceType='t2.micro',
#     LaunchConfigurationName='my-launch-config',
#     SecurityGroups=[
#         SG_ec2,
#     ],
# )

''' B- Crate the auto-scaling group '''
# response = AS_client.create_auto_scaling_group(
#     AutoScalingGroupName='my-auto-scaling-group',
#     LaunchConfigurationName='my-launch-config',
#     MaxInstanceLifetime=2592000,
#     MaxSize=2,
#     MinSize=2,
#     VPCZoneIdentifier='subnet-0aeca56f64528ef89,subnet-007039bde17cfd379',)

''' Describe auto-scaling-groups '''
# response = AS_client.describe_auto_scaling_groups(
#     AutoScalingGroupNames=[
#         'my-auto-scaling-group',
#     ],
# )['AutoScalingGroups']
# for AS in response:
#     ASGARN=AS['AutoScalingGroupARN']
# print(f"The Auto Scaling Group has been created successfully , its arn is {ASGARN}")

''' 26 - create the RDS DataBase and its security group '''
''' A- Create a DB security group '''
# response = cli_obj.create_security_group(
#     Description='Create the required security group for EC2 instances',
#     GroupName='DB_SG',
#     VpcId=my_vpc,)

''' Describe DB SG'''
response = cli_obj.describe_security_groups(

    GroupIds=[
        'sg-0ce1a696abb7b3225',
    ],

)['SecurityGroups']
for sgrds in response:
    DB_RDS_SG = sgrds['GroupId']
print(f"Security Group DB_SG has been created successfully , its id {DB_RDS_SG}")

'''  B- Authorize inbound access to the DB security group from only WebSG security group '''
# response = cli_obj.authorize_security_group_ingress(
#     GroupId=DG_SG,
#     IpPermissions=[
#         {
#             'FromPort': 80,
#             'IpProtocol': 'tcp',
#             'ToPort': 80,
#             'UserIdGroupPairs': [
#                 {
#                     'Description': 'HTTP access from other instances',
#                     'GroupId': SG_ec2,
#                 },
#             ],
#         },
#     ],
# )

'''C - Create the DB Subnet Group'''
''' Create private subnets us-east-1a for RDS '''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='10.0.30.0/24',
#     VpcId=my_vpc,
#
#
# )
'''  Create private subnets us-east-1b for RDS '''
# response = cli_obj.create_subnet(
#     AvailabilityZone='us-east-1b',
#     CidrBlock='10.0.40.0/24',
#     VpcId='vpc-032bcd0a0a4abb57c',
#
#
# )


'''Describe Private subnets private-us-east-1a for specific VpcId '''
''' save private subnet 1 us-east-1a'''
all_RDS_subnet = []
response = cli_obj.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                my_vpc,
            ]
        },
        {
            'Name': 'cidrBlock',
            'Values': [
                '10.0.30.0/24',
                '10.0.40.0/24',
            ]
        }
    ],
)['Subnets']
'''collecting all available RDS subnet for specific cidr '''
for j in response:
    all_RDS_subnet.append(j['SubnetId'])
RDS_subnet1 = all_RDS_subnet[1]
RDS_subnet2 = all_RDS_subnet[0]
''' Now creating subnet group '''
# response = RDS_client.create_db_subnet_group(
#     DBSubnetGroupDescription='My DB subnet group',
#     DBSubnetGroupName='mydbsubnetgroup',
#     SubnetIds=[
#         RDS_subnet1,
#         RDS_subnet2,
#     ],
# )

'''Describe subnet group '''
response = RDS_client.describe_db_subnet_groups(
    DBSubnetGroupName='mydbsubnetgroup',
)['DBSubnetGroups']
for sg in response:
    sg_arn = sg['DBSubnetGroupArn']
print(f"RDS subnet group arn is : {sg_arn}")

''' D- Launch The Multi-AZ RDS database '''
# response = RDS_client.create_db_instance(
#     DBName='test',
#     DBInstanceIdentifier='my-sql-instance',
#     AllocatedStorage=123,
#     DBInstanceClass='db.t2.micro',
#     Engine='MySQL',
#     MasterUsername='admin',
#     MasterUserPassword='admin12345',
#
#     VpcSecurityGroupIds=["sg-0ce1a696abb7b3225"],
#     DBSubnetGroupName='mydbsubnetgroup',
#
#     Port=3306,
#     MultiAZ=True,
#
# )

''' waiter to check the status of th DB'''
# response = RDS_client.describe_db_instances(
#     DBInstanceIdentifier='my-sql-instance',
# )['DBInstances']
#
# waiter = RDS_client.get_waiter('db_instance_available')
# print('''RDS Instance is being started ...... ''')
# waiter.wait(DBInstanceIdentifier='my-sql-instance')
# print("RDS Instance is up and available now")
# for db in response:
#     db_instance_ARN=db['DBInstanceArn']
# print(f"The RDS Instance DB has been created successfully , its arn is {db_instance_ARN}")



