from odoo import fields,models,api

class WayBill(models.Model):
    _name = 'way.bill'

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('way.bill.no') or '/'
    #
    #     res = super(WayBill, self).create(vals)
    #     return res
    #
    # name = fields.Char(string='Event No', required=True, index=True, copy=False, default='New', readonly=1)
    date = fields.Date()
    name = fields.Char('Way Bill No')
    loading = fields.Char()
    delivery = fields.Char('Delivery Point')
    ldg_ref = fields.Selection([('port','PORT'),('terminal','TERMNAL'),('whouse','W/HOUSE'),('other','OTHER')])
    job_no = fields.Char()
    special = fields.Boolean()
    dyna = fields.Boolean()
    lory = fields.Boolean()
    six = fields.Boolean()
    flat = fields.Boolean()
    sn = fields.Boolean('S.N')
    gs = fields.Boolean('G.S')
    curtain = fields.Boolean()
    refr = fields.Boolean('Refr.')
    lobid = fields.Boolean()
    forklift = fields.Boolean()
    other = fields.Char()
    other_bool = fields.Boolean()
    consignee_id = fields.Many2one('res.partner',string="Consignee Name")
    abandonee_id = fields.Many2one('res.partner',string="Abandonee Name")
    cargo_lines = fields.One2many('cargo.lines','way_bill_id')
    driver = fields.Char('Driver Name')
    id_no = fields.Char('I.D. No')
    vehicle_no = fields.Char('Vehicle No')
    mobile_no = fields.Char('Mobile No')
    received = fields.Boolean('Received All the Shipment in Good Condition')
    rec_name = fields.Char()
    rec_mobile_no = fields.Char('Mobile No')
    rec_date = fields.Date('Date')
    remarks = fields.Text()
    carge_consignee = fields.Float('Charges On Consignee')
    carge_abandonee = fields.Float('Charges On Abandonee')
    basic_charge = fields.Float('Basic Fees')
    other_charges = fields.Float('Other Charges')
    charge_description = fields.Char('Other Charge Description')
    total_fees = fields.Float('Total Fees')
    tax = fields.Many2many('account.tax',string='Tax')
    amount_total = fields.Float('Amount Total')
    dispatch_time = fields.Datetime()
    arrival_time = fields.Datetime()

    @api.onchange('basic_charge','other_charges')
    def compute_total_fees(self):
        if self.basic_charge:
            if self.other_charges:
                self.total_fees = self.basic_charge + self.other_charges

    @api.onchange('total_fees','tax')
    def compute_amount_total(self):
        if self.total_fees:
            if self.tax:
                tax_value = self.env['account.tax'].search([('name','=',self.tax.name)])
                for tax in tax_value:
                    amount_total = self.total_fees*(tax.amount/100)
                    self.amount_total = self.total_fees + amount_total





class CargoLines(models.Model):
    _name = 'cargo.lines'

    way_bill_id = fields.Many2one('way.bill')
    description = fields.Char()
    quantity = fields.Float()
    weight = fields.Float()



