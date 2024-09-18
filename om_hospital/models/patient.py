from datetime import *
from odoo import api,fields, models



class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Patient Model"
    _inherit=["mail.thread","mail.activity.mixin"]

    name = fields.Char(String="Name",tracking=True)
    date_of_birth = fields.Date(String="Date Of Birth",tracking=True)
    age = fields.Integer(String="Age",tracking=True,compute="_compute_age")
    gender = fields.Selection([('male','Male'),('female','Female')],String="Gender",tracking=True)
    ref = fields.Char(String="Reference",tracking=True)
    active = fields.Boolean(String="Active",tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age= datetime.today().year - rec.date_of_birth.year
            else:
                rec.age=1