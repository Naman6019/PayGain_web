with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_div = '<div class="container mx-auto px-6 py-12 flex-1 flex items-center justify-center">'
new_div = '<div class="container mx-auto px-6 py-12 flex-1 flex flex-col items-center justify-center">'

if old_div in content:
    content = content.replace(old_div, new_div)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed layout in contact.html')
else:
    print('Could not find the target string. Here is the context around it:')
    idx = content.find('flex-1')
    print(content[max(0, idx-100):min(len(content), idx+100)])
