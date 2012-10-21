
tags = [
  'Age 20',
  'Age 30',
  'Age 40',
  'Age 50',
  'Age 60',
  'Everyone',

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
  ('Age', True, 'Age 20', 'Age 30', 'Age 40', 'Age 50', 'Age 60', 'Everyone'),
  ('Goal', True, 'Health', 'Fun', 'Creativity', 'Spirituality', 'Nutrition'),
  ('Life event', True, 'Injury', 'Pregnancy', 'Menopause', 'Anniversary'),
  ('Challenge', True, 'Under 30'),
  #('Rock Climbing', False, 'Age 20', 'Age 30', 'Fun', 'Health'),
  #('Tai Chi', False, 'Age 40', 'Age 50', 'Age 60', 'Health'),
]

activities = [
  #('Rock Climbing', 'Do you like skinned knees? This is the sport for you!'),
  #('Tai Chi', 'Slow motion energy wrangling.'),
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

snaps2 = """
Running - health, age 20-60, injury, anniversary, menopause, under30 - Learn how to run.

Tai Chi - everyone, age 40-60 -  Soft moving ancient movement art.

Qi Gong -  age 40-60 - Ancient elemental slow moving self moving energy work.

Climbing Gym - age 20-40, anniversary, under30 - Strap in and go up but dont forget your belay partner cuz you cant climb alone!

Biking Classes - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Cycle on that bike.

Aerobics - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance-like moving in a room, sweating it out.

Dance - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance in a variety of different modalities.

Zumba - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance in a variety of different modalities.

African - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance in a variety of different modalities.

Samba - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance in a variety of different modalities.

Hip Hop - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dance in a variety of different modalities.

Hiking - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Go into nature to both relax and restore while getting exercise.

Boot Camps - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Outdoor or in gym groups that push you to your physical edges.

Feldenkrais - health, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Gentle movement training to create greater efficiency in movement.
 
Kiting - age 20-40 - Gooooooo fly and surf at the same time!

Surfing - age 20-40 - Ride the waves but dont forget your booties its coooold!

Sky Diving - age 20-40 - Ever wonder what it feels like to risk your life by choice? Jump out and fly!
"""

snaps3 = """\
Meditation Classes - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Learn to sit through it.

Mindfulness Classes - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Learn to sit through it and other techniques for careful living.

Qi Gong - spirituality, age 40-60 - Soft fluid moving meditation.

Tai Chi - spirituality, age 40-60 - Soft fluid moving meditation often with animal forms.

Course in Miracles Groups - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Spiritual study group to deepen your forgiveness and align a graceful spirit.

Prayer Groups - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Religious or non-religious conscious relating to the divine.

Tantra - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Deep intimacy training moving through your fears and resistances to just being with one another and experience the acceptance and splendor of not having to do anything to feel accepted.

Relationship Communication Classes - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Refine re-build healthy tools for better relating.

Conflict Resolution Classes - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Dont just hide from confrontation learn how to effectively handle them.

Parenting Classes - spirituality, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Teach your children with love and compassion.

Acting Classes - creativity, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Express yourself through theater.

Ceramics Classes - creativity, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Play with clay.

Poetry - creativity, age 20-60, injury, anniversary, pregnancy, menopause, under30 - Write poetry and share it with others.

Welding - creativity, age 20-60, injury, anniversary, menopause, under30 - Metal bending.
"""

for snap in (snaps + snaps2 + snaps3).split('\n'):
  if len(snap.strip()) == 0: continue
  parts = snap.split(' - ')
  title = parts[0]
  oldtags = [x.strip() for x in parts[1].split(',')]
  newtags = []
  for tag in oldtags:
    if tag == 'age 20-60':
      tags.extend(['Age 20', 'Age 30', 'Age 40', 'Age 50', 'Age 60'])
    elif tag == 'age 20-40':
      tags.extend(['Age 20', 'Age 30', 'Age 40'])
    elif tag == 'age 40-60':
      tags.extend(['Age 40', 'Age 50', 'Age 60'])
    else:
      newtags.append(tag[0].upper()+tag[1:])
  body =  parts[2]
  tagsets.append([title, False] + newtags)
  activities.append((title, body))

