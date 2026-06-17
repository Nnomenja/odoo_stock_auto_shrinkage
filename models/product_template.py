from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # -------------------------------------------------------------------------
    #                                                                    FIELDS 
    # -------------------------------------------------------------------------
    freinte_percent = fields.Float(
        string="Freinte (%)",
        digits=(16, 2),
        help="Pourcentage de perte naturelle du produit."
    )

    # -------------------------------------------------------------------------
    #                                                           SQL CONSTRAINTS 
    # -------------------------------------------------------------------------

    _check_freinte_percent_range = models.Constraint(
        'CHECK(freinte_percent >= 0 AND freinte_percent <= 100)',
        'Le pourcentage de freinte doit être compris entre 0 et 100.'
    )