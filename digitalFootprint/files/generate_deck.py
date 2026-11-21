import os
import shutil
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = "/home/test/presentation/Digital Footprints.pptx"
BACKUP_PATH = "/home/test/presentation/Digital Footprints.v1.backup.pptx"

if not os.path.exists(BACKUP_PATH) and os.path.exists(PPTX_PATH):
    shutil.copyfile(PPTX_PATH, BACKUP_PATH)

prs = pptx.Presentation(PPTX_PATH)

# Colors
C_INK = RGBColor(0x0F, 0x14, 0x19)       # #0F1419 - Primary Dark
C_INK2 = RGBColor(0x18, 0x20, 0x2A)      # #18202A - Secondary Dark
C_HOT = RGBColor(0xFF, 0x6B, 0x4A)       # #FF6B4A - Coral/Orange Accent
C_PAPER = RGBColor(0xED, 0xEF, 0xEA)     # #EDEFEA - White/Light Paper
C_BODY = RGBColor(0xC7, 0xCF, 0xD7)      # #C7CFD7 - Light Grey Body
C_MUTE = RGBColor(0x9A, 0xA7, 0xB4)      # #9AA7B4 - Muted Grey
C_FAINT = RGBColor(0x7C, 0x89, 0x96)     # #7C8996 - Faint Grey
C_CARD_BG = RGBColor(0x13, 0x1A, 0x22)   # Card Dark Background
C_CARD_BORDER = RGBColor(0x24, 0x30, 0x3E) # Card Border
C_CARD_LIGHT = RGBColor(0xFA, 0xFA, 0xF9)  # Light Card for Hot Slide

FONT_TITLE = "Space Grotesk"
FONT_BODY = "Inter"

# Drop all existing slides while keeping master, embedded fonts, and themes
while len(prs.slides) > 0:
    rId = prs.slides._sldIdLst[0].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[0]

blank_layout = prs.slide_layouts[0]

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, eyebrow_text, title_text, dark_mode=True):
    # Eyebrow
    tb_eye = slide.shapes.add_textbox(Inches(0.88), Inches(0.65), Inches(11.5), Inches(0.35))
    tf_eye = tb_eye.text_frame
    tf_eye.word_wrap = True
    tf_eye.margin_left = tf_eye.margin_top = tf_eye.margin_right = tf_eye.margin_bottom = 0
    p_eye = tf_eye.paragraphs[0]
    p_eye.text = eyebrow_text.upper()
    p_eye.font.name = FONT_BODY
    p_eye.font.size = Pt(12)
    p_eye.font.bold = True
    p_eye.font.color.rgb = C_HOT if dark_mode else C_INK

    # Title
    tb_title = slide.shapes.add_textbox(Inches(0.88), Inches(1.05), Inches(11.5), Inches(0.8))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = FONT_TITLE
    p_title.font.size = Pt(36)
    p_title.font.bold = True
    p_title.font.color.rgb = C_PAPER if dark_mode else C_INK

def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
    else:
        shape.line.fill.background()
    return shape

# ==========================================
# SLIDE 1: Cover
# ==========================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, C_INK)

tb1_eye = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(0.4))
p = tb1_eye.text_frame.paragraphs[0]
p.text = "DIGITAL FOOTPRINTS"
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HOT

tb1_title = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(2.2))
tf1_title = tb1_title.text_frame
tf1_title.word_wrap = True
p = tf1_title.paragraphs[0]
p.text = "Digital Footprints"
p.font.name = FONT_TITLE
p.font.size = Pt(64)
p.font.bold = True
p.font.color.rgb = C_PAPER

p2 = tf1_title.add_paragraph()
p2.text = "How much does the internet know about you?"
p2.font.name = FONT_BODY
p2.font.size = Pt(28)
p2.font.color.rgb = C_BODY
p2.space_before = Pt(16)

# Bottom author card
card_s1 = add_card(s1, Inches(1.0), Inches(5.2), Inches(11.33), Inches(1.2), bg_color=C_INK2)
tf_c1 = card_s1.text_frame
tf_c1.word_wrap = True
tf_c1.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_c1.paragraphs[0]
p.text = "Student 383  ·  Student 388"
p.font.name = FONT_TITLE
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.alignment = PP_ALIGN.CENTER

