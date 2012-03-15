Ext.define("App.view.tablet.Container", {
    extend: "Ext.Container",
    xtype: "mainview",

    config: {
		fullscreen: true,
        layout: "hbox",

        items: [
            {
                xtype: "navigator",
                flex: 1
            },
            {
                xtype: "spacer",
                width: "1px",
                style: "background-color: #000000"
            },
            {
                xtype: "servicecontainer",
                id: "serviceContainer",
                flex: 2
            }
        ]
    }
});
