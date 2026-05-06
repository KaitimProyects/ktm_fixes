# -*- coding: utf-8 -*-
{
    "name": "Kaitim MRP Fixes",
    "summary": "Temporary fixes for Odoo MRP core bugs pending upstream resolution",
    "description": """
    Temporary patches for known Odoo MRP bugs. Each fix is documented
    with a reference to the upstream issue or commit so it can be removed
    once the core ships the official solution.
    """,
    "author": "Kaitim",
    "website": "https://www.kaitim.com",
    "category": "Manufacturing",
    "version": "18.0.1.0.0",
    "depends": ["mrp"],
    "data": ["views/mrp_production_views.xml"],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
