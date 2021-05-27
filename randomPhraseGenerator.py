# This exercise comes from Head First Learn to Code, location 660.
# It's all about setting up a random phrase generator made of noun, verbs, and adjectives.

import random

# Create 3 lists - 1 for each type of word:
verbs = ['Leverage', 'Sync', 'Gamify', 'Offline', 'Crowd-sourced',
    '24/7', 'Lean-in', '30,000 foot', 'Synergize', 'Explode']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed',
    'B-to-B', 'Oriented', 'Cloud-based', 'API-based', 'Pay-to-win']

nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page',
    'Productivity', 'Process', 'Tipping Point', 'Paradigm', 'Home-grown']

# Now, we set new variables to be our randomized bits for the final phrase:
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Here's the final, randomized phrase:
phrase = verb + ' ' + adjective + ' ' + noun
print(phrase)