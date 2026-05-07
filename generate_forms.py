import os
import glob
import re

# Template for the form pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[[TITLE]] - PayGain</title>
    <link rel="icon" type="image/png" href="assets/images/Logo.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col">

    <header class="w-full bg-slate-900 shadow-lg py-4 border-b border-slate-800 sticky top-0 z-50">
        <div class="container mx-auto px-6 flex justify-between items-center">
            <a href="index.html" class="flex items-center text-decoration-none">
                <img src="assets/images/pg_logo_no_background.png" alt="PayGain Logo" class="h-10 w-auto object-contain">
            </a>
            <div class="flex items-center gap-4">
                <a href="index.html" class="text-slate-300 hover:text-pink-400 font-semibold transition">
                    <i class="fas fa-arrow-left mr-2"></i> Back to Home
                </a>
                <a href="pulse.html" class="text-slate-300 hover:text-pink-400 font-semibold transition text-sm md:text-base">
                    PayGain Pulse
                </a>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-6 py-12 flex-1 flex items-center justify-center">
        <div class="w-full max-w-2xl bg-white rounded-3xl shadow-xl overflow-hidden border border-slate-100">
            <div class="bg-gradient-to-r from-pink-500 to-rose-500 p-10 text-center relative overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full blur-2xl -mr-10 -mt-10"></div>
                <div class="absolute bottom-0 left-0 w-40 h-40 bg-blue-500/20 rounded-full blur-2xl -ml-10 -mb-10"></div>
                <h1 class="text-3xl md:text-4xl font-bold text-white relative z-10 mb-2">[[HEADING]]</h1>
                <p class="text-pink-100 text-lg relative z-10">[[SUBHEADING]]</p>
            </div>
            <div class="p-10 md:p-12">
                <form onsubmit="handleAnalysisSubmit(event)">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Full Name</label>
                            <input type="text" id="fullName" required placeholder="Enter your full name" class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Mobile Number</label>
                            <input type="tel" id="mobileNumber" required placeholder="+91 XXXXX XXXXX" class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Email Address</label>
                            <input type="email" id="emailAddress" required placeholder="you@example.com" class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">City</label>
                            <input type="text" id="city" required placeholder="e.g. Kolkata" class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Age Group</label>
                            <select id="ageGroup" required class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 bg-slate-50 appearance-none transition cursor-pointer">
                                <option value="" disabled selected>Select Age Group</option>
                                <option value="18-25">18 - 25 Years</option>
                                <option value="26-35">26 - 35 Years</option>
                                <option value="36-45">36 - 45 Years</option>
                                <option value="46-55">46 - 55 Years</option>
                                <option value="55+">55+ Years</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Preferred Time</label>
                            <input type="text" id="preferredTime" placeholder="e.g., Weekdays after 5 PM" class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50">
                        </div>
                    </div>
                    
                    <div class="mb-6">
                        <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Interested In</label>
                        <div class="relative">
                            <select id="interestedProduct" required class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 bg-slate-50 appearance-none transition cursor-pointer">
                                [[OPTIONS]]
                            </select>
                            <div class="absolute inset-y-0 right-0 flex items-center px-5 pointer-events-none text-slate-500"><i class="fas fa-chevron-down"></i></div>
                        </div>
                    </div>

                    <div class="mb-8">
                        <label class="block text-sm font-semibold text-slate-700 mb-2 uppercase tracking-wide">Message / Requirement</label>
                        <textarea id="message" rows="3" placeholder="Tell us more about your needs..." class="w-full px-5 py-4 border border-slate-200 rounded-xl focus:outline-none focus:border-pink-500 focus:ring-4 focus:ring-pink-500/10 transition bg-slate-50"></textarea>
                    </div>

                    <button type="submit" id="submitButton" class="w-full bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white font-bold py-4 rounded-xl shadow-xl shadow-pink-500/30 transition-all transform hover:-translate-y-1 hover:shadow-2xl text-lg flex items-center justify-center gap-2">
                        Submit & Request Callback
                    </button>
                    
                    <div id="success-msg" class="hidden mt-6 p-4 bg-green-50 border border-green-200 text-green-700 rounded-xl text-center text-sm font-medium">
                        Thank you. Our PayGain advisor will contact you shortly to understand your requirement and explain suitable options.
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script>
        async function handleAnalysisSubmit(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitButton');
            const originalText = submitBtn.innerHTML;
            const successMsg = document.getElementById('success-msg');
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> <span>Submitting...</span>';
            submitBtn.classList.add('opacity-75', 'cursor-not-allowed');
            successMsg.classList.add('hidden');
            
            const formData = {
                fullName: document.getElementById('fullName').value,
                mobileNumber: document.getElementById('mobileNumber').value,
                emailAddress: document.getElementById('emailAddress').value,
                city: document.getElementById('city').value,
                interestedProduct: document.getElementById('interestedProduct').value,
                ageGroup: document.getElementById('ageGroup').value,
                preferredTime: document.getElementById('preferredTime').value,
                message: document.getElementById('message').value
            };

            try {
                const response = await fetch('/api/submit-analysis', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();

                if (response.ok) {
                    successMsg.classList.remove('hidden');
                    e.target.reset();
                } else {
                    alert("Error: " + (result.error || "Failed to submit. Please try again."));
                }
            } catch (error) {
                console.error("Submission error:", error);
                alert("An error occurred while submitting. Please try again later.");
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
                submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
            }
        }
    </script>
</body>
</html>
"""

options_dict = {
    'contact.html': ('Book Consultation', 'Get PayGain Guidance', 'Share a few details and our team will contact you.', [
        ('Life Insurance & Family Protection', 'Life Insurance'),
        ('Health Insurance', 'Health Insurance'),
        ('Motor Insurance', 'Motor Insurance'),
        ('Child Future Planning', 'Child Future'),
        ('Retirement / Regular Income', 'Retirement'),
        ('Renewal Support', 'Renewal Support'),
        ('PayGain Advisor / Career', 'Career'),
        ('Structured Financial Opportunities', 'Structured Financial')
    ]),
    'form_life_insurance.html': ('Life Insurance', 'Life Insurance & Family Protection', 'Plan for life coverage and family security.', [('Life Insurance & Family Protection', 'Life Insurance')]),
    'form_health_insurance.html': ('Health Insurance', 'Health Insurance Planning', 'Protect your savings from medical emergencies.', [('Health Insurance', 'Health Insurance')]),
    'form_motor_insurance.html': ('Motor Insurance', 'Motor Insurance Strategy', 'Explore motor insurance planning strategies.', [('Motor Insurance', 'Motor Insurance')]),
    'form_child_future.html': ('Child Future', 'Child Future Planning', 'Prepare for your child’s education and milestones.', [('Child Future Planning', 'Child Future')]),
    'form_regular_income.html': ('Regular Income', 'Regular Income Planning', 'Explore structured financial solutions for regular income.', [('Retirement / Regular Income', 'Retirement')]),
    'form_structured_financial.html': ('Structured Financial', 'Structured Financial Opportunities', 'Understand structured financial options and fixed-income-style benefits.', [('Structured Financial Opportunities', 'Structured Financial')]),
    'form_renewal_support.html': ('Renewal Support', 'Renewal Support', 'Check eligibility for long-term premium continuation support.', [('Renewal Support', 'Renewal Support')])
}

for filename, (title, heading, subheading, options_list) in options_dict.items():
    options_html = ""
    if len(options_list) > 1:
        options_html += '<option value="" disabled selected>Select an Option</option>\n'
    for display, val in options_list:
        options_html += f'                                <option value="{val}">{display}</option>\n'
    
    file_content = template.replace('[[TITLE]]', title).replace('[[HEADING]]', heading).replace('[[SUBHEADING]]', subheading).replace('[[OPTIONS]]', options_html)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print(f"Created {filename}")

# Remove section from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Remove the contact section
contact_section_pattern = re.compile(r'<!-- LEAD CAPTURE FORM -->.*?<!-- DETAILED CORPORATE FOOTER -->', re.DOTALL)
if contact_section_pattern.search(index_content):
    index_content = contact_section_pattern.sub('<!-- DETAILED CORPORATE FOOTER -->', index_content)
    print("Removed contact section from index.html")

# Define all specific link replacements
# Find href="#contact" and replace with specific pages depending on the context
def card_href_replacer(match):
    block = match.group(1)
    if 'Life Insurance' in block: new_href = 'href="form_life_insurance.html"'
    elif 'Regular Income' in block: new_href = 'href="form_regular_income.html"'
    elif 'Child Future' in block: new_href = 'href="form_child_future.html"'
    elif 'Health Insurance' in block: new_href = 'href="form_health_insurance.html"'
    elif 'Motor Insurance' in block: new_href = 'href="form_motor_insurance.html"'
    elif 'Structured Financial' in block: new_href = 'href="form_structured_financial.html"'
    else: new_href = 'href="contact.html"'
    return block + new_href

# For the Solutions Section cards
card_pattern = re.compile(r'(<h3[^>]*>(?:Life Insurance & Family Protection|Regular Income Planning|Child Future Planning|Health Insurance Planning|Motor Insurance Strategy|Structured Financial Opportunities)</h3>.*?)(href="#contact"|href="contact\.html")', re.DOTALL)
index_content = card_pattern.sub(card_href_replacer, index_content)

# For the Renewal Support section
renewal_pattern = re.compile(r'(<h2[^>]*>Worried About Long-Term Premium Commitments\?</h2>.*?)(href="#contact"|href="contact\.html")', re.DOTALL)
def renewal_href_replacer(match):
    return match.group(1) + 'href="form_renewal_support.html"'
index_content = renewal_pattern.sub(renewal_href_replacer, index_content)

# Replace all other #contact with contact.html
index_content = index_content.replace('href="#contact"', 'href="contact.html"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

# Update footers in all HTML files
html_files = glob.glob('*.html')
for f in html_files:
    if f.startswith('form_') or f == 'contact.html': continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace all specific footer links
    content = content.replace('href="index.html#contact">Life Insurance', 'href="form_life_insurance.html">Life Insurance')
    content = content.replace('href="index.html#contact">Regular Income', 'href="form_regular_income.html">Regular Income')
    content = content.replace('href="index.html#contact">Child Future', 'href="form_child_future.html">Child Future')
    content = content.replace('href="index.html#contact">Health Insurance', 'href="form_health_insurance.html">Health Insurance')
    content = content.replace('href="index.html#contact">Motor Insurance', 'href="form_motor_insurance.html">Motor Insurance')
    content = content.replace('href="index.html#contact">Structured Financial', 'href="form_structured_financial.html">Structured Financial')
    
    content = content.replace('href="#contact"', 'href="contact.html"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated links in {f}")

print("Done generating forms and updating links")
