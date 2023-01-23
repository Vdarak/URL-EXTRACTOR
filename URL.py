import re
# first we open text file then we read the contents 
# and by using findall function to find URLs in the text,
# next we check if any URL is actually present in the given text file.
def find_url(file_path):
    
    with open(file_path, 'r') as file:
        
        text = file.read()
        
        urls = re.findall("(?P<url>https?://[^\s]+)", text)
       
        if len(urls)>0:
            print(f"Occurrence Found: {len(urls)} First Occurrence: {urls[0]}")
        else:
            print("No URL found in the text.")

find_url('/Users/vr/Desktop/Code/my_text_file.txt/')
