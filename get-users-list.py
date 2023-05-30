from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

# https://github.com/googleapis/google-api-python-client#maclinux

if __name__ == '__main__':
    SCOPES = [
        'https://www.googleapis.com/auth/admin.directory.user.readonly']
    credentials = service_account.Credentials.from_service_account_file(
        '*****.json', scopes=SCOPES)
    delegated_credentials = credentials.with_subject(
        '*****@*****.jp')
    service = build('admin', 'directory_v1', credentials=delegated_credentials)
    response = service.users().get(userKey='1234567890123456789012').execute()
    print(json.dumps(response))
    pass
