import re
with open('pulse.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<footer.*?</footer>', re.DOTALL | re.IGNORECASE)

footer_content = """<footer class="bg-slate-900 text-white pt-20 pb-12 border-t border-slate-800 reveal">
            <div class="container mx-auto px-6">
                <!-- Top Links Section -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16 border-b border-slate-800 pb-16">
                    <div class="lg:col-span-1">
                        <img src="assets/images/pg_logo_no_background.png" alt="PayGain Logo" class="h-16 w-auto object-contain mb-6">
                        <p class="text-slate-400 text-sm leading-relaxed mb-8">
                            Helping Indian families plan for protection, regular income, renewal support, and long-term financial security through structured financial and insurance-based solutions.
                        </p>
                    </div>
                    
                    <div>
                        <h4 class="text-lg font-bold mb-6 text-white tracking-wide">Quick Links</h4>
                        <ul class="space-y-3 text-slate-400 text-sm">
                            <li><a href="index.html" class="hover:text-pink-400 transition">Home</a></li>
                            <li><a href="about_us.html" class="hover:text-pink-400 transition">About Us</a></li>
                            <li><a href="career.html" class="hover:text-pink-400 transition">Careers / PayGain Advisor</a></li>
                            <li><a href="faq.html" class="hover:text-pink-400 transition">FAQs</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-lg font-bold mb-6 text-white tracking-wide">Our Solutions</h4>
                        <ul class="space-y-3 text-slate-400 text-sm">
                            <li><a href="index.html#contact" class="hover:text-pink-400 transition">Life Insurance & Family Protection</a></li>
                            <li><a href="index.html#contact" class="hover:text-pink-400 transition">Regular Income Planning</a></li>
                            <li><a href="index.html#contact" class="hover:text-pink-400 transition">Child Future Planning</a></li>
                            <li><a href="index.html#contact" class="hover:text-pink-400 transition">Health Insurance Planning</a></li>
                            <li><a href="index.html#contact" class="hover:text-pink-400 transition">Motor Insurance Strategy</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-lg font-bold mb-6 text-white tracking-wide">Contact PayGain</h4>
                        <ul class="space-y-4 text-slate-400 text-sm">
                            <li class="flex items-start gap-3">
                                <i class="fas fa-clock text-pink-500 mt-1 shrink-0 text-base"></i>
                                <span class="leading-relaxed"><strong>Business Hours:</strong><br>Monday–Saturday, 10:00 AM – 7:00 PM</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <i class="fas fa-map-marker-alt text-pink-500 mt-1 shrink-0 text-base"></i>
                                <span class="leading-relaxed">
                                    <a href="#" class="hover:text-pink-400 transition">3WS4B, 3rd Floor, West Tower, Mani Casadona, Newtown, Kolkata, WB - 700156</a><br><br>
                                    <strong>Registered Office:</strong> C/O Krishna Banshi Khanra, Vill+PO- Nandapur, East Midnapore, WB - 721625
                                </span>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-phone-alt text-pink-500 shrink-0 text-base"></i>
                                <span>033 4501 3342</span>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fab fa-whatsapp text-pink-500 shrink-0 text-base"></i>
                                <a href="https://wa.me/910000000000" class="hover:text-pink-400 transition">+91 XXXXX XXXXX</a>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="fas fa-envelope text-pink-500 shrink-0 text-base"></i>
                                <a href="mailto:info.paygain@gmail.com" class="hover:text-pink-400 transition">info.paygain@gmail.com</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="mt-12 p-6 bg-slate-900/50 rounded-xl text-xs text-slate-400 leading-relaxed text-justify mb-8 border border-slate-800">
                    <strong>Disclaimer:</strong> The information provided on this website is for general awareness and educational purposes only. Detailed plan structures, premium illustrations, Renewal Support details, returns, policy benefits, preference share terms, eligibility conditions, and documentation are shared only during consultation and through official documents. Product features, benefits, returns, tax treatment, policy conditions, dividend payouts, and outcomes may vary based on selected plans, insurer/company terms, customer eligibility, applicable laws, and official documentation. Customers should read all policy documents, benefit illustrations, offer documents, terms, conditions, exclusions, and risk factors carefully before making any financial or insurance decision.
                </div>

                <!-- Comprehensive Corporate Information (MCA Standards) -->
                <div class="mb-12">
                     <h4 class="text-lg font-bold mb-6 text-slate-300">Corporate Information</h4>
                     <p class="text-slate-500 text-xs leading-relaxed text-justify mb-8">
                         <strong>PAYGAIN MULTI SERVICES PRIVATE LIMITED</strong> is a Private Limited Company, governed by the Companies Act as a company limited by shares. Classified as a Non-government company, it is registered under the Registrar of Companies <strong>RoC-Kolkata</strong>. According to the Ministry of Corporate Affairs (MCA), this company was incorporated on <strong>31-01-2024</strong>. Its Corporate Identification Number (CIN) is <strong>U70200WB2024PTC267967</strong>, and it carries the registration number <strong>267967</strong>. Currently, its eFiling status is listed as "<strong>Active</strong>".
                     </p>
                </div>

                <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row items-center justify-between text-slate-500 text-xs gap-4">
                    <p>&copy; 2024 PayGain Multi Services Private Limited. All rights reserved.</p>
                    <div class="flex flex-wrap items-center gap-4 justify-center md:justify-start">
                        <a href="privacy.html" class="hover:text-slate-300 transition">Privacy Policy</a>
                        <span class="hidden sm:inline">|</span>
                        <a href="terms.html" class="hover:text-slate-300 transition">Terms of Service</a>
                        <span class="hidden sm:inline">|</span>
                        <a href="faq.html" class="hover:text-slate-300 transition">Disclaimers</a>
                    </div>
                </div>
            </div>
        </footer>"""

new_content = pattern.sub(footer_content, content)
with open('pulse.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Updated pulse.html')
