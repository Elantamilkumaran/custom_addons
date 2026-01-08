from odoo import fields, models

class BookReviewTag(models.Model) :

    _name = 'book.review.tag'
    _description = 'Book Review Tag'

    name = fields.Char(
        required = True
    )

    color = fields.Char()