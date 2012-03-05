Ext.define("ZenUsage.view.ServiceListView", {
    extend: "Ext.List",
    xtype: "servicelistview",

    config: {
        title: "Services",

        store: "Services",
        itemTpl: "{alias}"
    }
});
