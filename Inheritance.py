class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print(self.incantation)
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self): #Just add this for the function. (d)
        return 'This charm summons an object to the caster, potentially over a significant distance' #and then add this to add the description. (d)
class Confundo(Spell): #Wrong indentation was causing it to be inside the class Accio.
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
    def study_spell(spell):
        print(spell)
spell = Accio()
spell.execute()
#study_spell(spell)
#study_spell(Confundo())
print(Accio())
#a. Spell is the parent, Accio is the child.
#b. The incantation of Accio, the name of Accio and the name of Confundo.
#c. None, study_spell only prints the name of the spell and notheing else.
#d. Comment lines.