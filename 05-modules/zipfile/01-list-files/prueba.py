from zipfile import ZipFile

# Create a ZipFile Object and load sample.zip in it
with ZipFile('prueba.zip', 'r') as zipObj:
   # Get list of files names in zip
   listOfiles = zipObj.namelist()
   # Iterate over the list of file names in given list & print them
   for elem in listOfiles:
       print(elem)