p_sub = tf_c1.add_paragraph()
p_sub.text = "5-Minute Presentation & Topic Defense"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = C_MUTE
p_sub.alignment = PP_ALIGN.CENTER
p_sub.space_before = Pt(4)

s1.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker A / 383 & 388 · 30s):\n\n"
    "Pause two seconds and let the title sit on screen.\n\n"
    "“Think about your everyday online routine: you check Instagram, search on Google, navigate with maps, "
    "and stream music. You've never paid a subscription fee for any of them. "
    "So who is paying, and what are they buying?\n\n"
    "I'm Student 383, and my co-presenter is Student 388. In the next five minutes, we'll demonstrate what a digital "
    "footprint actually is: not just one leaked password or forgotten photo, but a continuous pipeline that logs, "
    "profiles, and sells access to your predicted behavior.”"
)

# ==========================================
# SLIDE 2: The Hook
# ==========================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, C_INK)
add_header(s2, "The Hook", "You thought about it. Then you saw the ad.")

tb2_sub = s2.shapes.add_textbox(Inches(0.88), Inches(1.95), Inches(11.5), Inches(0.6))
p = tb2_sub.text_frame.paragraphs[0]
p.text = "Your phone isn't listening through your microphone. It’s doing something much smarter."
p.font.name = FONT_BODY
p.font.size = Pt(20)
p.font.color.rgb = C_BODY

# Two cards: Myth vs Reality
c2_a = add_card(s2, Inches(0.88), Inches(2.7), Inches(5.6), Inches(3.8), bg_color=C_CARD_BG)
tf = c2_a.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.35)
p = tf.paragraphs[0]
p.text = "THE POPULAR MYTH"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_HOT

p = tf.add_paragraph()
p.text = "Secret Microphones"
p.font.name = FONT_TITLE
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.space_before = Pt(8)

p = tf.add_paragraph()
p.text = "• Streaming live audio from billions of phones is technically detectable and bandwidth-heavy.\n\n" \
         "• Security researchers monitoring outbound network packets find zero evidence of secret audio transmissions.\n\n" \
         "• The belief persists because predictive targeting feels so uncannily accurate."
p.font.name = FONT_BODY
p.font.size = Pt(15)
p.font.color.rgb = C_BODY
p.space_before = Pt(14)

c2_b = add_card(s2, Inches(6.8), Inches(2.7), Inches(5.6), Inches(3.8), bg_color=C_INK2)
tf = c2_b.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.35)
p = tf.paragraphs[0]
p.text = "THE TECHNICAL REALITY"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_HOT

p = tf.add_paragraph()
p.text = "Predictive Modeling & Correlation"
p.font.name = FONT_TITLE
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.space_before = Pt(8)

p = tf.add_paragraph()
p.text = "• Co-location: When you talk to a friend, your phones share Wi-Fi or GPS. If they search it, you get shown the ad.\n\n" \
         "• Algorithmic Prediction: Based on age, habits, and scroll patterns, models anticipate what you want before you search.\n\n" \
         "• Bottom Line: They don't need to listen to you. They already know you."
p.font.name = FONT_BODY
p.font.size = Pt(15)
p.font.color.rgb = C_BODY
p.space_before = Pt(14)

s2.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker A · 45s):\n\n"
    "“Hands up if you've ever mentioned a product to a friend, or merely thought about it, and within an hour an ad for it popped up on your feed.\n\n"
    "Most people assume their phone's microphone is secretly listening. But cybersecurity packet analyses consistently show this isn't happening. Live audio streaming would drain battery, consume massive data bandwidth, and trigger privacy sensors.\n\n"
    "The truth is far more sobering: platforms don't need to listen to your voice. By correlating your location with the people around you, analyzing what your friends search for, and leveraging predictive models built from millions of users, algorithms predict what you want before you even search for it.”"
)

# ==========================================
# SLIDE 3: What is a digital footprint?
# ==========================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, C_INK2)
add_header(s3, "01 · The Foundation", "What is a digital footprint?")

# Active Panel
c3_a = add_card(s3, Inches(0.88), Inches(2.1), Inches(5.6), Inches(3.6), bg_color=C_CARD_BG)
tf = c3_a.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.35)
p = tf.paragraphs[0]
p.text = "ACTIVE FOOTPRINT"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_HOT

