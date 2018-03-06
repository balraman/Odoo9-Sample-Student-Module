import time
from openerp import api, models, fields, _
from openerp.exceptions import UserError, ValidationError
import openerp.addons.decimal_precision as dp
import re
import datetime
import logging
_logger = logging.getLogger(__name__)

class Student(models.Model):
	_name = 'student.detail'

	name = fields.Char('Name', required=True)
	street = fields.Char('Street')
	street2 = fields.Char('Street2')
	zip_code = fields.Char('Zip', size=24)
	city = fields.Char('City')
	state_id = fields.Many2one('res.country.state', string='State')
	country_id = fields.Many2one('res.country', string='Country')
	education = fields.Char('Education')
	
	@api.multi
	def onchange_state(self, state_id):
		if state_id:
			state = self.env['res.country.state'].browse(state_id)
			return {'value': {'country_id': state.country_id.id}}
		return {'value': {}}
