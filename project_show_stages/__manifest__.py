# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Project Show Stages",
    "summary": """
        This module helps us to configure the stages of
        projects in corresponding projects itself.""",
    "version": "16.0.1.0.0",
    "category": "Project Management",
    "website": "https://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        "base",
        "project",
    ],
    "data": [
        "views/project_view.xml",
    ],
    "images": ["images/main_screenshot.jpg"],
}
