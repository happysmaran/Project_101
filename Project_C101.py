import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.Al7Fx5mXYh_K2MdQBcmcKdXwgXQRAr7WFo4lkWbJA5PIWz0DOa8e3JfAklWPRT51RVIt7ESX92O7en5D-d-MyeuxNDl-4k0gYWD3ZX6gDVve4eBA8I9QUX9wOir6eaT0yrvT7Hk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to= "/HwTest/test101.txt"

    transferData.upload_file(file_from, file_to)
    print("Done")

main()
