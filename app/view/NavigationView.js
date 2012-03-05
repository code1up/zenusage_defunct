Ext.define("ZenUsage.view.NavigationView", {
    extend: "Ext.navigation.View",
    xtype: "navigationview",

    config: {
        autoDestroy: false, // TODO: why?

        navigationBar: {
            items: [
                {
                    xtype: "button",
                    id: "editAccountsButton",
                    ui: "action",
                    text: "Edit",
                    align: "right"
                },
                {
                    xtype: "button",
                    id: "doneEditingAccountsButton",
                    ui: "decline",
                    text: "Done",
                    align: "right",
                    hidden: true
                }
            ]
        },

        items: [
            {
                xtype: "accountlistview"
            }
        ]
    },
});
