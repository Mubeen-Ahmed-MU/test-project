from odoo import fields, models, api


class TestProject(models.Model):
    _name = "test.project.with"
    _description = "This is Test Project"

    name = fields.Char(string="Name")
