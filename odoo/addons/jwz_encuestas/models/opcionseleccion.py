from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpcionSeleccion(models.Model):
    _name = 'jwz_encuestas.opcionseleccion'
    _description = 'Opción Selección'

    name = fields.Char(string="ID", required=True)
    respuesta_id = fields.Many2one('jwz_encuestas.respuestas', string='Respuesta')
    opcion = fields.Char(string='Opción',required=True)

    @api.constrains('name')
    def _check_name_is_numeric(self):
        for record in self:
            if not record.name.isdigit():
                raise ValidationError("El ID de la opción debe ser un número.")

    @api.constrains('name', 'respuesta_id')
    def _check_id_is_unique(self):
        for opcion in self:
            existing_options = self.search([('name', '=', opcion.name), ('respuesta_id', '=', opcion.respuesta_id.id)])
            if len(existing_options) > 1:
                raise ValidationError("El ID de la opción debe ser único dentro de una respuesta.")