import re
import glob
import os

descriptions = {
    # SKIN TREATMENTS
    "Acne Treatments": "At Medshine, we target the root causes of acne with advanced clinical therapies. Our tailored Medshine protocols reduce active inflammation, clear clogged pores, and prevent future breakouts for a radiant complexion.",
    "Scar Treatments": "Smooth and restore your skin texture with Medshine’s advanced scar treatments. Using state-of-the-art technology, our Medshine specialists carefully diminish acne scars and trauma marks, revealing flawless skin.",
    "Anti Ageing Treatments": "Turn back time with exclusive Medshine anti-ageing solutions. We customize every Medshine treatment to combat fine lines, wrinkles, and volume loss, giving you a naturally youthful and refreshed appearance.",
    "Pigmentation Treatment": "Erase stubborn dark spots and melasma with Medshine’s targeted pigmentation therapies. The Medshine clinical approach breaks down excess melanin safely, leaving your skin even-toned and luminous.",
    "Medicated Facials": "Revitalize your complexion with Medshine’s specialized medicated facials. Infused with potent active ingredients, each Medshine facial is tailored to deeply cleanse, hydrate, and heal your unique skin type.",
    "Hydra Facials": "Experience the ultimate glow with a Medshine Hydra Facial. This multi-step Medshine procedure deeply cleanses, exfoliates, and extracts impurities while bathing the new skin in hydrating serums.",
    "Skin Tags, Warts": "Safely and painlessly remove unwanted growths with Medshine’s precision treatments for skin tags and warts. Our Medshine experts ensure minimal scarring and quick recovery for smooth, clear skin.",
    "Corn Removal": "Relieve foot discomfort instantly with professional corn removal at Medshine. Using sterile, clinical techniques, the Medshine team safely removes painful corns, restoring your mobility and comfort.",
    "Botox": "Soften dynamic wrinkles and frown lines with precision Botox injections at Medshine. Our highly trained Medshine practitioners deliver natural-looking results that preserve your unique facial expressions.",
    "Skin Booster": "Infuse your skin with deep, lasting hydration using Medshine Skin Boosters. These micro-injections at Medshine improve skin elasticity and radiance from within, giving you a dewy, youthful glow.",
    "Derma Filler": "Restore lost facial volume and contour your features beautifully with Medshine derma fillers. Our Medshine specialists use premium hyaluronic acid fillers to sculpt lips, cheeks, and jawlines naturally.",
    "Thread Lift": "Achieve a non-surgical face lift with Medshine’s innovative thread lift procedures. The Medshine technique carefully lifts sagging skin and stimulates collagen production for a firmer, younger profile.",
    "MNRF": "Rejuvenate your skin from the inside out with Medshine’s Micro-Needling Radio Frequency (MNRF) therapy. Medshine MNRF effectively targets deep wrinkles, scars, and loose skin by remodeling collagen at the dermis level.",
    "Skin Whitening": "Brighten your overall complexion safely with Medshine’s customized skin whitening and brightening protocols. The Medshine approach uses medically approved ingredients to give you a luminous, glowing skin tone.",
    "Face PRP": "Harness your body's own healing power with a Medshine Face PRP (Vampire Facial) treatment. Medshine uses platelet-rich plasma to stimulate cellular turnover, boosting collagen and completely revitalizing your skin.",
    "Microneedling": "Stimulate fresh collagen and elastin with Medshine’s clinical microneedling therapy. By creating controlled micro-injuries, the Medshine protocol dramatically improves skin texture, pore size, and fine lines.",
    "Body Polishing": "Exfoliate and nourish your skin from head to toe with a luxurious Medshine body polishing session. The Medshine technique removes dead skin cells, leaving your body feeling incredibly smooth and deeply hydrated.",
    "Skin analysis": "Understand your skin at a microscopic level with a comprehensive Medshine skin analysis. Using advanced diagnostic tools, Medshine experts identify underlying issues to create your perfect, personalized skincare regimen.",
    "Open pore treatment": "Refine your skin texture and minimize enlarged pores with Medshine’s specialized open pore treatments. The Medshine protocols tighten the skin structure and control sebum, giving you a flawless, airbrushed finish.",
    "Red velvet facial": "Indulge in the signature Medshine Red Velvet Facial for an instant red-carpet glow. This exclusive Medshine treatment combines gentle exfoliation with luxurious antioxidants to deeply nourish and illuminate your face.",
    "Skin pH examination": "Optimize your skin’s natural barrier with a clinical Medshine skin pH examination. By accurately measuring your acid-alkaline balance, Medshine tailors medical skincare to protect and heal your unique complexion.",
    "Water Infusion Treatments": "Quench thirsty skin with Medshine’s advanced water infusion treatments. This Medshine therapy drives intense hydration deep into the dermal layers, plumping the skin and banishing dryness and dullness instantly.",

    # MEDICAL TREATMENTS
    "Diabetes Mellitus": "Manage your blood sugar effectively with comprehensive Medshine diabetes care. The Medshine medical team focuses on lifestyle integration and precision medicine to prevent complications and keep you thriving.",
    "Cardiology Diseases": "Protect your heart health with expert preventative care and management at Medshine. From hypertension to cholesterol management, Medshine provides thorough cardiovascular evaluations and personalized medical therapies.",
    "Dyslipidemia": "Balance your cholesterol levels and protect your vascular health with Medshine’s dyslipidemia management. Medshine doctors create tailored dietary and medical protocols to effectively reduce your risk of heart disease.",
    "Respiratory Illness": "Breathe easier with specialized care for respiratory illnesses at Medshine. Whether managing asthma or chronic bronchitis, the Medshine team provides acute relief and long-term pulmonary management.",
    "Infectious Disease": "Get accurate diagnosis and rapid treatment for infectious diseases at Medshine. Our Medshine medical experts utilize advanced diagnostics to ensure you receive the right antibiotics or antivirals for a swift recovery.",
    "Rheumatology Problems": "Relieve joint pain and manage autoimmune conditions effectively with Medshine rheumatology care. Medshine offers targeted therapies to reduce inflammation, preserve joint function, and improve your daily quality of life.",
    "Metabolic Illness": "Restore your body's internal balance with Medshine’s holistic approach to metabolic illnesses. Medshine experts address the root causes of metabolic syndrome, guiding you towards sustainable weight and health management.",
    "Endocrine Abnormalities": "Regulate your hormones and regain your vitality with Medshine’s endocrine care. Whether it's thyroid dysfunction or PCOS, Medshine provides precise testing and tailored medical treatments to stabilize your system.",
    "Kidney Problems": "Safeguard your renal function with proactive kidney care at Medshine. The Medshine medical team offers comprehensive screening and management for early-stage kidney problems, focusing on long-term preservation.",
    "Gastrointestinal Problems": "Heal your gut and resolve digestive issues with expert Medshine gastrointestinal care. From acid reflux to IBS, Medshine provides accurate diagnostics and dietary protocols to restore your digestive harmony.",
    "Neurological Illness": "Receive compassionate and expert care for neurological conditions at Medshine. Medshine provides comprehensive evaluations and management plans for migraines, neuropathy, and other nervous system disorders.",

    # HAIR TREATMENTS
    "High Frequency Laser Helmet": "Experience the future of hair restoration with the Medshine High Frequency Laser Helmet. This non-invasive Medshine treatment stimulates hair follicles and increases blood flow to encourage thicker, healthier hair growth.",
    "Platelet Rich Plasma Therapy": "Naturally combat hair loss with Medshine's advanced Platelet Rich Plasma (PRP) Therapy. Medshine utilizes your own growth factors to awaken dormant follicles and significantly increase hair density and strength.",
    "Anti Dandruff Treatments": "Eliminate stubborn flakes and soothe an itchy scalp with Medshine’s clinical anti-dandruff treatments. The Medshine protocol restores scalp health, balancing sebum production and deeply cleansing the roots.",
    "MesoTherapy": "Nourish your hair follicles directly with Medshine’s targeted hair mesotherapy. By micro-injecting vitamins and minerals into the scalp, Medshine halts hair fall and promotes the growth of strong, vibrant hair.",
    "QR678": "Halt severe hair loss with the revolutionary QR678 treatment, available at Medshine. This advanced Medshine therapy delivers specific growth factors directly to the scalp, clinically proven to regrow lost hair.",
    "Derma Rollers": "Stimulate your scalp’s natural healing response with Medshine’s clinical derma roller treatments. The Medshine technique creates micro-channels to boost blood circulation and maximize the absorption of hair growth serums.",
    "Scalp Treatment": "Restore the foundation of healthy hair with a deep-cleansing Medshine scalp treatment. Medshine specialists detoxify the scalp, removing buildup and unclogging follicles to create the perfect environment for hair growth.",
    "Hair meso": "Revitalize thinning hair with Medshine’s specialized Hair Meso treatments. This Medshine therapy infuses the scalp with a customized cocktail of nutrients, blocking DHT and encouraging robust, healthy hair strands.",
    "Hair analysis": "Discover the root cause of your hair concerns with a microscopic Medshine hair analysis. Using advanced trichology tools, Medshine identifies structural damage and scalp issues to formulate your perfect treatment plan.",

    # LASER TREATMENTS
    "Carbon Facial": "Achieve a flawless, porcelain complexion instantly with the Medshine Carbon Facial (Hollywood Peel). Medshine uses advanced laser technology and liquid carbon to deeply exfoliate, shrink pores, and brighten your skin.",
    "Laser Hair Removal": "Say goodbye to shaving forever with Medshine’s painless laser hair removal. Utilizing the latest diode technology, Medshine permanently reduces unwanted hair on all skin types safely and effectively.",
    "Omega Light Therapy": "Accelerate skin healing and fight acne bacteria with Medshine Omega Light Therapy. This soothing LED Medshine treatment uses specific light wavelengths to calm inflammation and boost cellular regeneration.",
    "Pigmentation, Laser toning & Open pores": "Tackle multiple skin concerns at once with Medshine’s comprehensive laser toning protocols. Medshine safely breaks down pigmentation while shrinking open pores, giving you a smooth, even-toned complexion.",
    "Skin Rejuvenation": "Turn back the clock with Medshine’s advanced laser skin rejuvenation. The Medshine lasers gently heat the dermis, stimulating collagen production to erase fine lines, sun damage, and uneven texture.",
    "Skin tightening": "Firm and lift sagging skin non-surgically with Medshine’s powerful laser skin tightening. Medshine uses deep dermal heating to contract existing collagen and spur new growth, resulting in a tighter, more youthful contour.",
    "Tattoo Removal": "Safely erase unwanted ink with Medshine’s advanced Q-switched laser tattoo removal. The Medshine technique breaks down tattoo pigments effectively with minimal discomfort, gradually clearing the skin without scarring.",

    # INJECTABLES
    "Scar Subscision Treatment": "Release deep, tethered acne scars with Medshine’s expert subcision treatments. By carefully breaking the fibrous bands beneath the skin, Medshine allows depressed scars to elevate, creating a smoother skin surface.",

    # NON-SURGICAL
    "HIFU": "Achieve a non-surgical facelift with Medshine’s High-Intensity Focused Ultrasound (HIFU) therapy. Medshine HIFU targets deep structural layers of the skin, dramatically lifting the brow, jawline, and neck.",

    # BRIDAL
    "Customised treatment": "Prepare for your big day with a completely bespoke Medshine bridal treatment plan. The Medshine team customizes a timeline of facials, lasers, and polishing to ensure you have a flawless, radiant bridal glow.",
    "Skin Polishing": "Get picture-perfect, glowing skin with Medshine’s pre-bridal skin polishing. This intensive Medshine exfoliation treatment sweeps away dullness and rough texture, leaving your face and body luminous for your wedding day.",
}

