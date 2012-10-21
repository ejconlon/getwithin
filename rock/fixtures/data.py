
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
  'Nutrition'
]

tagsets = [
  ('Age', True, 'Age 20', 'Age 30', 'Age 40', 'Age 50', 'Age 60'),
  ('Goal', True, 'Health', 'Fun', 'Creativity', 'Spirituality', 'Nutrition'),
  ('Rock Climbing', False, 'Age 20', 'Age 30', 'Fun', 'Health'),
  ('Tai Chi', False, 'Age 50', 'Age 60', 'Health'),
]

activities = [
  ('Rock Climbing', 'Do you like skinned knees? This is the sport for you!'),
  ('Tai Chi', 'Slow motion energy wrangling.'),
]

events = [(x, 'Tai Chi') for x in 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')]

