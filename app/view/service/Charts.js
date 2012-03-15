Ext.define("App.view.service.Charts", {
    extend: "Ext.Panel",
    xtype: "servicecharts",

    config: {
        title: "Charts",
        iconCls: "star",
        html: "Charts",
        styleHtmlContent: true,

        items: [
            {
                xtype: "toolbar",
                docked: "top",
                title: "Charts"
            }
        ]
    }
});
