# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "L10n_AR Iva Import",
    "summary": """
        This module allows you to import supplier invoices extracted from AFIP/ARCA """,
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["base", "account"],
    "data": ["views/account_view.xml", "security/ir.model.access.csv"],
}
