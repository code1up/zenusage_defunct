Ext.define("App.view.service.About", {
    extend: "Ext.Panel",
    xtype: "serviceabout",

    config: {
        title: "About",
        iconCls: "star",
        html: "About",
        styleHtmlContent: true,

        items: [
            {
                xtype: "toolbar",
                docked: "top",
                title: "About"
            }
        ]
    }
});
