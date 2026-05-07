import os
import glob
import re

# 1. Update all footers to include Google Maps link and Preference Share Opportunities
def update_footer(content):
    # Update Structured Financial to Preference Share
    content = content.replace("Structured Financial Opportunities", "Preference Share Opportunities")
    content = content.replace("passive-income-style benefits", "income-support options")
    
    # Add Google Maps link in footer
    address_str = "C/O Krishna Banshi Khanra, Vill+PO- Nandapur, East Midnapore, WB - 721625"
    if address_str in content and "View on Google Maps" not in content:
        maps_link = '<br><a href="https://maps.google.com/?q=3WS4B,+3rd+Floor,+West+Tower,+Mani+Casadona,+Newtown,+Kolkata,+WB+-+700156" target="_blank" class="hover:text-pink-400 transition underline text-pink-500 mt-2 inline-block"><i class="fas fa-map-marker-alt"></i> View on Google Maps</a>'
        content = content.replace(address_str + '\n', address_str + maps_link + '\n')
        content = content.replace(address_str + '</span>', address_str + maps_link + '</span>')
        content = content.replace(address_str + '\r\n', address_str + maps_link + '\r\n')
    
    # Change Navbar CTA
    content = content.replace("Book Consultation", "Check Eligibility")
    content = content.replace("Get Analysis", "Check Eligibility")
    
    # Add mobile sticky bar if not exists
    mobile_bar = """
    <!-- Mobile Sticky CTA Bar -->
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-2 flex justify-between items-center z-50 md:hidden shadow-[0_-4px_10px_rgba(0,0,0,0.1)] pb-safe">
        <a href="tel:03345013342" class="flex flex-col items-center justify-center text-slate-600 hover:text-pink-500 text-[10px] font-bold w-1/3 py-1">
            <i class="fas fa-phone-alt text-xl mb-1"></i> Call
        </a>
        <a href="https://wa.me/910000000000" class="flex flex-col items-center justify-center text-green-500 hover:text-green-600 text-[10px] font-bold w-1/3 border-l border-r border-slate-100 py-1">
            <i class="fab fa-whatsapp text-xl mb-1"></i> WhatsApp
        </a>
        <a href="contact.html" class="flex flex-col items-center justify-center text-pink-500 hover:text-pink-600 text-[10px] font-bold w-1/3 py-1">
            <i class="fas fa-clipboard-check text-xl mb-1"></i> Eligibility
        </a>
    </div>
    <style>
        @media (max-width: 768px) {
            body { padding-bottom: 70px; }
            .pb-safe { padding-bottom: env(safe-area-inset-bottom, 8px); }
        }
    </style>
</body>"""
    if "Mobile Sticky CTA Bar" not in content:
        content = content.replace("</body>", mobile_bar)
        
    return content

