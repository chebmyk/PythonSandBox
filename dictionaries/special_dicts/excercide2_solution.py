from collections import defaultdict, Counter

eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")

class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color


from random import seed, choices
seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]

print(persons)

# Some other collection (say recovered from a database, or an external API) contains a list of `Person` objects that have an eye color property.
# Your goal is to create a dictionary that contains the number of people that have the eye color as specified in `eye_colors`.
# The wrinkle here is that even if no one matches some eye color, say `amber`, your dictionary should still contain an entry `"amber": 0`.
#


# Write a function that returns a dictionary with the correct counts for each eye color listed in `eye_colors`.

def color_count(persons):
    result = Counter({color : 0 for color in eye_colors})
    for p in persons:
        result.update({p.eye_color: 1})
    return result


print(color_count(persons))