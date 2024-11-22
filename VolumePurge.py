import boto3
import datetime
client = boto3.client('ec2')
resp = client.describe_volumes()
for vol in resp['Volumes']:
    print(vol['VolumeId'], vol['State'], vol['Size'])
#import boto3
dateLimit = datetime.datetime(2024,3,26)
dateToday = datetime.datetime.now()

dateDiff = dateToday - dateLimit
print(dateDiff.days)
print('date diff is %d' % (dateDiff.days))
ec2 = boto3.client('ec2')
jj = ec2.describe_instances()
#for instance in ec2.instances.all():
    #print(instance.id , instance.state)
    #print(instance)
for ins in jj['Reservations']:
    for list in ins['Instances']:
        #print(list['LaunchTime'])
        a = (list['LaunchTime'])
        b = a.date()
        print(a.date())
        c = datetime.datetime.now().date()
        print(c)
        j = c - b
        print(j.days)
        if (dateDiff.days < j.days):
            print("Snapshot need to be deleted")
        else:
            print("Don't delete the snapshots")
