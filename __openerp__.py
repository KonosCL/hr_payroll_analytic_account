# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Payroll Chilean Accounting',
    'version': '1.0',
    'category': 'Accounting',
    'author': 'Blanco Martin & Asociados - Nelson Ramírez Sánchez, Daniel Blanco',
    'description': """
Generic Payroll system Integrated with Chilean Accounting.
==================================================

    * Analytic Accounting

    """,
    'website': 'http://blancomartin.cl',
    'depends': [
        'hr_payroll_account','account_analytic_analysis'
    ],
    'data': ['l10n_cl_hr_payroll_account_view.xml'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
