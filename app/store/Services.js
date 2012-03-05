Ext.define("ZenUsage.store.Services", {
    extend: "Ext.data.Store",

    config: {
        model: "ZenUsage.model.Service",
        sorters: "alias",

        data: [
            { alias: "Home" },
            { alias: "Office" }
        ]
    }
});
