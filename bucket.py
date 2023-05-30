from google.cloud import storage

client = storage.Client()

# create a new storage bucket
new_bucket = client.create_bucket('as-you-want') # Bucket name should be Globally unique
