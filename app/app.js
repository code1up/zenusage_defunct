Ext.application({
    name: "ZenUsage",

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
