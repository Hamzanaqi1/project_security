# -*- coding: utf-8 -*-

from odoo import models, fields, api




class project_security(models.Model):
    _inherit = 'project.task'
    stage_name=fields.Char(compute='_compute_stage_name',store=True)
    @api.depends('stage_id')
    def _compute_stage_name(self):
        for r in self:
            r.stage_name=r.stage_id.name

#     _description = 'project_security.project_security'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
