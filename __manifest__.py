{
    'name': 'Freinte de stock',
    'version': '19.0.1.0.0',
    'summary': 'Réduit automatiquement de  la quantité mise en stock lors de la réception (perte naturelle)',
    'description': """
        Module de freinte : permet de calculer et d'appliquer automatiquement les pertes naturelles de quantité ou de poids des produits stockés selon des règles prédéfinies (temps, température, humidité, type de produit, etc.).
    """,
    'author': 'Mamenosoa',
    'category': 'Inventory/Inventory',
    'depends': ['stock', 'purchase_stock', 'purchase'],
    'data': [
        'views/product_template_views.xml',
        'views/stock_move_line_view.xml',
        'views/purchase_order_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
