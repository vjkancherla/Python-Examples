#!/usr/bin/env python3

"""
Add and Retrieve a Paramter in SSM Parameter Store
"""

import json

# def getBranchName():
#     # Opening JSON file
#     f = open('./sns-slack/github-event.json',)
#
#     # returns JSON object as
#     # a dictionary
#     data = json.load(f)
#
#     branch_name = data['ref'].split("/",1)
#
#     print("Branch Name - "+branch_name)
#
#     # Closing file
#     f.close()
#
#     return branch_name
#
#
# def getCodeBuildTriggerId():
#     # Opening JSON file
#     f = open('./sns-slack/codebuild-trigger-response.json',)
#
#     # returns JSON object as
#     # a dictionary
#     data = json.load(f)
#
#     trigger_id = data['build']['id']
#
#     print("CodeBuild trigger id - "+trigger_id)
#
#     # Closing file
#     f.close()
#
#     return trigger_id
#
#
# def putSsmParameter(codebuild_trigger_id, branch_name):
#     parameter_name        = "/tmp/codebuild/"+codebuild_trigger_id
#     parameter_description = "This CodeBuild Trigger Id stores the GitHub Branch Name its working on"
#     parameter_value       = branch_name
#     parameter_type        = "String"
#
#     print("Add SSM Parameter {} with Value {}".format(parameter_name, parameter_value))
#
#     client = boto3.client("ssm", region_name="us-east-1")
#
#     response = client.put_parameter(
#         Name = parameter_name,
#         Description = parameter_description,
#         Value = parameter_value,
#         Type = parameter_type,
#         Tags=[
#             {
#                 'Provider': 'Rackspace',
#                 'Terraform': 'false',
#                 'Created_By': 'Lambda Function',
#                 'Lambda_Function_name': 'MyFunction'
#             },
#         ],
#     )
#
#      if response["Version"] == 1:
#          print("SSM Parameter successfully created")
#      else:
#          print("Failed to create SSM Parameter")


def getBranchNameFromSNSEvent():
    # Opening JSON file
    f = open('./sns-slack/sns-event.json',)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    record = data["Records"][0]
    message = record["Sns"]["Message"]
    message_as_dict = json.loads(message)
    message_detail = message_as_dict["detail"]
    message_detail_additional_info = message_detail["additional-information"]
    codebuild_environment = message_detail_additional_info["environment"]
    codebuild_environment_vars = codebuild_environment["environment-variables"]

    branch_name = "N/A"
    for env_var_dict in codebuild_environment_vars:
        env_var_name = env_var_dict["name"]
        print("Env Var Name - "+env_var_name)
        if env_var_name in ["FEATURE_BRANCH", "STAGING_BRANCH", "PROD_BRANCH"]:
            branch_name = env_var_dict["value"]
            break

    print("Branch_Name - "+branch_name)

    # Closing file
    f.close()



# def getBranchNameFromSNSEvent2():
#
#     # Opening JSON file
#     f = open('./sns-slack/sns-event.json',)
#
#     # returns JSON object as
#     # a dictionary
#     data = json.load(f)
#
#     #formatting event
#     x = data['Records'][0]['Sns']['Message']
#     y = x.replace('\\', '')
#     z = json.loads(y)
#
#     if (z['source'] == 'aws.codebuild'):
#         print('this is a codebuild event')
#     elif (z['source'] == 'aws.codepipeline'):
#         print('this is codepipeline event')
#     else:
#         print('this is not a codebuild or codepipeline event')
#
#     message_detail = z["detail"]
#     message_detail_additional_info = message_detail["additional-information"]
#     codebuild_environment = message_detail_additional_info["environment"]
#     codebuild_environment_vars = codebuild_environment["environment-variables"]
#
#     branch_name = ""
#     for env_var_dict in codebuild_environment_vars:
#         env_var_name = env_var_dict["name"]
#         if env_var_name in ["FEATURE_BRANCH", "STAGING_BRANCH", "PROD_BRANCH"]:
#             branch_name = env_var_dict["value"]
#             break
#
#     print("Branch_Name found - "+branch_name)
#
#     # Closing file
#     f.close()


getBranchNameFromSNSEvent()
