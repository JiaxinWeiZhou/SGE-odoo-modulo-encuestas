from odoo import models, fields

class Pregunta(models.Model):
    _name = 'jwz_encuestas.pregunta'
    _description = 'Pregunta'

    name = fields.Char(string='Pregunta', required=True)
    encuestas_ids = fields.Many2many('jwz_encuestas.encuesta', string='Encuestas')
    tipo = fields.Selection([
        ('Texto', 'Respuesta Texto'),
        ('Seleccion', 'Respuesta Selección')
        ], string='Tipo de pregunta')
    respuesta_t_ids = fields.One2many('jwz_encuestas.respuestat', 'pregunta_id', string='Respuesta Texto')
    respuesta_s_ids = fields.One2many('jwz_encuestas.respuestas', 'pregunta_id', string='Respuesta Selección')
    