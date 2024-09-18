from odoo import api,fields, models


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description="Appointment Model"
    _inherit=["mail.thread","mail.activity.mixin"]
    _rec_name="ref"

    patient_id=fields.Many2one("hospital.patient",String="Patient")
    appointment_time =fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    gender = fields.Selection(related='patient_id.gender')
    booking_date=fields.Date(string="Booking Date",default=fields.Date.context_today)
    ref = fields.Char(String="Reference",readonly=True)
    prescription=fields.Html()
    priority=fields.Selection([
        ('0','No'),
        ('1','Low'),
        ('2','Normal'),
        ('3','High')
    ],string="Priority")
    state=fields.Selection([
        ('draft','Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel','Cancel'),
    ])
    doctor_id=fields.Many2one('res.users',string="Doctor")

    @api.onchange('patient_id')
    def set_ref(self):
        for rec in self:
            rec.ref = rec.patient_id.ref

    def cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def increment_priority(self):
        for rec in self:
            p = int(rec.priority)
            if p<3:
                rec.priority=p+1
    def decrement_priority(self):
        for rec in self:
            p = int(rec.priority)
            if p>0:
                rec.priority=p-1

