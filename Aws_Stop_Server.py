import boto3
import csv
client = boto3.client('ec2')
obj = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
#Create a CSV file with header
with open('stopEC2lis.csv', 'w', newline='') as file:
    header = ["Instance-ID", "InstanceType", "State"]
    writer = csv.DictWriter(file, fieldnames=header)
    #file.close()
    writer.writeheader()
    file.close()

for res in obj['Reservations']:
    for ins in res['Instances']:
        #print(ins['InstanceId'], ins['ImageId'], ins['State']['Name'])
        with open('stopEC2lis.csv', 'a', newline='') as file1:
            csvwriter = csv.writer(file1)
            csvwriter.writerow([ins['InstanceId'], ins['ImageId'], ins['State']['Name']])
        #print(ins['State']['Name'])
file1.close()
print("All server details has been added in CSV file")
