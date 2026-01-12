from odoo import models, fields, api

class book(models.Model) :
    _name = 'book.management'
    _description = 'Book Management'

    book_id = fields.Integer(string='Book ID', required=True)
    book_title = fields.Char(string='Book Title', size=500, required = True, index=True)
    book_author = fields.Char(string = 'Book Author', size=100, required=True, default='unknown')
    book_rating = fields.Float(string="Rating", digits=(2,1), default=0.0, required=True)

    book_review_ids = fields.Many2many(
        'book.review.tag',
        string = 'Review',
        readonly=True,
        store=True,
        compute='_compute_review'
    )

    book_genre_ids = fields.Many2many(
        'book.genre',
        string='Genre'
    )

    status = fields.Selection(
        [
            ('new','New'),
            ('writing', "Writing"),
            ('correction', "Correction"),
            ('published', "Published")
        ],
        string="Status",
        default="new",
        required=True
    )

    def next_status(self) :
        for rec in self:
            if rec.status == 'new':
                rec.status = 'writing'
            elif rec.status == 'writing':
                rec.status = 'correction'
            else :
                rec.status = 'published'

    def previous_status(self) :
        for rec in self:
            if rec.status == 'published' :
                rec.status = 'correction'
            elif rec.status == 'correction' :
                rec.status = 'writing'
            else :
                rec.status = 'new'

    book_description=fields.Text()

    @api.depends('book_rating')
    def _compute_review(self):

        ReviewTag = self.env['book.review.tag']

        for rec in self:
            # clear old tags
            rec.book_review_ids = [(5, 0, 0)]

            if rec.book_rating < 2.0:
                tag_name = 'Very bad'
            elif rec.book_rating < 3.0:
                tag_name = 'Bad'
            elif rec.book_rating < 4.0:
                tag_name = 'Good'
            elif rec.book_rating < 6.0:
                tag_name = 'Nice'
            elif rec.book_rating < 8.0:
                tag_name = 'Very nice'
            else:
                tag_name = 'Excellent'

            tag = ReviewTag.search([('name', '=', tag_name)], limit=1)
            if tag:
                rec.book_review_ids = [(6, 0, tag.ids)]

    def open_next_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm Next Stage',
            'res_model': 'book.confirm.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_id': self.id,
                'default_direction': 'next',
            }
        }


    def open_previous_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm Previous Stage',
            'res_model': 'book.confirm.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_id': self.id,
                'default_direction': 'previous',
            }
        }
