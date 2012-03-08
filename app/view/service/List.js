Ext.define("App.view.service.List", {
    extend: "Ext.List",
    xtype: "servicelist",

    config: {
        title: "Services",

        store: "Services",
        itemTpl: "{alias}"
    }
});
