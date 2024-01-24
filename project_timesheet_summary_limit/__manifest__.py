# Copyright 2018-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Project timesheet summary limit",
    "summary": """
        This module limits the timesheet summary to show 20 records per page.
    """,
    "author": "Sodexis",
    "website": "https://sodexis.com/",
    "category": "Project Management",
    "version": "16.0.1.0.0",
    "license": "OPL-1",
    "depends": [
        "hr_timesheet",
    ],
    "data": [
        "views/project_view.xml",
    ],
    "installable": True,
    "images": ["images/main_screenshot.jpg"],
}
