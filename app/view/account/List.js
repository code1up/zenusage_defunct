Ext.define("App.view.account.List", {
    extend: "Ext.List",
    xtype: "accountlist",

    config: {
        store: "Accounts",

        // ui: "round",
        // pinHeaders: true, // TODO

        // styleHtmlContent: true,
        itemTpl: "{userName}"

        // styleHtmlContent: true,
        // itemTpl: "<div class='x-list-item-label'>{userName}</div>"

        // onItemDisclosure: true
    }
});
