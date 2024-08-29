import boto3

# Initialize a DynamoDB resource object for the specified region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Instantiate a table resource object
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    # Extracting data from the event
    student_id = event.get('student_id')
    sort_key = event.get('sort_key')
    name = event.get('name')
    student_class = event.get('student_class')
    age = event.get('age')

    # Check if the required keys are present
    if not student_id or not sort_key:
        return {
            "statusCode": 400,
            "body": "Missing required keys: student_id and/or sort_key"
        }

    # Inserting data into the table
    table.put_item(
        Item={
            'StudentId': student_id,  # Ensure this matches the key name in your table schema
            'SortKey': sort_key,      # Ensure this matches the key name in your table schema
            'name': name,
            'student_class': student_class,
            'age': age
        }
    )

    return {
        "statusCode": 200,
        "body": "Data inserted successfully"
    }