p = tf.add_paragraph()
p.text = "What You Consciously Share"
p.font.name = FONT_TITLE
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.space_before = Pt(6)

p = tf.add_paragraph()
p.text = "• Photos, videos, stories, and status updates\n" \
         "• Comments, forum posts, and public reviews\n" \
         "• Accounts and profiles you manually register\n" \
         "• Forms, survey responses, and customer support chats"
p.font.name = FONT_BODY
p.font.size = Pt(15)
p.font.color.rgb = C_BODY
p.space_before = Pt(12)

# Passive Panel
c3_b = add_card(s3, Inches(6.8), Inches(2.1), Inches(5.6), Inches(3.6), bg_color=C_CARD_BG)
tf = c3_b.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.35)
p = tf.paragraphs[0]
p.text = "PASSIVE FOOTPRINT"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_HOT

p = tf.add_paragraph()
p.text = "What Is Collected About You"
p.font.name = FONT_TITLE
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.space_before = Pt(6)

p = tf.add_paragraph()
p.text = "• Real-time GPS location and Wi-Fi bssid telemetry\n" \
         "• Search queries, click sequences, and link referrals\n" \
         "• Hardware specs, battery status, and OS build\n" \
         "• Browser canvas fingerprinting and ad tracking cookies"
p.font.name = FONT_BODY
p.font.size = Pt(15)
p.font.color.rgb = C_BODY
p.space_before = Pt(12)

# Bottom Punch banner
b_punch3 = add_card(s3, Inches(0.88), Inches(6.0), Inches(11.52), Inches(0.8), bg_color=C_INK)
tf = b_punch3.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.text = "It’s not a single trace. It’s a longitudinal record that grows for years."
p.font.name = FONT_TITLE
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_PAPER
p.alignment = PP_ALIGN.CENTER

s3.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker A · 45s):\n\n"
    "“Your footprint divides into two distinct categories.\n\n"
    "First is the active footprint: the photos you upload, status updates, reviews, and messages. This is what most people think of when they hear 'digital footprint'. You have agency over it.\n\n"
    "Second—and far larger—is the passive footprint. This is the telemetry gathered while you simply exist online: your IP address, device specs, browsing duration, and movement patterns. You never explicitly agree to it, and it happens entirely in the background.\n\n"
    "The key insight: a digital footprint isn't a snapshot in time. It is a continuous, longitudinal record that compounds over years.”"
)

# ==========================================
# SLIDE 4: What gets logged
# ==========================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, C_INK)
add_header(s4, "02 · Telemetry", "What gets logged about you")

tiles = [
    ("Location", "GPS coordinates, connected Wi-Fi networks, Bluetooth beacons, daily travel routes."),
    ("Searches", "Queries, medical worries, curiosities, and late-night private questions."),
    ("Purchases", "Credit card categories, items bought, brand loyalty, and items abandoned in cart."),
    ("Contacts", "Call frequencies, synced address books, interaction reciprocity, and proximity."),
    ("Device Info", "Battery health, screen resolution, browser extensions, audio hardware fingerprints."),
    ("Micro-Signals", "Scroll velocity, hover duration, deleted draft comments, and insomnia scroll hours.")
]

tw = Inches(3.65)
th = Inches(1.8)
xs = [Inches(0.88), Inches(4.8), Inches(8.75)]
ys = [Inches(2.1), Inches(4.1)]

for i, (tt, td) in enumerate(tiles):
    x = xs[i % 3]
    y = ys[i // 3]
    card = add_card(s4, x, y, tw, th, bg_color=C_CARD_BG)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
    p = tf.paragraphs[0]
    p.text = tt
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = C_HOT if i == 5 else C_PAPER
    
    p = tf.add_paragraph()
    p.text = td
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(6)

b_punch4 = add_card(s4, Inches(0.88), Inches(6.15), Inches(11.52), Inches(0.65), bg_color=C_INK2)
tf = b_punch4.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.text = "Micro-signals require zero voluntary sharing: lingering over a post without clicking still logs interest."
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.color.rgb = C_BODY
p.alignment = PP_ALIGN.CENTER

s4.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker A · 45s):\n\n"
    "“What kinds of data are actually stored?\n\n"
    "Location, searches, purchases, and device specs are standard. But look closely at tile 6: Micro-Signals.\n\n"
    "Modern social media apps and web platforms track telemetry down to the millisecond. If you pause over an image in your feed for three seconds without clicking 'Like', that dwell time is recorded as a micro-signal of interest. If you type a response and delete it, the hesitation is noted. If you scroll between 2 AM and 4 AM, the algorithm flags sleep disruption and possible emotional vulnerability.\n\n"
    "Each data point seems trivial on its own. Bound together, they reconstruct your daily life.”"
)

