Ext.application({
    name: "App",

    profiles: [
        "Phone",
        "Tablet"
    ],

    models: [
        "Account",
        "Service"
    ],

    stores: [
        "Accounts",
        "Services"
    ]
});
