
# This is dynamic code just edit function name and action command on ec2 basis and will work as per your need.
# edit tags as per your need.

def stop_instances():
    ec2 = boto3.client('ec2')
    obj = ec2.describe_instances(Filters=[
                                    {'Name': 'instance-state-name', 'Values': ['stopped']},
                                    {'Name': 'tag:do_not_stop', 'Values': ['true']}
                                ])
    #jj = yaml.safe_load(obj)
    #print(obj)
    for reservation in obj['Reservations']:
        for instance in reservation['Instances']:
            tags = instance["Tags"]
            for tag in tags:
                if((tag['Key'] == 'do_not_stop') and (tag['Value'] == 'true')):
                    print(instance['InstanceId'], instance['State']['Name'])
                #print(tag)
                #print(tag['Value'])
                #print(tag['Key'])
            #else:
            #    print("hello")
            #    #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
if __name__ == '__main__':
    stop_instances()
