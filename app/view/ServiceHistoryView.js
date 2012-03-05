Ext.define("ZenUsage.view.ServiceHistoryView", {
    extend: "Ext.Panel",
    xtype: "servicehistoryview",

    config: {
        title: "History",
        iconCls: "star",
        html: "History",
        styleHtmlContent: true,

        items: [
            {
                xtype: "toolbar",
                docked: "top",
                title: "History"
            }
        ]
    }
});
