Ext.define("ZenUsage.view.phone.MainView", {
    extend: "Ext.Container",
    xtype: "mainview",

    config: {
		fullscreen: true,
        layout: "fit",

        items: [
            {
                xtype: "navigationview"
            }
        ]
    }
});
