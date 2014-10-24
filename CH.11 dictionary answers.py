__author__ = 'Dark-Knight'


BreakingBad = {'a': 'You’re an insane, degenerate piece of filth, and you deserve to die.','b': 'Stay out of my territory','c': 'No more half-measures.',
'd': 'I am the one who knocks.', 'e': "Just because you shot Jesse James, don't make you Jesse James.", 'f': 'Shut the f--- up and let me die in peace.'}
print(BreakingBad['d'])
print(BreakingBad.get('d'))
for i in BreakingBad:
    print(BreakingBad[i])
for key in BreakingBad:
    if key == 'a':
        print("I like Pie")
