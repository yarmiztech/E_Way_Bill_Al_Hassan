{
    "name": "E Way Bill",
    "summary": "This Module is For E Way Bill",
    "version": "14.0.1.3.5",
    "author": "Enzapps",
    "category": "base",
    "images": ["images/galvanisation.jpg"],
    "support": "info@enzapps.com",
    "website": "https://www.enzapps.com/",
    "depends": ['base', 'account','contacts', 'stock', 'product','sale', 'sale_management', 'purchase'],
    "data": [
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "views/way_bill.xml",
             ],
    "installable": True,
    "application":True,
}
