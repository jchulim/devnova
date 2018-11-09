# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(
        required=True,
        string='Title',
    )
    description = fields.Text(
    )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        ondelete='set null',
        string='Responsible',
        index=True,
    )
    session_ids = fields.One2many(
        comodel_name='openacademy.session',
        inverse_name='course_id',
        string='Sessions',
    )
