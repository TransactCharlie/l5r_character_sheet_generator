__Author__ = "Charlie"

from imgtools import generate_skills_mask, serve_pil_image
from skills import Skill
from flask import Flask

l5r = Flask(__name__)

@l5r.route("/about")
def about():
    return 'a service to generate character sheets for l5r'

@l5r.route("/imgtest")
def imgtest():
    skills = [
        Skill("Lore: Maho", 5),
        Skill("Iaijutsu", 5),
        Skill("Ettiquette", 2),
        Skill("Courtier", 1),
        Skill("Lore: Bushido", 3)
    ]
    return serve_pil_image(generate_skills_mask(skills))

if __name__ == '__main__':
    l5r.run(debug = True)