Ext.define("App.view.service.History", {
    extend: "Ext.Panel",
    xtype: "servicehistory",

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
