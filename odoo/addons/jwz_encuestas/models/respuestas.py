from odoo import models, fields

class RespuestaS(models.Model): 
    _name = 'jwz_encuestas.respuestas'
    _description = 'Respuesta Selección'

    name =fields.Char(string='Respuesta')
    pregunta_id = fields.Many2one('jwz_encuestas.pregunta', string='Pregunta')
    opciones_ids = fields.One2many('jwz_encuestas.opcionseleccion', 'respuesta_id', string='Opciones')
    elegida = fields.Many2one('jwz_encuestas.opcionseleccion', string='Tu Selección', domain="[('respuesta_id', '=', id)]")
