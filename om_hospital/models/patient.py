from odoo import api,fields, models


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Patient Model"

    name = fields.Char(String="name")
    age = fields.Integer(String="age")
    gender = fields.Selection([('male','Male'),('female','Female')],String="gender")