# ==========================================
# SLIDE 5: From logs to a profile (The Pipeline)
# ==========================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, C_INK2)
add_header(s5, "03 · The Mechanism", "From raw logs to a predictive profile")

steps = [
    ("1. COLLECT", "Cookies, scripts & app telemetry"),
    ("2. LINK", "Identity resolution across all devices"),
    ("3. PROFILE", "Data aggregation into user dossiers"),
    ("4. CONNECT", "Social graph & relationship mapping"),
    ("5. PREDICT", "Machine learning models anticipate actions"),
    ("6. ACT", "Targeted ads, price steering & feed ranking")
]

step_w = Inches(1.8)
step_gap = Inches(0.14)
start_x = Inches(0.88)

for i, (st, sd) in enumerate(steps):
    x = start_x + i * (step_w + step_gap)
    c = add_card(s5, x, Inches(2.2), step_w, Inches(2.8), bg_color=C_CARD_BG)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.18)
    p = tf.paragraphs[0]
    p.text = st
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    
    p = tf.add_paragraph()
    p.text = sd
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_PAPER
    p.space_before = Pt(12)

# Explanatory Callout Box
callout5 = add_card(s5, Inches(0.88), Inches(5.25), Inches(11.52), Inches(1.5), bg_color=C_INK)
tf = callout5.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "Key Concept: Identity Resolution"
p.font.name = FONT_TITLE
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_HOT

p = tf.add_paragraph()
p.text = "Data brokers and ad platforms do not treat your phone, laptop, home IP, and personal email as separate entities. Identity resolution algorithms merge these fragmented identifiers into a single persistent profile, associating every click across work, personal, and mobile devices."
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.color.rgb = C_BODY
p.space_before = Pt(6)

s5.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B / 388 takes over · 50s):\n\n"
    "“Thank you. Now, how does fragmented tracking data become a weapon of persuasion? It moves through a six-stage pipeline.\n\n"
    "Step 1: Raw data is collected via trackers, SDKs, and cookies.\n"
    "Step 2: Identity Resolution merges disparate identifiers—your work laptop, home Wi-Fi, personal phone, and email aliases become tied to one persistent individual.\n"
    "Step 3: Profiles are synthesized.\n"
    "Step 4: Social graphs map who you talk to and how frequently.\n"
    "Step 5: Machine learning models predict your likely decisions.\n"
    "Step 6: Platforms act—delivering hyper-targeted ads, adjusting insurance quotes, or re-ranking your newsfeed.\n\n"
    "The data isn't just stored; it is continually analyzed to predict what you will do next.”"
)

# ==========================================
# SLIDE 6: They guess what you never said
# ==========================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, C_INK)
add_header(s6, "04 · Inference", "They guess what you never said")

tb6_sub = s6.shapes.add_textbox(Inches(0.88), Inches(1.95), Inches(11.5), Inches(0.6))
p = tb6_sub.text_frame.paragraphs[0]
p.text = "Not sharing doesn't protect you. Inference consistently beats disclosure."
p.font.name = FONT_BODY
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = C_HOT

cards6 = [
    ("Homophily", "Peer-Group Inference", 
     "People closely resemble the company they keep. Even if you never post your political leaning, salary, or religious views, algorithms infer them with high statistical confidence based strictly on your friends' behavior."),
    ("Shadow Profiles", "Non-User Tracking", 
     "Even if you have never created an account on a platform, you likely have a shadow profile. When friends sync their address books or upload tagged group photos, the platform constructs an indexed profile for you."),
    ("Behavioral Inference", "Latent Trait Modeling", 
     "Models can detect early signs of depression, chronic illness, relationship strain, or job insecurity from subtle shifts in typing speed, active hours, and content consumption—without you typing a single word about it.")
]

