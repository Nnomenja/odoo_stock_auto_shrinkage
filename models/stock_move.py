from odoo import models, fields

class StockMove(models.Model):
    _inherit = "stock.move"

    final_qty = fields.Float(
        string="Quantité finale",
        related="purchase_line_id.final_qty",
        store=True,
        readonly=True,
        digits="Product Unit of Measure",
    )