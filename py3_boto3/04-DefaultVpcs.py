#!/usr/bin/env python3

import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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


def main():
    print("Running Main")

    """
      Delete VPC and its corresponding resources in the following order:
      1.) Delete the internet-gateway
      2.) Delete subnets
      3.) Delete route-tables
      4.) Delete network access-lists
      5.) Delete security-groups
      6.) Delete the VPC
    """

    ec2_client = get_ec2_client("us-east-1")
    ec2_regions = ec2_client.describe_regions()["Regions"]
    errored_regions = []
    ok_regions = []

    for aregion in ec2_regions:
        region = aregion['RegionName']
        try:
            ec2_client = get_ec2_client(region)
            ec2_resource = get_ec2_resource(region)

            vpcs = ec2_client.describe_vpcs(
                    Filters=[
                      {
                          'Name' : 'isDefault',
                          'Values' : ['true'],
                      },
                    ]
                  )

            default_vpc_exists = len(vpcs['Vpcs']) > 0

            if default_vpc_exists:
                vpc_id = vpcs['Vpcs'][0]['VpcId']
                vpc_resource = ec2_resource.Vpc(vpc_id)
                default_subnets = get_default_subnets(ec2_resource, vpc_resource)

                print(f"Region: {region}, DefaultVPCId: {vpc_id}")

                if len(default_subnets) > 0 and is_vpc_in_use(ec2_client, default_subnets):
                    raise ValueError('The VPC is in use and cannot be deleted')

                delete_igw(vpc_resource)
                delete_subnets(default_subnets)
                delete_route_tables(vpc_resource)
                delete_acls(vpc_resource)
                delete_security_groups(vpc_resource)
                delete_vpc(vpc_resource)

            else:
                print(f"Region: {region}, DefaultVPCId: No-Default-VPC-Found")

            ok_regions.append(region)

        except Exception as e:
            print(f"Error {region}: {e}")
            errored_regions.append(region)
        finally:
            print ("=========================")

    if len(errored_regions) > 0:
        print(f"Failed in the following regions: {errored_regions}.")
        print(f"But successful in regions: {ok_regions}.")
        return {
            'status': 'amber',
            'info': {
                'enabled': ok_regions,
                'failed': errored_regions
            }
        }
    else:
        print(f"Successful in ALL regions: {ok_regions}.")

    return {
        'status': 'green',
        'info': {
            'enabled': ok_regions
        }
    }

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


def delete_subnets(default_subnets):
  print("Delete the subnets ")

  if len(default_subnets) > 0:
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
            print(f"{rtb.id} is the main route table and can't be deleted, continue...")
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
      print(f"{sg.id} is the default security group and can't be deleted, continue...")
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


main()
