from delete import service

def CheckFileDir(FileName):
    # page_token = None
    results = service.files().list(q='trashed=false',spaces='drive',fields="nextPageToken, files(id, name)",pageSize=400).execute()
    items = results.get('files', [])

    # print(len(items))
    # for i in items:  
    if not items:
        print('No files found.')
        return None
    else:
        # print('Files:')
        for item in items:
            # print(item['name'])
            if(item['name'] == FileName):
                print(FileName + " is already there")
                # print(item['name'])
                return item['id']
def retrieve_permissions(file_id):
  """Retrieve a list of permissions.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to retrieve permissions for.
  Returns:
    List of permissions.
  """
  try:
    permissions = service.permissions().list(fileId=file_id).execute()
    return permissions.get('permissions', [])
  except Exception as error:
    print('An error occurred: %s' % error)
  return None
def ShareFile(filename,emails):
    file_id = CheckFileDir(filename)
    perm_id = retrieve_permissions(file_id)
    print(perm_id)

    for id in perm_id:
        try:
            service.permissions().delete(fileId=file_id, permissionId=id['id']).execute()
        except Exception as e:
            print("Done deleting...")


    # add emails like this
    try:
        for email in emails:
            new_permission = {
                'type': 'user',
                'role': 'writer',
                'emailAddress': email
                }
            run_new_permission = service.permissions().create(fileId=file_id,sendNotificationEmail=False,body=new_permission).execute()
            print("success : New Email added")
    except Exception as e:
        print("error : cant add new permission")



if __name__ == '__main__':
    emails = ["daniahmedkhatri@gmail.com","something@gmail.com"]
    ShareFile('GS2',emails)