cw6 = Inches(3.65)
for i, (ct, cs, cd) in enumerate(cards6):
    c = add_card(s6, xs[i], Inches(2.7), cw6, Inches(3.9), bg_color=C_CARD_BG)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = ct
    p.font.name = FONT_TITLE
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_PAPER
    
    p = tf.add_paragraph()
    p.text = cs
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    p.space_before = Pt(4)
    
    p = tf.add_paragraph()
    p.text = cd
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(12)

s6.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B · 50s):\n\n"
    "“The most common defense people offer is: 'I don't post anything sensitive, so I have nothing to worry about.'\n\n"
    "This ignores how machine learning works. In data analytics, inference beats disclosure.\n\n"
    "First, homophily: you share characteristics with your peer network. If five of your friends are interested in a specific medical treatment or investment, models infer that you are too.\n\n"
    "Second, shadow profiles: platforms map non-users through address book uploads and photo metadata. You don't need an account to be tracked.\n\n"
    "Third, behavioral inference: changes in when you log on or how quickly you scroll reveal health conditions, stress levels, and life transitions long before you disclose them.”"
)

# ==========================================
# SLIDE 7: The feed is built for them, not you
# ==========================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, C_INK2)
add_header(s7, "05 · The Business Model", "The feed is built for them, not you")

tb7_sub = s7.shapes.add_textbox(Inches(0.88), Inches(1.95), Inches(11.5), Inches(0.6))
p = tb7_sub.text_frame.paragraphs[0]
p.text = "The product is your attention and predicted behavior. Advertisers are the paying customers."
p.font.name = FONT_BODY
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = C_PAPER

cards7 = [
    ("Variable Rewards", "Dopamine Slot Machine",
     "Pull-to-refresh and algorithmic feeds deliver unpredictable rewards. You scroll because the next post *might* be interesting—the exact psychological trigger exploited in gambling machines."),
    ("Filter Bubbles & Outrage", "Engagement Over Truth",
     "Algorithms prioritize content that maximizes reaction time. Moral outrage and agreeable echo-chambers keep users engaged longer than balanced or nuanced reporting."),
    ("Vulnerability Targeting", "Monetizing Low Points",
     "Users scrolling late at night or during stressful periods spend significantly longer on screen. Documented studies reveal that vulnerable states generate peak advertising and scam profitability.")
]

for i, (ct, cs, cd) in enumerate(cards7):
    c = add_card(s7, xs[i], Inches(2.7), cw6, Inches(3.9), bg_color=C_CARD_BG)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = ct
    p.font.name = FONT_TITLE
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_PAPER
    
    p = tf.add_paragraph()
    p.text = cs
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    p.space_before = Pt(4)
    
    p = tf.add_paragraph()
    p.text = cd
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(12)

s7.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B · 45s):\n\n"
    "“Why is the digital environment constructed this way?\n\n"
    "Because social feeds are not designed to inform you—they are engineered to capture your attention and sell access to your future behavior.\n\n"
    "Variable rewards turn your feed into a casino slot machine. Filter bubbles feed confirmation bias and outrage because outrage generates comments and shares. And most dangerously, when users are lonely, exhausted, or anxious, their defense mechanisms drop and their scroll times soar—making them the most profitable targets for advertising and scams.\n\n"
    "You are not the customer; you are the inventory being calibrated.”"
)

# ==========================================
# SLIDE 8: When it leaks
# ==========================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, C_INK)
add_header(s8, "06 · Permanent Risk", "When it leaks")

tb8_sub = s8.shapes.add_textbox(Inches(0.88), Inches(1.95), Inches(11.5), Inches(0.6))
p = tb8_sub.text_frame.paragraphs[0]
p.text = "You can change a password. You can’t change your NID or your face."
p.font.name = FONT_TITLE
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = C_HOT

