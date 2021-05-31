# -*- coding: utf-8 -*-

from odoo import models, fields


class Class(models.Model):
    _name = 'web_school.class'
    _description = 'A Class'

    name = fields.Char()
    professor = fields.Char()
    # student_ids = fields.Many2many('web_school.student')