# tu_modulo/models/pos_config.py
from odoo import models, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    @api.model
    def write(self, vals):
        """ Sobreescribe el write para establecer el informe de ticket por defecto
            solo si no hay otro informe establecido.
        """
        # Obtenemos el ID externo de la acción de informe que creamos
        report_id = self.env.ref('tu_modulo.action_report_pos_order_minimal', raise_if_not_found=False)
        
        # Si la configuración de TPV no tiene un informe de recibo de orden y nuestro informe existe, lo establecemos.
        if report_id and not vals.get('report_order_id'):
            vals['report_order_id'] = report_id.id
            
        return super(PosConfig, self).write(vals)

    @api.model
    def create(self, vals):
        """ Sobreescribe el create para establecer el informe de ticket por defecto
            al crear una nueva configuración de TPV.
        """
        report_id = self.env.ref('tu_modulo.action_report_pos_order_minimal', raise_if_not_found=False)
        
        if report_id and not vals.get('report_order_id'):
            vals['report_order_id'] = report_id.id
            
        return super(PosConfig, self).create(vals)