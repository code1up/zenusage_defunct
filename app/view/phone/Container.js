Ext.define("App.view.phone.Container", {
    extend: "Ext.Container",
    xtype: "phonecontainer",

    config: {
		fullscreen: true,
        layout: "card",

        items: [
            {
                xtype: "navigator"
            },
            {
                xtype: "servicecontainer",
                id: "servicecontainer"
            }
        ]
    }
});
