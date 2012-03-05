Ext.define("ZenUsage.view.tablet.MainView", {
    extend: "Ext.Container",
    xtype: "mainview",

    config: {
		fullscreen: true,
        layout: "hbox",

        items: [
            {
                xtype: "navigationview",
                flex: 1
            },
            {
                xtype: "spacer",
                width: "1px",
                style: "background-color: #000000"
            },
            {
                xtype: "servicetabview",
                flex: 3
            }
        ]
    }
});
