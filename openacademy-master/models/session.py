# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(
        required=True,
    )
    start_date = fields.Date(
        default=fields.Date.today,
    )
    duration = fields.Float(
        digits=(6, 2),
        help='Duration in days',
    )
    seats = fields.Integer(
        string='Number of seats',
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher"),
        ],
        string='Instructor',
    )
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        ondelete='cascade',
        string='Course',
        required=True,
    )
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Attendees',
    )
    active = fields.Boolean(
        default=True,
    )

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    @api.one
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        if not self.seats:
            self.taken_seats = 0.0
        else:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