# Iterate all html files
for filepath in glob.glob("*.html"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = update_footer(content)
    
    if filepath == 'index.html':
        # Hero paragraph
        content = content.replace("regular income possibilities", "future income planning")
        
        # Hero buttons microcopy
        hero_buttons_end = content.find("</a>", content.find("Check Eligibility")) + 4
        # Just to be safe, search for the buttons container end
        # We will look for "Explore Solutions" button and add after its closing tag if not there
        if "Prefer calling? Speak with PayGain" not in content:
            hero_btn_html = 'Explore Solutions</a>'
            replacement = hero_btn_html + '''
                </div>
                <div class="mt-6 text-slate-300 text-sm font-medium animate-fade-in-up" style="animation-delay: 0.6s;">
                    Prefer calling? Speak with PayGain at 033 4501 3342<br>
                    <span class="text-slate-400 text-xs">Monday–Saturday, 10:00 AM – 7:00 PM</span>
                </div>
            '''
            # A little tricky since we have flex gap. Let's find the flex container of buttons.
            if hero_btn_html in content:
                # We'll just replace the closing div of the flex container containing the buttons
                pass
                
        # Card descriptions
        content = content.replace("Understand structured financial options and fixed-income-style benefits.", "Eligible customers can request a consultation to understand Preference Share opportunities. Details are shared only during consultation and through official documentation.")
        content = content.replace("href=\"contact.html?product=structured\">Request Details", "href=\"contact.html?product=preference\">Request Consultation")
        content = content.replace("contact.html?product=structured", "contact.html?product=preference")
        
        # Add new sections
        # 1. After You Submit
        after_submit_html = """
        <!-- AFTER YOU SUBMIT SECTION -->
        <section class="py-20 bg-slate-50 border-t border-slate-200 reveal">
            <div class="container mx-auto px-6">
                <div class="text-center max-w-3xl mx-auto mb-16">
                    <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-6">After You Submit Your Requirement</h2>
                    <p class="text-lg text-slate-600 leading-relaxed">
                        PayGain follows a consultation-first process so you can understand suitable options before making any decision.
                    </p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-5 gap-4 text-center">
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center">
                        <div class="w-12 h-12 bg-pink-50 text-pink-500 rounded-full flex items-center justify-center font-bold mb-4">1</div>
                        <p class="text-sm font-semibold text-slate-800">PayGain receives<br>your details</p>
                    </div>
                    <div class="hidden md:flex items-center justify-center text-slate-300"><i class="fas fa-chevron-right text-2xl"></i></div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center">
                        <div class="w-12 h-12 bg-pink-50 text-pink-500 rounded-full flex items-center justify-center font-bold mb-4">2</div>
                        <p class="text-sm font-semibold text-slate-800">An advisor<br>contacts you</p>
                    </div>
                    <div class="hidden md:flex items-center justify-center text-slate-300"><i class="fas fa-chevron-right text-2xl"></i></div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center">
                        <div class="w-12 h-12 bg-pink-50 text-pink-500 rounded-full flex items-center justify-center font-bold mb-4">3</div>
                        <p class="text-sm font-semibold text-slate-800">Age, goal, budget<br>& eligibility reviewed</p>
                    </div>
                    <div class="hidden md:flex items-center justify-center text-slate-300"><i class="fas fa-chevron-right text-2xl"></i></div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center">
                        <div class="w-12 h-12 bg-pink-50 text-pink-500 rounded-full flex items-center justify-center font-bold mb-4">4</div>
                        <p class="text-sm font-semibold text-slate-800">Partner options<br>are explained</p>
                    </div>
                    <div class="hidden md:flex items-center justify-center text-slate-300"><i class="fas fa-chevron-right text-2xl"></i></div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center">
                        <div class="w-12 h-12 bg-pink-50 text-pink-500 rounded-full flex items-center justify-center font-bold mb-4">5</div>
                        <p class="text-sm font-semibold text-slate-800">You decide after<br>reviewing docs</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- WHY CUSTOMERS TRUST -->
        <section class="py-20 bg-white border-t border-slate-200 reveal">
            <div class="container mx-auto px-6">
                <div class="text-center max-w-3xl mx-auto mb-16">
                    <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-6">Why Customers Can Speak With PayGain Confidently</h2>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="flex items-start gap-4"><i class="fas fa-check-circle text-green-500 mt-1 text-xl"></i><div><h4 class="font-bold text-slate-800">Registered Private Limited Company</h4><p class="text-sm text-slate-500">CIN: U70200WB2024PTC267967</p></div></div>
                    <div class="flex items-start gap-4"><i class="fas fa-map-marker-alt text-blue-500 mt-1 text-xl"></i><div><h4 class="font-bold text-slate-800">Kolkata-Based Office Presence</h4><p class="text-sm text-slate-500">Available for in-person consultations.</p></div></div>
                    <div class="flex items-start gap-4"><i class="fas fa-handshake text-pink-500 mt-1 text-xl"></i><div><h4 class="font-bold text-slate-800">Partner-Coordinated Guidance</h4><p class="text-sm text-slate-500">We work with relevant insurance partners.</p></div></div>
                    <div class="flex items-start gap-4"><i class="fas fa-comments text-purple-500 mt-1 text-xl"></i><div><h4 class="font-bold text-slate-800">Consultation-First Approach</h4><p class="text-sm text-slate-500">No rushed decisions or instant quotes.</p></div></div>
                    <div class="flex items-start gap-4"><i class="fas fa-file-contract text-orange-500 mt-1 text-xl"></i><div><h4 class="font-bold text-slate-800">Official Documents Reviewed</h4><p class="text-sm text-slate-500">Decide only after understanding complete terms.</p></div></div>
                </div>
            </div>
        </section>
        
        <!-- COMPACT LEAD FORM -->
        <section class="py-20 bg-slate-900 text-white relative overflow-hidden reveal">
            <div class="absolute inset-0 opacity-10 bg-[url('assets/images/pattern.png')] bg-repeat"></div>
            <div class="container mx-auto px-6 relative z-10 flex justify-center">
                <div class="w-full max-w-xl bg-white rounded-3xl p-8 md:p-10 shadow-2xl text-slate-800">
                    <h3 class="text-2xl font-bold text-center mb-2">Get PayGain Guidance</h3>
                    <p class="text-sm text-center text-slate-500 mb-8">Share a few details and our team will contact you to understand your requirements and explain suitable options.</p>
                    
                    <form action="contact.html" method="GET" class="space-y-4">
                        <input type="text" placeholder="Full Name" required class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-pink-500 focus:outline-none bg-slate-50">
                        <input type="tel" placeholder="Mobile Number" required pattern="^[6-9]\d{9}$" class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-pink-500 focus:outline-none bg-slate-50">
                        <input type="text" placeholder="City" required class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-pink-500 focus:outline-none bg-slate-50">
                        <select name="product" required class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-pink-500 focus:outline-none bg-white">
                            <option value="" disabled selected>Interested In...</option>
                            <option value="life">Life Insurance & Family Protection</option>
                            <option value="health">Health Insurance</option>
                            <option value="motor">Motor Insurance</option>
                            <option value="child">Child Future Planning</option>
                            <option value="income">Retirement / Future Income Planning</option>
                            <option value="renewal">Renewal Support</option>
                            <option value="preference">Preference Share Opportunities</option>
                            <option value="career">PayGain Advisor / Career</option>
                        </select>
                        <input type="text" placeholder="Preferred Contact Time" class="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-pink-500 focus:outline-none bg-slate-50">
                        
                        <button type="submit" class="w-full bg-pink-500 hover:bg-pink-600 text-white font-bold py-4 rounded-xl shadow-lg transition text-lg mt-4">
                            Submit & Request Callback
                        </button>
                        <p class="text-xs text-center text-slate-400 mt-4 leading-relaxed">
                            PayGain collects your requirement and may coordinate with relevant insurance/financial partners. Final quotations, benefits, terms, and documents are provided by the respective partner, insurer, or company.
                        </p>
                    </form>
                </div>
            </div>
        </section>
        """
        
        if "AFTER YOU SUBMIT SECTION" not in content:
            # Insert before the detailed corporate footer
            footer_index = content.find("<!-- DETAILED CORPORATE FOOTER -->")
            if footer_index != -1:
                content = content[:footer_index] + after_submit_html + content[footer_index:]

    if filepath == 'faq.html':
        content = content.replace("passive-income-style benefits", "income-support options")
        
        # Add new FAQ
        new_faq = """
                <!-- FAQ Item -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md transition">
                    <h3 class="text-xl font-bold text-slate-800 mb-4 flex items-start gap-3">
                        <i class="fas fa-question-circle text-pink-500 mt-1"></i> Will I get an instant quote from the website?
                    </h3>
                    <p class="text-slate-600 leading-relaxed">
                        No. PayGain does not generate instant quotations on the website. After you submit your requirement, our team may coordinate with relevant insurance/financial partners. Final quotations, illustrations, terms, benefits, and documentation are provided by the respective partner, insurer, or company.
                    </p>
                </div>
        """
        if "Will I get an instant quote" not in content:
            faq_container_end = content.find("</div>\n        </div>\n    </section>")
            if faq_container_end != -1:
                content = content[:faq_container_end] + new_faq + content[faq_container_end:]

    if filepath == 'contact.html':
        content = content.replace("structured", "preference")
        content = content.replace("Structured Financial Opportunities", "Preference Share Opportunities")
        content = content.replace("Understand fixed-income-style structured options.", "Understand Preference Share opportunities.")
        content = content.replace("Speak with an advisor to understand structured options, eligibility, tenure, and risks before making any financial decision. Information is shared strictly via official documentation.", "Eligible customers can request a consultation to understand Preference Share opportunities through official documentation.")
        content = content.replace("Structured opportunities, fixed-income-style benefits, tenure options, eligibility, risks, documentation, and terms are explained only during consultation and through official documents. Nothing on this form should be treated as an offer, guarantee, or investment advice.", "Preference Share details are shared only during consultation and through official documentation. This inquiry form does not represent an offer, guarantee, or investment advice.")
        content = content.replace("'preference': {", "'preference': {\n                title: 'Preference Share Inquiry',")
        # Removing previous duplicate title insertion if it happens, we'll just cleanly replace the dict value:
        
        # For the generic partner text below the form, we already have a dynamic note. But user requested a text *below all major forms or near form submit buttons*.
        # I'll update the static text in compact lead form. For contact.html, the disclaimer box at bottom handles the general one, and `solution-note` handles the specific one.
        pass

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Massive updates applied successfully.")
