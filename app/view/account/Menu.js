Ext.define("App.view.account.Menu", {
    extend: "Ext.Panel",
    xtype: "accountmenu",

    config: {
        layout: {
            type: "vbox"
        },

        floating: true,
        modal: true,
        // hideOnMaskTap: true,
        width: 256,
        scroll: false,

        items: [
            {
                xtype: "button",
                ui: "decline",
                text: "Delete",
                style: "margin: 2px;"
            },
            {
                xtype: "button",
                // ui: "action",
                text: "Set Credentials",
                style: "margin: 2px;"
            }
        ]
    }
});
