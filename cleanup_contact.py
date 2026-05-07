import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure the Preference Share config is correct
preference_config_old = """'preference': {
                title: 'Structured Financial Opportunities',"""

preference_config_new = """'preference': {
                title: 'Preference Share Inquiry',"""

content = content.replace(preference_config_old, preference_config_new)

# Also ensure "passive-income-style benefits" is gone
content = content.replace("passive-income-style benefits", "income-support options")

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("contact.html cleaned up")
