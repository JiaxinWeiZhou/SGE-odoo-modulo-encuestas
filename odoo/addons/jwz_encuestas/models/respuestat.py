from odoo import models, fields

class RespuestaT(models.Model): 
    _name = 'jwz_encuestas.respuestat'
    _description = 'Respuesta Texto'

    name = fields.Char(string='Respuesta')
    pregunta_id = fields.Many2one('jwz_encuestas.pregunta', string='Pregunta')
    respuesta = fields.Text(string='Tu respuesta')
    