from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Appointment Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "ref"

    patient_id = fields.Many2one("hospital.patient", String="Patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    gender = fields.Selection(related='patient_id.gender')
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(String="Reference", readonly=True)
    prescription = fields.Html()
    pharmacy_lines_ids= fields.One2many('pharmacy.lines','appointment_id',string="Pharmacy Lines")
    hide_price = fields.Boolean(string="Hide Price",default=False)
    priority = fields.Selection([
        ('0', 'No'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High')
    ], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ],default='draft')
    doctor_id = fields.Many2one('res.users', string="Doctor",tracking=True)

    @api.onchange('patient_id')
    def set_ref(self):
        for rec in self:
            rec.ref = rec.patient_id.ref

    def draft_method(self):
        for rec in self:
            rec.state = 'draft'
    def in_consultation_method(self):
        for rec in self:
            rec.state = 'in_consultation'
    def done_method(self):
        for rec in self:
            rec.state = 'done'
    def cancel_method(self):
        for rec in self:
            rec.state = 'cancel'

    def increment_priority(self):
        for rec in self:
            p = int(rec.priority)
            if p < 3:
                rec.priority = str(p + 1)

    def decrement_priority(self):
        for rec in self:
            p = int(rec.priority)
            if p > 0:
                rec.priority = str(p - 1)

class PharmacyLines(models.Model):
    _name="pharmacy.lines"
    _description="Pharmacy Lines Model"

    product_id=fields.Many2one('product.product',string="Product")
    qty=fields.Integer(string="Quantity",default=1)
    price=fields.Float(related='product_id.list_price')
    appointment_id=fields.Many2one("hospital.appointment", string="Appointment")