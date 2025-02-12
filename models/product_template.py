from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    default_code = fields.Char(
        'Part Number', compute='_compute_default_code',
        inverse='_set_default_code', store=True)
    
    @api.depends('product_variant_ids.default_code')
    def _compute_default_code(self):
        self._compute_template_field_from_variant_field('default_code')

    def _set_default_code(self):
        self._set_product_variant_field('default_code')