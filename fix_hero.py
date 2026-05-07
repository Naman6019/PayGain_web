import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update hero buttons and add microcopy
old_hero_buttons = """<a href="contact.html" class="bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white font-bold py-4 px-8 rounded-full shadow-xl shadow-pink-500/40 hover:-translate-y-1 transition-all inline-block text-center">
                            Book Free Consultation
                        </a>
                        <a href="https://wa.me/910000000000" class="flex items-center justify-center gap-2 text-white font-semibold py-4 px-8 rounded-full border border-slate-600 hover:bg-white/10 transition-all text-center">
                            <i class="fab fa-whatsapp text-green-400 text-xl"></i> Check Eligibility
                        </a>
                    </div>"""

new_hero_buttons = """<a href="contact.html" class="bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white font-bold py-4 px-8 rounded-full shadow-xl shadow-pink-500/40 hover:-translate-y-1 transition-all inline-block text-center">
                            Check Eligibility
                        </a>
                        <a href="https://wa.me/910000000000" class="flex items-center justify-center gap-2 text-white font-semibold py-4 px-8 rounded-full border border-slate-600 hover:bg-white/10 transition-all text-center">
                            <i class="fab fa-whatsapp text-green-400 text-xl"></i> Chat on WhatsApp
                        </a>
                    </div>
                    <div class="mt-6 text-slate-400 text-sm md:text-base font-medium animate-fade-in-up md:text-left text-center" style="animation-delay: 0.4s;">
                        Prefer calling? Speak with PayGain at 033 4501 3342<br>
                        <span class="text-slate-500 text-xs md:text-sm">Monday–Saturday, 10:00 AM – 7:00 PM</span>
                    </div>"""

# Replace the specific block if it exists (might have minor differences, so use regex)
hero_pattern = re.compile(r'<div class="flex flex-col sm:flex-row gap-4 justify-center md:justify-start reveal active"[^>]*>.*?</div>', re.DOTALL)
if hero_pattern.search(content):
    content = hero_pattern.sub(new_hero_buttons, content)

# 2. Fix the "Book Free Consultation" anywhere else in the document
content = content.replace("Book Free Consultation", "Check Eligibility")
content = content.replace("Book Consultation", "Check Eligibility")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("hero buttons fixed")
