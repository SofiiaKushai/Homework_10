# Create a file with some content. As example, you can take this one:

with open('first_file.txt', 'w') as file:
    content = (
        'A man who fears suffering is already '
        'suffering from what he fears.'
    )
    file.write(content)

# Create a second file and copy the content of the first file to the second
# file in upper case.

with open('first_file.txt', 'r') as file:
    original_content = file.read()

with open('second_file.txt', 'w') as file:
    file.write(original_content.upper())
