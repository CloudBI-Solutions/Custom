# Copyright 2023 JumpTo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Add calendar view to attendance, hr_attendance_calendar_view",
    "summary": """
        This module adds the calendar view as an option to display attendance""",
    "license": "AGPL-3",
    "author": "Eqilibrium Solutions",
    "website": "https://www.eqilibriumsolutions.com",
    "category": "Human Resources",
    "version": "16.0.1.0.0",
    "depends": ["base", "hr_attendance"],
    "data": [
        "views/hr_attendance_calendar_views.xml",
    ],
}
