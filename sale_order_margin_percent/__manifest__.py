# Copyright 2017 PESOL (http://pesol.es)
#                Luis Adan Jimenez Hernandez (luis.jimenez@pesol.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Order Margin Percent",
    "summary": "Show Percent in sale order",
    "version": "12.0.1.1.1",
    "category": "Sales",
    "website": "https://github.com/OCA/margin-analysis",
    "author": "PESOL, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'sale_margin'
    ],
    "data": [
        'views/sale_order_margin_percent_view.xml',
    ]
}
