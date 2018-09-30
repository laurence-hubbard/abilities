import re

def abilities(instance):
  instance_class = instance.__class__
  all_abilities = list(set(dir(instance))-set(dir(instance_class.__bases__)))
  all_abilities.sort()
  print('###\nThe key abilities of ',instance_class,' are:\n')
  for ability in all_abilities:
    if re.match(r"^[^_]*$", ability):
      print(ability)
  return all_abilities
