
tags = [
  'Age 20',
  'Age 30',
  'Age 40',
  'Age 50',
  'Age 60',

  'Health',
  'Fun',
  'Creativity',
  'Spirituality',
  'Nutrition',

  'Injury',
  'Pregnancy',
  'Menopause',
  'Anniversary',

  'Under 30',
]

tagsets = [
  ('Age', True, 'Age 20', 'Age 30', 'Age 40', 'Age 50', 'Age 60'),
  ('Goal', True, 'Health', 'Fun', 'Creativity', 'Spirituality', 'Nutrition'),
  ('Life event', True, 'Injury', 'Pregnancy', 'Menopause', 'Anniversary'),
  ('Challenge', True, 'Under 30'),
  ('Rock Climbing', False, 'Age 20', 'Age 30', 'Fun', 'Health'),
  ('Tai Chi', False, 'Age 40', 'Age 50', 'Age 60', 'Health'),
]

activities = [
  ('Rock Climbing', 'Do you like skinned knees? This is the sport for you!'),
  ('Tai Chi', 'Slow motion energy wrangling.'),
]

events = [(x, 'Tai Chi') for x in 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')]

snaps = """
Chiropractic - health, age 20-60, injury - Spinal manipulations so you can rest medicine.

Acupuncture - health, age 20-60, injury, pregnancy, menopause, anniversary, under 30 - Flying needles at magnetic points in your body somehow produce a health benefit? Seems to work since there are a million people practicing here and it's like 5,000 years old or something like that.

Swedish Massage - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Rest and relax on a table receiving soft muscle tissue massage with oil.  Feel good massage.

Rolfing - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Often painful really really deep massage changing your muscle patterns often ending up with postural changes.

Deep Tissue Massage - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Deep pressure massage for hose more stubborn knots in your muscles.

Myofacial Release - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Intuitive touch with lighter pressure that releases muscle tension.

Cranial Sacral - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Incredibly gentle deep and slow holding of different areas hooding tension and supporting release on very deep levels helps tmj, vertigo, birth trauma, headaches, ringing ears.

Zero Balancing - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Energy balancing.

Polarity Therapy - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Energy balancing.

Biofeedback Session - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Re-patterning neural networks resulting in transformation of consciousness.

Shamanic Journey - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Lay down close your eyes and listen to the drum while you consciously travel to upper-middle or lower worlds and meet your spirit allies and learn valuable insights into your life.

Naturopathic Consultation - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Preventative medicine doctors using herbs, homeopathy, acupuncture, supplements, and holistic medicine.

Hypnosis - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Follow the light and just listen to my voice.... Learn to re-pattern your subconscious mind for better health make choices about which areas you want to improve and voila! Watch the magic in effect.

Yoga - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Get a yoga mat and pray through your body while making interesting shapes.

Pilates - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Work that core with a variety leg lifting and hip bending exercises.
"""

for snap in snaps.split('\n'):
  if len(snap) == 0: continue
  parts = snap.split(' - ')
  title = parts[0]
  oldtags = [x.strip() for x in parts[1].split(',')]
  newtags = []
  for tag in oldtags:
    if tag == 'age 20-60':
      tags.extend(['Age 20', 'Age 30', 'Age 40', 'Age 50', 'Age 60'])
    else:
      newtags.append(tag[0].upper()+tag[1:])
  body =  parts[2]
  tagsets.append([title, False] + newtags)
  activities.append((title, body))

