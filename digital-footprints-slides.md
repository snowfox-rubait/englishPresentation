# Digital Footprints: How Much Does Internet Know about You?

Slide content v2. Each slide has **On the slide** (what the audience reads) and **Triggers** (things the slide hints at that you expand on yourself). Triggers are not meant to be on screen in full.

Design rule: big text, few words. If a slide needs more than ~25 words, move it into Triggers.

---

## Slide 1: Cover

**On the slide**
- Title: **Digital Footprints**
- Subtitle: How much does the internet know about you?
- Names, course, university

---

## Slide 2: Hook

**On the slide**
- Big text: **You thought about it. Then you saw the ad.**
- Small text: Your phone isn't listening. It's doing something smarter.

**Triggers**
- Open with a question to the class: "Hands up if you've ever seen an ad for something you only *thought* about."
- Likely causes, not a secret microphone: friends' searches linked to you, same Wi-Fi or location, and prediction (the model guessed before you did).
- The point: the system does not need to listen. It already knows enough to predict you.

Alternate hook if you prefer something darker: **"Nobody asked me how I felt. The internet knew anyway."**

---

## Slide 3: What is a digital footprint?

**On the slide**
- **Active:** what you share (posts, comments, photos, accounts)
- **Passive:** what is collected about you (location, searches, device, cookies)
- Punch line: **It's not a single trace. It's a record that grows for years.**

**Triggers**
- Most of the footprint is passive: you never chose it.
- Longitudinal: the longer it runs, the more predictive it gets.

---

## Slide 4: What gets logged

**On the slide** (icon tiles)
- Location
- Searches
- Purchases
- Contacts
- Devices
- **Micro-signals:** scroll speed, pause time, deleted drafts, late-night use

**Triggers**
- Micro-signals need no sharing at all: lingering on a post without liking it still counts.
- Late-night usage hints at sleep and mood.
- Each piece looks harmless. Together they describe your life.
- Optional stat from v1: about 1,000 data points per person (verify the source first).

---

## Slide 5: From logs to a profile

**On the slide** (flow arrows)
- **Collect** → **Link** → **Profile** → **Connect** → **Predict** → **Act**

**Triggers**
- Link = identity resolution: phone, laptop, email and loyalty card become one person.
- Connect = who you talk to, how often, how closely.
- Act = ads, prices, credit scoring, what your feed shows.
- Trackers behind the first step: cookies, app permissions, fingerprinting (one technique among many, not the whole story).

---

## Slide 6: They guess what you never said

**On the slide**
- Big text: **Not sharing doesn't protect you.**
- Three chips: **Your friends' data** · **Your network** · **Your behavior**

**Triggers**
- Homophily: people resemble who they're connected to, so a teen's interests can be guessed from other teens or close friends.
- Shadow profiles: someone who never joined a platform can still be profiled through others' contacts and tagged photos.
- Inference beats disclosure: models can estimate sensitive traits from behavior alone (politics, health, mood).
- The data you didn't give is often the most sensitive output.

---

## Slide 7: The feed is built for them, not you

**On the slide**
- Big text: **The product is your attention.**
- Three chips: **Infinite scroll** · **Outrage and agreeing content** · **Vulnerable users**

**Triggers**
- Advertisers are the customers. Platforms sell access to your predicted behavior (brokers sell the data itself).
- Variable reward: pull to refresh works like a slot machine.
- Filter bubble and confirmation bias: you see more of what you already believe, fewer counterexamples, and the system never needs to "intend" it.
- Vulnerability targeting: when someone is lonely, stressed or low, they scroll longer, which makes them the most profitable (and most exposed to scams and harmful content). Keep this abstract in class.
- Consent is basically fictional: terms of service disclose it, but nobody can negotiate.
- Fairness note to add: the same machinery also does spam filtering, fraud detection and recommendations people like. The issue is consent and control.

---

## Slide 8: When it leaks

**On the slide**
- Big text: **You can change a password. You can't change your NID or your face.**
- Chips: **KYC and age checks** · **Data breaches** · **Linked datasets**
- Bottom line: **Identity + behavior = a target with a name.**

**Triggers**
- Every verifier (bank, telco, exchange, "age check" vendor) keeps a copy of your ID and selfie. More copies mean more breach surface: data honeypots.
- Breaches are permanent. Examples to cite: Equifax 2017, verification-photo leaks, reported Bangladeshi NID exposures (look up the exact sources before you say these).
- Joined with telemetry: identity fraud, SIM swap, targeted phishing, sextortion, blackmail, doxxing, harassment.
- OSINT: a username, an old post and a tagged photo can be pieced together into a detailed picture of you.
- Fair point: KYC and age checks have real goals. The flaw is over-collection and over-retention. Better designs exist (on-device checks, "over 18: yes" proofs, deleting documents after verification).

---

## Slide 9: What you can do

**On the slide**
1. **Audit yourself:** search your own name and usernames
2. **Lock down:** private profiles, ad personalization off
3. **Limit permissions:** does a flashlight app need your contacts?
4. **Separate identities:** different emails and usernames for finance, social and everyday use
5. **Share less ID:** hand over documents only when you must
6. **Delete old accounts**

Bottom line: **Think before you expose.**

**Triggers**
- Name it: OPSEC (operational security), a habit more than a tool.
- Data minimization: companies should collect only what they need, and so should you.
- Unique email aliases per service, and never reuse recovery answers.

---

## Slide 10: Takeaway

**On the slide**
- Big text: **You can't erase your footprint. You can choose what it says about you.**
- **Know** what is collected · **Limit** what you share and allow · **Question** anything "free"
- Closing line: **The question isn't whether we're tracked. It's who controls what's built from it.**

---

## Slide 11: Thank you

**On the slide**
- **Thank you**
- Names
- "Questions?"

---

## What changed from v1

- **New hook:** the "thought it, saw the ad" question replaces "Your information is being sold."
- **Claim fixed:** "sold" now means attention and predicted behavior. Brokers selling raw data is a separate, smaller point.
- **Merged** the old "what they know" and "how it's collected" slides.
- **Added** pipeline, inference/homophily/shadow profiles, feeds and bias, and breaches/KYC.
- **Shrunk** doxxing and OSINT into one trigger line on slide 8.
- **Removed** hard-coded page numbers (they break when you reorder slides) and the speaker A/B split.
- **Dropped** the market-size numbers ($264B, $471B, 5,000 brokers) because I haven't verified them. Re-add only with a checked source.

## Sources to pull before presenting

- Facebook emotional contagion study (2014, PNAS) and the 2017 leaked "insecure teens" document (Facebook disputed the framing)
- Equifax breach 2017
- Reported Bangladesh NID exposure (confirm year and details)
- Data broker estimates (CNBC/NBC piece from v1, Mozilla, Proton), if you keep any numbers
- Any reference for the claim that phones are not secretly listening for ads (so you can answer if someone challenges the hook)
d