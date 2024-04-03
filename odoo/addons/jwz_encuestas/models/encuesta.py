from odoo import models, fields

class Encuesta(models.Model):
    _name = 'jwz_encuestas.encuesta'
    _description = 'Encuesta'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    preguntas_ids = fields.Many2many('jwz_encuestas.pregunta', string='Preguntas')
    imagen = fields.Binary(string="Imagen", store=True, help="Seleccionar imagen aquí")
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_curso', 'En Curso'),
        ('finalizada', 'Finalizada')],
        string='Estado', default='borrador')