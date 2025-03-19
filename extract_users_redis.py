import redis
import csv

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Get all key-value pairs from the Redis hash
user_details = r.hgetall('user_details_ON')

# Convert bytes to string
user_details = {key.decode(): value.decode() for key, value in user_details.items()}

# Write to CSV file
with open('userson.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Key', 'Value'])
    for key, value in user_details.items():
        writer.writerow([key, value])
print([1,2,3][2::-1])