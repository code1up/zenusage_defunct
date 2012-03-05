Ext.define("ZenUsage.view.ServiceTabView", {
    extend: "Ext.TabPanel",
    xtype: "servicetabview",

    config: {
        title: "Xxx",
        activeTab: 0,

        layout: {
            animation: 'slide'
        },

        tabBar: {
            docked: "bottom",

            layout: {
                pack: "center",
                align: "center"
            }
        },

        items: [
            {
                xtype: "serviceaboutview"
            },
            {
                xtype: "serviceliveview"
            },
            {
                xtype: "servicehistoryview"
            }
        ]
    }
});
