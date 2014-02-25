__author__ = 'Charlie'
from PIL import ImageFont


SKILL_FONT_POINT_SIZE = 20
SKILL_FONT = ImageFont.truetype("resources/present_lt_black_condensed.ttf", SKILL_FONT_POINT_SIZE)
SKILL_LINE_THICKNESS = 2
SKILL_FONT_SIZE = SKILL_FONT.getsize("X")[1]

TITLE_FONT_SIZE = 28
TITLE_FONT = ImageFont.truetype("resources/present_lt_black_condensed.ttf", TITLE_FONT_SIZE)

SHEET_BACKGROUND_COLOR = "white"
SHEET_FOREGROUND_COLOR = "black"

SKILLS_USE_TALLYS = True
SKILLS_CELL_WIDTH = 200
SKILLS_CELL_HEIGHT = SKILL_FONT_SIZE + 7
SKILL_VERTICAL_SPACING = SKILL_FONT_SIZE + 10
SKILLS_BOX_SIZE = (SKILLS_CELL_WIDTH, SKILL_VERTICAL_SPACING * 20)