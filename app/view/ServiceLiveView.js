Ext.define("ZenUsage.view.ServiceLiveView", {
    extend: "Ext.Panel",
    xtype: "serviceliveview",

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
