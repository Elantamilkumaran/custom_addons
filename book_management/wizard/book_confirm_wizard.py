from odoo import fields, models, api

class BookConfirmWizard(models.TransientModel):
    _name = 'book.confirm.wizard'
    _description = 'Confirm state change'

    book_id = fields.Many2one('book.management')
    direction = fields.Selection(
        [
            ('next', "Next"),
            ('previous', "Previous")
        ],
        required = True
    )

    next_stage = {
            'new' : "writing",
            'writing' : "correction",
            'correction' : "published"
            }
    previous_stage = {
            'writing' : "new",
            'correction' : "writing",
            'published' : "correction"
            }
    
    @api.depends('direction')
    def action_confirm(self):

        self.ensure_one()

        if self.direction == 'next':
            self.book_id.status = self.next_stage[self.book_id.status]
        elif self.direction == 'previous':
            self.book_id.status = self.previous_stage[self.book_id.status]