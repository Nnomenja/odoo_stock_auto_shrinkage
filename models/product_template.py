from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    freinte_percent = fields.Float(
        string="Freinte (%)",
        digits=(16, 2),
        help="Pourcentage de perte naturelle du produit."
    )

