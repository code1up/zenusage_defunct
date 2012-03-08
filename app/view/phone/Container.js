Ext.define("App.view.phone.Container", {
    extend: "Ext.Container",
    xtype: "mainview",

    config: {
		fullscreen: true,
        layout: "fit",

        items: [
            {
                xtype: "navigationview",
                id: "navigationView"
            }
        ]
    }
});
