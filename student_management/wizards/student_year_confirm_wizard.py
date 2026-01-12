from odoo import fields,models
class StudentYearConfirmWizard(models.TransientModel):
    _name='student.year.confirm.wizard'
    _description='Confirm year change'

    student_id=fields.Many2one('student.management')
    direction=fields.Selection(
        [
            ('next','Next'),
            ('previous','Previous')
        ]
    )

    next_year_label = {'year1':'year2', 'year2':'year3', 'year3':'year4'}
    previous_year_label = {'year2':'year1', 'year3':'year2', 'year4':'year3'}
    
    # def action_confirm(self):
    #     year_list=['year1','year2','year3','year4']
    #     student=self.student_id
    #     current_index=year_list.index(student.year_stage)
    #     if self.direction =='next' and current_index<3:
    #         student.year_stage=year_list[current_index+1]
    #     elif self.direction =='previous' and current_index>0:
    #         student.year_stage=year_list[current_index-1]

    def action_confirm(self):
        if self.direction == 'next':
            self.student_id.year_stage = self.next_year_label[self.student_id.year_stage]
        elif self.direction == 'previous':
            self.student_id.year_stage = self.previous_year_label[self.student_id.year_stage]