cards8 = [
    ("KYC & Age Verification", "Data Honeypots",
     "Every bank, crypto exchange, and app demanding national identity documents and verification selfies creates an attractive honeypot for cybercriminals."),
    ("Permanent Breaches", "No Reset Button",
     "Credentials can be revoked, but leaked national IDs, biometric selfies, and birth records are permanent. Major breaches (e.g. Equifax, national ID exposures) leak lifetime identifiers."),
    ("Identity + Telemetry", "Targeted Exploitation",
     "When leaked government IDs are synthesized with browsing telemetry, attackers launch devastating spear-phishing, SIM swaps, financial fraud, extortion, and doxxing attacks.")
]

for i, (ct, cs, cd) in enumerate(cards8):
    c = add_card(s8, xs[i], Inches(2.7), cw6, Inches(3.9), bg_color=C_CARD_BG)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = ct
    p.font.name = FONT_TITLE
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_PAPER
    
    p = tf.add_paragraph()
    p.text = cs
    p.font.name = FONT_BODY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    p.space_before = Pt(4)
    
    p = tf.add_paragraph()
    p.text = cd
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(12)

s8.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B · 45s):\n\n"
    "“The ultimate risk of digital footprints isn't just annoying ads—it is permanent vulnerability when data inevitably leaks.\n\n"
    "Today, countless services demand KYC: uploads of your passport, national ID card, and a facial biometric selfie. These corporate servers become giant data honeypots.\n\n"
    "Here is the fundamental difference: if someone steals your password, you can change it in 30 seconds. But you cannot rotate your national ID number, your date of birth, or your face. Once leaked in a breach—such as the massive Equifax breach or public government portal exposures—that data is out forever.\n\n"
    "When criminals marry leaked identity documents with your browsing habits, it enables flawless identity theft, SIM-swap attacks, and targeted extortion.”"
)

# ==========================================
# SLIDE 9: What you can do (6 Actionable Habits)
# ==========================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, C_INK2)
add_header(s9, "07 · Mitigation", "What you can do: 6 Actionable Habits")

habits = [
    ("1. Audit Yourself", "Search your full name, phone numbers, and handles across search engines to see your public attack surface."),
    ("2. Lock Down Settings", "Make social profiles private, disable ad personalization, and turn off background location permissions."),
    ("3. Limit App Access", "Enforce strict least privilege: does a calculator or flashlight app need your contacts or microphone? Deny it."),
    ("4. Separate Identities", "Use unique email aliases (e.g. SimpleLogin) and distinct usernames for banking, social media, and newsletters."),
    ("5. Share Less ID", "Practice data minimization: challenge unnecessary ID requests and avoid uploading verification documents."),
    ("6. Delete Old Accounts", "Unused forums and abandoned apps still leak credentials during breaches. Regularly purge dormant accounts.")
]

for i, (ht, hd) in enumerate(habits):
    x = xs[i % 3]
    y = ys[i // 3]
    c = add_card(s9, x, y, tw, th, bg_color=C_CARD_BG)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.22)
    p = tf.paragraphs[0]
    p.text = ht
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    
    p = tf.add_paragraph()
    p.text = hd
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(6)

b_punch9 = add_card(s9, Inches(0.88), Inches(6.15), Inches(11.52), Inches(0.65), bg_color=C_INK)
tf = b_punch9.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.text = "The mindset behind all six is OPSEC (Operational Security): think about what you expose before you post."
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.color.rgb = C_PAPER
p.alignment = PP_ALIGN.CENTER

s9.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B · 45s):\n\n"
    "“So what is our defense? We don't need to throw our phones in a river. We need OPSEC—operational security—and data minimization.\n\n"
    "Six concrete habits:\n"
    "1. Audit yourself: run searches on your own name to see what a stranger sees.\n"
    "2. Lock down privacy and ad-tracking toggles.\n"
    "3. Practice least-privilege app permissions.\n"
    "4. Compartmentalize: use separate email aliases for critical banking versus disposable sign-ups.\n"
    "5. Practice data minimization: resist handing over national IDs unless legally mandatory.\n"
    "6. Delete forgotten accounts before their database gets dumped online.\n\n"
    "OPSEC is not a tool; it's the habit of thinking before exposing.”"
)

# ==========================================
# SLIDE 10: Takeaway (Hot Slide)
# ==========================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, C_HOT)

