#This file is part asterisk module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['User']
__metaclass__ = PoolMeta


class User():
    __name__ = "res.user"
    internal_number = fields.Char('Internal number',
        help="User's internal phone number.")
    callerid = fields.Char('Caller ID',
        help="Caller ID used for the calls initiated by this user.")
    asterisk_chan_type = fields.Selection([
            (None, ''),
            ('SIP', 'SIP'),
            ('IAX2', 'IAX2'),
            ('DAHDI', 'DAHDI'),
            ('Zap', 'Zap'),
            ('Skinny', 'Skinny'),
            ('MGCP', 'MGCP'),
            ('mISDN', 'mISDN'),
            ('H323', 'H323'),
            ], 'Asterisk channel type',
            help="Asterisk channel type, as used in the Asterisk dialplan. "
                "If the user has a regular IP phone, the channel type is "
                "'SIP'.")
    asterisk_server = fields.Function(fields.Many2One('asterisk.configuration',
            'Asterisk server',
            help="Asterisk server on which the user's phone is connected."),
            getter='get_asterisk_server')

    def get_asterisk_server(self, name=None):
        ConfigurationCompany = Pool().get('asterisk.configuration.company')
        if self.company:
            confs = ConfigurationCompany.search([
                    ('company', '=', self.company.id),
                    ], limit=1)
            if confs:
                return confs[0].id
        return None
