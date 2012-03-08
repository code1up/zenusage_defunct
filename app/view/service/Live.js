Ext.define("App.view.service.Live", {
    extend: "Ext.Panel",
    xtype: "servicelive",

    config: {
        title: "Live",
        iconCls: "star",
        html: "Live",
        styleHtmlContent: true,

        items: [
            {
                xtype: "toolbar",
                docked: "top",
                title: "Live"
            }
        ]
    }
});