tb10_eye = s10.shapes.add_textbox(Inches(0.88), Inches(0.65), Inches(11.5), Inches(0.35))
p = tb10_eye.text_frame.paragraphs[0]
p.text = "THE TAKEAWAY"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_INK

tb10_title = s10.shapes.add_textbox(Inches(0.88), Inches(1.05), Inches(11.5), Inches(1.1))
tf = tb10_title.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "You can’t erase your footprint. You can choose what it says about you."
p.font.name = FONT_TITLE
p.font.size = Pt(38)
p.font.bold = True
p.font.color.rgb = C_INK

takes = [
    ("KNOW", "Understand what telemetry and micro-signals are gathered silently in the background."),
    ("LIMIT", "Compartmentalize identities, minimize data handover, and strictly restrict permissions."),
    ("QUESTION", "Recognize that 'free' services monetize your attention, time, and predicted behavior.")
]

for i, (tt, td) in enumerate(takes):
    c = add_card(s10, xs[i], Inches(2.4), cw6, Inches(3.0), bg_color=C_CARD_LIGHT, border_color=None)
    tf = c.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = tt
    p.font.name = FONT_TITLE
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_HOT
    
    p = tf.add_paragraph()
    p.text = td
    p.font.name = FONT_BODY
    p.font.size = Pt(15)
    p.font.color.rgb = C_INK
    p.space_before = Pt(12)

tb10_close = s10.shapes.add_textbox(Inches(0.88), Inches(5.75), Inches(11.5), Inches(0.8))
tf = tb10_close.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "“The question isn’t whether we’re tracked. It’s who controls what’s built from it.”"
p.font.name = FONT_TITLE
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = C_INK
p.alignment = PP_ALIGN.CENTER

s10.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Speaker B · 30s):\n\n"
    "“You cannot completely erase your digital footprint in the 21st century. But you can actively control what it says about you.\n\n"
    "Know what is collected.\n"
    "Limit what you share and allow.\n"
    "And question anything that claims to be 'free'.\n\n"
    "Because ultimately, the defining question of our generation isn't whether we're tracked—it's who controls what is built from it.”"
)

# ==========================================
# SLIDE 11: Thank You & Q&A
# ==========================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, C_INK)

tb11_eye = s11.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(0.4))
p = tb11_eye.text_frame.paragraphs[0]
p.text = "DIGITAL FOOTPRINTS"
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HOT

tb11_title = s11.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.5))
p = tb11_title.text_frame.paragraphs[0]
p.text = "Thank You"
p.font.name = FONT_TITLE
p.font.size = Pt(64)
p.font.bold = True
p.font.color.rgb = C_PAPER

# Presenters box
c11 = add_card(s11, Inches(1.0), Inches(3.6), Inches(11.33), Inches(2.6), bg_color=C_CARD_BG)
tf = c11.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.4)
p = tf.paragraphs[0]
p.text = "Questions & Discussion"
p.font.name = FONT_TITLE
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = C_HOT
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "Presented by Student 383 & Student 388"
p.font.name = FONT_BODY
p.font.size = Pt(20)
p.font.color.rgb = C_PAPER
p.alignment = PP_ALIGN.CENTER
p.space_before = Pt(14)

p = tf.add_paragraph()
p.text = "Topics: Identity Resolution · Data Minimization · Latent Inference · Behavioral Telemetry · OPSEC"
p.font.name = FONT_BODY
p.font.size = Pt(14)
p.font.color.rgb = C_MUTE
p.alignment = PP_ALIGN.CENTER
p.space_before = Pt(12)

s11.notes_slide.notes_text_frame.text = (
    "SPEAKER NOTES (Joint · 20s):\n\n"
    "“Thank you for your attention. We would now be glad to take questions from the class and the instructor.\n\n"
    "(Prepared Q&A defense points: information asymmetry, difference between selling raw data vs. selling access to predicted behavior, and zero-knowledge proofs as a solution to KYC honeypots.)”"
)

# Save both Digital Footprints.pptx and 383 & 388.pptx
prs.save(PPTX_PATH)
copy_target = "/home/test/presentation/383 & 388.pptx"
shutil.copyfile(PPTX_PATH, copy_target)
print("Successfully generated 11-slide presentation to:")
print(" -", PPTX_PATH)
print(" -", copy_target)
