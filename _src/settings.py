# Site-wide settings. Copy for each language lives in _src/lang/<code>.py.
LINKEDIN = "https://www.linkedin.com/company/qiaopartners/"
EMAIL = "contact@qiaopartners.eu"
CALENDLY_URL = "https://calendly.com/wdong-qiaopartners/30min"   # empty string hides the calendar
WHATSAPP = "https://wa.me/qr/V5JZQYHRWE3IJ1"                      # QR image: img/whatsapp-qr.png
FORM_ENDPOINT = "https://formsubmit.co/ajax/contact@qiaopartners.eu"   # enquiry form submissions are emailed here
GOOGLE_SITE_VERIFICATION = ""   # code from Google Search Console (HTML tag method)
BING_SITE_VERIFICATION = ""     # code from Bing Webmaster Tools (meta tag method)
SITE = "https://qiaopartners.eu"

# Confirmed memberships only. Logo at img/members/<slug>.png (+ <slug>-dark.png for dark backgrounds).
MEMBERS = [
    {"slug": "sinocham", "name": "SinoCham",
     "full": {"en": "Polish-Chinese General Chamber of Commerce", "pl": "Polsko-Chińska Główna Izba Gospodarcza",
              "zh": "波兰中国总商会", "ru": "Польско-Китайская генеральная торговая палата"}},
]
