from odoo import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super().button_validate()

        for picking in self.filtered(
            lambda p: p.picking_type_code == 'incoming' and p.state == 'done'
        ):
            for move_line in picking.move_line_ids.filtered(lambda ml: ml.quantity > 0):
                qty_received = move_line.quantity
                qty_losed   = move_line.product_uom_id.round(qty_received * move_line.product_id.freinte_percent / 100)

                quant = self.env['stock.quant'].search([
                    ('product_id',   '=', move_line.product_id.id),
                    ('location_id',  '=', move_line.location_dest_id.id),
                    ('lot_id',       '=', move_line.lot_id.id if move_line.lot_id else False),
                ], limit=1)

                if quant and qty_losed > 0:
                    quant.with_context(inventory_mode=True).write({
                        'quantity': quant.quantity - qty_losed
                    })


        return res
