#!/usr/bin/env python3

import boto3
import logging

def delete_igw(vpc_resource):
  print("Detach and delete the internet-gateway ")

  igws = vpc_resource.internet_gateways.all()

  if igws:
    for igw in igws:
        print(f"==> Detaching and Deleting igw-id: {igw.id}")
        # igw.detach_from_vpc(
        #   VpcId=vpc_id
        # )
        # igw.delete(
        #   # DryRun=True
        # )

def get_default_subnets(ec2_resource, vpc_resource):
    subnets = vpc_resource.subnets.all()
    default_subnets = []

    for subnet in subnets:
        if subnet.default_for_az:
            default_subnets.append(ec2_resource.Subnet(subnet.id))

    return default_subnets

def is_vpc_in_use(ec2_client, default_subnets):
    print("Checking if VPC is in use by checking whether any of the subnets have resources")
    in_use = False
    for sub in default_subnets:
        nics = ec2_client.describe_network_interfaces(
                        Filters=[
                            {
                                'Name': 'subnet-id',
                                'Values': [sub.id]
                            }
                        ]
                    )

        if len(nics['NetworkInterfaces']) > 0:
            print(f"This VPC is in use. There are resources in Subnet: {sub.id}")
            in_use = True
            break

    return in_use


def delete_subnets(default_subnets):
  print("Delete the subnets ")

  for sub in default_subnets:
    print(f"==> Deleting Subnet: {sub.id}")
    # sub.delete(
    #   # DryRun=True
    # )


def delete_route_tables(vpc_resource):
  print("Delete the route-tables ")

  rtbs = vpc_resource.route_tables.all()

  for rtb in rtbs:
    assoc_attr = rtb.associations_attribute

    for rtb_ass in assoc_attr:
        if rtb_ass['Main'] == True:
            print(f"{rtb.id} is the main route table, continue...")
            continue

        print(f"==> Deleting rtb-id: {rtb.id}")
        table = ec2_resource.RouteTable(rtb.id)
        # table.delete(
        #   # DryRun=True
        # )


def delete_acls(vpc_resource):
  print("Delete the network-access-lists ")

  acls = vpc_resource.network_acls.all()

  for acl in acls:
    if acl.is_default:
      print(f"{acl.id} is the default NACL, continue...")
      continue

    print(f"==> Deleting acl-id: {acl.id}")
    # acl.delete(
    #   # DryRun=True
    # )


def delete_security_groups(vpc_resource):
  print("Delete any security-groups ")

  sgps = vpc_resource.security_groups.all()

  for sg in sgps:
    if sg.group_name == 'default':
      print(f"{sg.id} is the default security group, continue...")
      continue

    print(f"==> Deleting sg-id: {sg.id}")
    # sg.delete(
    #       # DryRun=True
    # )


def delete_vpc(vpc_resource):
  print("Delete the VPC ")

  print(f"==> Deleting vpc-id: {vpc_resource.id}")
  # vpc_resource.delete(
  #   # DryRun=True
  # )

def get_ec2_client(region):
    ec2_client = boto3.client(
        'ec2',
        region_name=region
    )
    return ec2_client

def get_ec2_resource(region):
    ec2_resource = boto3.resource(
        'ec2',
        region_name=region
    )
    return ec2_resource

ec2_client = get_ec2_client("us-east-1")
ec2_resource = get_ec2_resource("us-east-1")

vpcs = ec2_client.describe_vpcs(
        Filters=[
          {
              'Name' : 'isDefault',
              'Values' : ['true'],
          },
        ]
      )

vpc_id = vpcs['Vpcs'][0]['VpcId']

print(f"Region: eu-central-1, DefaultVPCId: {vpc_id}")

vpc_resource = ec2_resource.Vpc(vpc_id)
default_subnets = get_default_subnets(ec2_resource, vpc_resource)

if len(default_subnets) > 0 and is_vpc_in_use(ec2_client, default_subnets):
    print("Noting to do")
    exit()

delete_igw(vpc_resource)
if len(default_subnets) > 0:
    delete_subnets(default_subnets)
delete_route_tables(vpc_resource)
delete_acls(vpc_resource)
delete_security_groups(vpc_resource)
delete_vpc(vpc_resource)
