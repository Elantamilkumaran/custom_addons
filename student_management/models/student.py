from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    # --------------------
    # BASIC DETAILS
    # --------------------
    name = fields.Char(string='Student Name',required=True)
    image_1920 = fields.Image(string="Profile Picture",help="Profile Photo")

    age = fields.Integer(string='Age',default="18")

    course = fields.Selection(
        [
            ('cse', 'Computer Science Engineering'),
            ('ece', 'Electronics and Communication Engineering'),
            ('eee', 'Electrical and Electronics'),
            ('mech', 'Mechanical Engineering'),
            ('civil', 'Civil Engineering'),
        ],
        string='Course',
        required=True
    )
    year_stage=fields.Selection(
        [
            ('year1','1st Year'),
            ('year2','2nd Year'),
            ('year3','3rd Year'),
            ('year4','4th Year'),
        ],
        string='Current Year',
        default='year1'
    )
    # --------------------
    # MARKS
    # --------------------
    internal_marks = fields.Float(string="Internal Marks")
    external_marks = fields.Float(string="External Marks")

    total_marks = fields.Float(
        string="Total Marks",
        compute="_compute_total_marks",
        store=True
    )

    # --------------------
    # GRADE
    # --------------------
    grade = fields.Selection(
        [
            ('outstanding', 'Outstanding'),
            ('excellent', 'Excellent'),
            ('good', 'Good'),
            ('fail', 'Fail'),
        ],
        string='Grade',
        compute="_compute_grade",
        store=True
    )
    skill_ids=fields.One2many(
        'student.skill',
        'student_id',
        string='Skills'
    )
    @api.depends('internal_marks', 'external_marks')
    def _compute_total_marks(self):
        for record in self:
            record.total_marks = (record.internal_marks or 0.0) + (record.external_marks or 0.0)

    @api.depends('total_marks')
    def _compute_grade(self):
        for record in self:
            if record.total_marks >= 90:
                record.grade = 'outstanding'
            elif record.total_marks >= 75:
                record.grade = 'excellent'
            elif record.total_marks >= 50:
                record.grade = 'good'
            else:
                record.grade = 'fail'
    
    def action_next_year(self):
        for rec in self:
            if rec.year_stage=='year1':
                rec.year_stage='year2'
            elif rec.year_stage=='year2':
                rec.year_stage='year3'
            elif rec.year_stage=='year3':
                rec.year_stage='year4'
    def action_prev_year(self):
        for rec in self:
            if rec.year_stage=='year4':
                rec.year_stage='year3'
            elif rec.year_stage=='year3':
                rec.year_stage='year2'
            elif rec.year_stage=='year2':
                rec.year_stage='year1'
    
    def action_next_year_confirm(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm',
            'res_model': 'student.year.confirm.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_student_id': self.id,
                'default_direction': 'next',
            }
        }


    def action_previous_year_confirm(self):
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm',
            'res_model': 'student.year.confirm.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_student_id': self.id,
                'default_direction': 'previous',
            }
        }


#end