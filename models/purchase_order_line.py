from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    # -------------------------------------------------------------------------
    #                                                                    FIELDS 
    # -------------------------------------------------------------------------

    final_qty = fields.Float(
        string='Quantité finale (nette)',
        digits='Product Unit of Measure',
        readonly=True,
        help="Quantité finale après application de la freinte.",
        default=0,
        compute='_compute_final_qty',
    )


    # -------------------------------------------------------------------------
    #                                                           SQL CONSTRAINTS 
    # -------------------------------------------------------------------------

    _check_final_qty_positive = [
        ('final_qty_positive', 'CHECK(final_qty >= 0)', 'La quantité finale doit être positive.'),
    ]


    # -------------------------------------------------------------------------
    #                                                           DEPENDS METHODS 
    # -------------------------------------------------------------------------

    @api.depends('product_qty', 'product_id.freinte_percent')
    def _compute_final_qty(self):
        for line in self:
            freinte = line.product_id.freinte_percent or 0.0
            line.final_qty = line.product_qty - (
                line.product_qty * freinte / 100
            )

