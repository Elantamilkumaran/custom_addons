from odoo import fields,models

class StudentSkill(models.Model):

    _name='student.skill'
    _description='Student Skill'

    name=fields.Char(string='Name',required=True)
    level=fields.Selection(
        [
            ('ad','Advanced'),
            ('im','Intermediate'),
            ('am','Amateaur'),
            ('bg','Beginner')
        ],
        required=True,
        default='am'
    )
    student_id=fields.Many2one(
        'student.management',
        string='Student',
        ondelete='cascade'
    )
#end
