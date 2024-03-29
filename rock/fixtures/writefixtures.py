#!/usr/bin/env python

from data import *

def write_block(model, pk, pairs):
  s = "- model: %s\n  pk: %d\n  fields:\n" % (model, pk)
  for k, v in pairs:
    s += "    %s: %s\n" % (k, v)
  return s

def dfilter(d, keys):
  e = {}
  for k in keys:
    if k in d:
      e[k] = d[k]
  return e

def modify_tags(tags):
  new_tags = []
  for tag in tags:
    new_tag = {}
    new_tag['slug'] = tag.lower().replace(' ', '')
    new_tag['body'] = tag
    new_tags.append(new_tag)
  return new_tags

def modify_tagsets(tagsets, slug_to_tag_pk):
  new_tagsets = []
  for tagset in tagsets:
    new_tagset = {}
    new_tagset['title'] = tagset[0]
    new_tagset['slug'] = tagset[0].lower().replace(' ', '')
    new_tagset['highlighted'] = tagset[1]
    new_tagset['tags'] = []
    for title in tagset[2:]:
      slug = title.lower().replace(' ', '')
      pk = slug_to_tag_pk[slug]
      new_tagset['tags'].append(pk)
    new_tagsets.append(new_tagset)
  return new_tagsets 

def modify_activities(activities, slug_to_tagset_pk):
  new_activities = []
  for activity in activities:
    new_activity = {}
    new_activity['title'] = activity[0]
    new_activity['slug'] = activity[0].lower().replace(' ', '')
    new_activity['body'] = activity[1]
    new_activity['tag_set'] = slug_to_tagset_pk[new_activity['slug']]
    new_activities.append(new_activity)
  return new_activities

def modify_events(events, slug_to_activity_pk):
  new_events = []
  for event in events:
    new_event = {}
    new_event['month'] = event[0]
    new_event['activity'] = slug_to_activity_pk[event[1].lower().replace(' ', '')]
    new_events.append(new_event)
  return new_events

tag_keys = ['slug', 'body']
tagset_keys = ['slug', 'title', 'highlighted', 'tags']
activity_keys = ['slug', 'title', 'body', 'tag_set']
event_keys = ['month', 'activity']

slug_to_tag_pk = {}
slug_to_tagset_pk = {}
slug_to_activity_pk = {}
ystr = ""

tags = modify_tags(tags)

pk = 1
for tag in tags:
  ystr += write_block('rock.tag', pk, dfilter(tag, tag_keys).items())
  slug_to_tag_pk[tag['slug']] = pk
  pk += 1

tagsets = modify_tagsets(tagsets, slug_to_tag_pk)

pk = 1
for tagset in tagsets:
  ystr += write_block('rock.tagset', pk, dfilter(tagset, tagset_keys).items())
  slug_to_tagset_pk[tagset['slug']] = pk
  pk += 1

activities = modify_activities(activities, slug_to_tagset_pk)  

pk = 1
for activity in activities:
  ystr += write_block('rock.activity', pk, dfilter(activity, activity_keys).items())
  slug_to_activity_pk[activity['slug']] = pk
  pk += 1

events = modify_events(events, slug_to_activity_pk)

pk = 1
for event in events:
  ystr += write_block('rock.event', pk, dfilter(event, event_keys).items())
  pk += 1

print ystr

