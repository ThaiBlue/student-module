# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = 'web_school.student'
    _description = 'A Student'

    name = fields.Char()
    gender = fields.Char()
    birth_date = fields.Date()
    faculty = fields.Char()
    # class_ids = fields.Many2many('web_school.class')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100