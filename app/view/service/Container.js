Ext.define("App.view.service.Container", {
    extend: "Ext.TabPanel",
    xtype: "servicecontainer",

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
                xtype: "serviceabout"
            },
            {
                xtype: "servicelive"
            },
            {
                xtype: "servicehistory"
            }
        ]
    }
});
