with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

broken_str = '''</p>
                    <a href="contact.html" class="bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white font-bold py-4 px-8 rounded-full shadow-xl shadow-pink-500/40 hover:-translate-y-1 transition-all inline-block text-center">'''

fixed_str = '''</p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center md:justify-start reveal active" style="transition-delay: 0.3s;">
                        <a href="contact.html" class="bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white font-bold py-4 px-8 rounded-full shadow-xl shadow-pink-500/40 hover:-translate-y-1 transition-all inline-block text-center">'''

content = content.replace(broken_str, fixed_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed missing div in hero')
