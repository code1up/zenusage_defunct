Ext.define("ZenUsage.view.AccountListView", {
    extend: "Ext.List",
    xtype: "accountlistview",

    config: {
        title: "Accounts",

        store: "Accounts",
        itemTpl: "{userName}",

        onItemDisclosure: true
    }
});
