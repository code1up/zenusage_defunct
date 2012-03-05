Ext.define("ZenUsage.view.ServiceAboutView", {
    extend: "Ext.Panel",
    xtype: "serviceaboutview",

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
