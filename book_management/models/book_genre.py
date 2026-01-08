from odoo import fields, models

class BookGenre(models.Model) :

    _name = 'book.genre'
    _description = 'Book Genre'

    name = fields.Char(required = True)
    color = fields.Integer()