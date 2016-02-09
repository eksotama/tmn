# -*- coding: utf-8 -*-
# © 2016 Andhitia Rama <andhitia.r@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_emoney_member = fields.Boolean(
        string='E-money Member',
        )

    is_emoney_agent = fields.Boolean(
        string='E-money Agent',
        )

    is_emoney_merchant = fields.Boolean(
        string='E-money Merchant',
        )