category_files = [
    "treatment-skin.html", "treatment-medical.html", "treatment-hair.html", 
    "treatment-laser.html", "treatment-injectables.html", "treatment-non-surgical.html", 
    "treatment-bridal.html", "treatments.html"
]

all_html = glob.glob("treatment-*.html")
detail_pages = [f for f in all_html if f not in category_files]

def replace_description_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract the title from the h1 tag
    title_match = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', content, re.IGNORECASE | re.DOTALL)
    if not title_match:
        print(f"Could not find title in {filepath}")
        return

    title = title_match.group(1).strip()
    
    # Clean up the title a bit (sometimes there are weird spaces or capitalization)
    # The dictionary keys must match exactly. Let's do a case-insensitive lookup
    desc = None
    for key, val in descriptions.items():
        if key.lower() == title.lower():
            desc = val
            break
            
    if not desc:
        print(f"WARNING: No specific description found for title '{title}' in {filepath}. Using fallback.")
        desc = f"Experience the transformative care of Medshine Clinic with our specialized {title} treatments. Medshine experts utilize the latest clinical advancements and customized protocols to ensure safe, effective, and outstanding results for your unique needs."

    # Now, find the <p class="text-[17px] md:text-[19px] text-inkmute leading-relaxed font-light reveal-anim">
    # and <p class="text-[17px] md:text-[19px] text-cream/70 leading-relaxed font-light reveal-anim">
    # and replace their inner text.
    
    # Regex to match the p tag and replace its contents.
    # The paragraph comes right after the image div, but let's just replace all paragraphs that match these classes.
    
    p_inkmute_pattern = r'(<p class="text-\[17px\] md:text-\[19px\] text-inkmute leading-relaxed font-light reveal-anim">).*?(</p>)'
    content = re.sub(p_inkmute_pattern, rf'\1\n            {desc}\n          \2', content, flags=re.DOTALL)
    
    p_cream_pattern = r'(<p class="text-\[17px\] md:text-\[19px\] text-cream/70 leading-relaxed font-light reveal-anim">).*?(</p>)'
    content = re.sub(p_cream_pattern, rf'\1\n            {desc}\n          \2', content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Updated {filepath} with Medshine description for '{title}'.")

for page in detail_pages:
    replace_description_in_file(page)

print("Done updating all treatment descriptions!")
