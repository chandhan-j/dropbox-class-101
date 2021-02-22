import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Art6AETK1XqtzP-tcXQTRQNXdO66VhgHUnI3aFKF1PMSX05ES3z9niOvc-NVPyYaJSB5WJUHyY0DAUxEVNAxuH9p30f-Y-szisFEAaCM8dnzXKUZBH5NWyLoF1TVKiB7abzQJa8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("Enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()