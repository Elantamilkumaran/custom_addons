from odoo import models, fields, api

class book(models.Model) :
    _name = 'book.management'
    _description = 'Book Management'

    book_id = fields.Integer(string='Book ID', required=True)
    book_title = fields.Char(string='Book Title', size=500, required = True, index=True)
    book_author = fields.Char(string = 'Book Author', size=100, required=True, default='unknown')
    book_genre = fields.Selection(
        [
            ('ac', 'Action'),
            ('ad', 'Adventure'),
            ('ro', 'Romance'),
            ('cm', 'Comedy'),
            ('no', 'Novel'),
            ('fn', 'Fantasy'),
            ('st', 'Story'),
            ('hr', 'Horror'),
            ('tr', 'Thriller'),
            ('un', 'Unknown')
        ],
        required = True,
        default = "un"
    )
    book_rating = fields.Float(string="Rating", digits=(2,1), default=0.0, required=True)
    book_review = fields.Selection(
        [
            ('vb', 'Very bad'),
            ('b', 'Bad'),
            ('g', 'Good'),
            ('av', 'Average'),
            ('n', 'Nice'),
            ('vn', 'Very nice'),
            ('ex', 'Excellent')
        ],
        readonly=True,
        default = 'av',
        store=True,
        compute='_compute_review'
    )
    book_description=fields.Text()

    @api.depends('book_rating')
    def _compute_review(self):
        for rec in self:
            if rec.book_rating < 2.0:
                rec.book_review = 'vb'
            elif rec.book_rating < 3.0 :
                rec.book_review = 'b'
            elif rec.book_rating < 4.0 :
                rec.book_review = 'g'
            elif rec.book_rating < 6.0 :
                rec.book_review = 'n'
            elif rec.book_rating < 8.0 :
                rec.book_review = 'vn'
            elif rec.book_rating < 10.0 :
                rec.book_review = 'ex'