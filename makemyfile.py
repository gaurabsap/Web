import time
import os
# import subprocess


# file_location = str(input("Enter your file full location \n"));
current_location = os.getcwd()


html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Created by python</title>
</head>
<body>
    
</body>
<script src="script.js"></script>
</html>
'''

css = '''* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

'''

# print("Creating html files")
file1 = open(f"{current_location}\index.html", "w")
file1.write(html)
file1.close()

# print("Creating css files")
file2 = open(f"{current_location}\style.css", "w")
file2.write(css)
file2.close()

# print("Creating js files")
file3 = open(f"{current_location}\script.js", "w")
file3.close()

print(current_location)
print(os.system(f'code {current_location}'))
# print("Opening vs code")


# else:
#     file4 = open(f"{file_location}\index.html", "w")
#     file4.write(html)
#     file4.close()

#     file5 = open(f"{file_location}\style.css", "w")
#     file5.write(css)
#     file5.close()

#     file6 = open(f"{file_location}\app.js", "w")
#     file6.close()
#     os.system(f'code {file_location}')
