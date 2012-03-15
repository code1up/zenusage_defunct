(function() {
    var backButton = Ext.create("Ext.Button", {
        id: "backButton",
        ui: "back",
        text: "Back",
        align: "left",
        hidden: true
    });

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
                    xtype: "titlebar",
                    docked: "top",
                    title: "About",

                    items: [
                        backButton
                    ]
                }
            ]
        }

        // TODO: HERE
    });
})();
