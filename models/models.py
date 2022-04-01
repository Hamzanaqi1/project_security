# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

from odoo.exceptions import UserError, AccessError, ValidationError, RedirectWarning



class project_security(models.Model):
    _inherit = 'project.task'
    aaa=fields.Char()
    def write(self,vals):
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        print(' write(self,val write(self,val write(self,val')
        res= super(project_security, self).write(vals)
        if(self.env.user.has_group('project_security.group_5')):
            if(self.stage_name not in ['Esperando Pasta','Pasta','Fondo y Decorado','Empaque','Enviada']):
                raise UserError(_("Sorry you do not have access to modify this record."))
        return res
                

        
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
